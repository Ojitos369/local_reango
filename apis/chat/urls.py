from django.urls import path

from .api import (
    ChatOllama, 
)

app_name = "chat"
urlpatterns = [
    path("chat_ollama/", ChatOllama.as_view(), name=f"{app_name}_chat_ollama"),
]