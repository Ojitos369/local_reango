# Python
import os
import json
import requests
from uuid import uuid4

# Ojitos369
from ojitos369.utils import get_d

# User
from app.core.bases.apis import PostApi, GetApi


class ChatOllama(PostApi, GetApi):
    def main(self):
        """ 
        qwen2.5:3b               357c53fb659c    1.9 GB    20 hours ago
        llama3.2:3b              a80c4f17acd5    2.0 GB    6 days ago
        deepseek-coder:latest    3ddd2d3fc8d2    776 MB    6 days ago
        deepseek-r1:1.5b         a42b25d8c10a    1.1 GB    6 days ago
        """
        self.show_me()
        model = self.data.get("model", "qwen2.5:3b")
        clave = self.data.get("clave", str(uuid4()))
        message = self.data.get("message", None)
        if not message:
            raise self.MYE("message is required")

        self.crear_conexion()
        query = """INSERT INTO chats (uuid, model, message, usuario) VALUES (%(uuid)s, %(model)s, %(message)s, 'user')"""
        query_data = {"uuid": clave, "model": model, "message": message}
        if not self.conexion.ejecutar(query, query_data):
            self.conexion.rollback()
            return self.MYE("Error al guardar el mensaje")
        self.conexion.commit()

        query = """SELECT * FROM chats where uuid = %(uuid)s order by created_at asc"""
        query_data = {"uuid": clave}
        df = self.conexion.consulta_asociativa(query, query_data)
        print(df)
        chats = ""
        for chat in df.iloc:
            chats += f"{chat['usuario']}: {chat['message']}\n"
        
        link = "http://localhost:11434/api/generate"
        prompt = chats
        print(f"prompt: {prompt}")
        
        data = {
            "model": model,
            "prompt": prompt
        }
        
        pensamiento = ""
        respuesta = ""
        pensando = False

        for response in self.stream_responses(data, link):
            rs = json.loads(response)
            # print(rs)
            done = rs["done"]
            
            if not done:
                message = rs["response"]
                if "<think>" in message:
                    print("pensando: ")
                    pensando = True
                    message = message.replace("<think>", "").replace("\n", "")
                
                if not pensando:
                    respuesta += message

                if "</think>" in message:
                    pensando = False
                    message = message.replace("</think>", "").replace("\n", "")
                    pensamiento += message
                    print(message, end="")
                    print(f"\n{'-'*50}")
                    print(f"Respondiendo:")
                else:
                    print(message, end="")
                
                if pensando:
                    pensamiento += message

        os.system(f"ollama stop {model}")
        query = """INSERT INTO chats (uuid, model, message, usuario) VALUES (%(uuid)s, %(model)s, %(message)s, 'ollama')"""
        query_data = {"uuid": clave, "model": model, "message": respuesta}
        if not self.conexion.ejecutar(query, query_data):
            self.conexion.rollback()
            return self.MYE("Error al guardar el mensaje")
        self.conexion.commit()
        self.response = {"respuesta": respuesta, "pensamiento": pensamiento, "clave": clave}

    def stream_responses(self, data, link):
        response = requests.post(link, json=data, stream=True)
        for line in response.iter_lines():
            if line:
                yield line.decode('utf-8')

