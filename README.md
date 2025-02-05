This app is based in 
[https://github.com/Ojitos369/reango](https://github.com/Ojitos369/reango) 
and [https://github.com/Ojitos369/base-react](https://github.com/Ojitos369/base-react)  

## Activate the environment

* VENV
```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

* CONDA
```shell
conda create -y --name rng python=3.12
conda activate rng
pip install -r requirements.txt
```

* DOCKER
```shell
docker-compose up
```

## Install npm packages
    
```shell
cd front
npm install
```

## Work  
you can edit react app an make the build

and run django command to migrate view

```shell
python manage.py migrate_view
```


## Docker configs  
### docker-compose.yml  
> services > web > container_name  
- - Put the name of your project  
> services > web > ports  
- - Put the port you want to use  

### dockerfile  
##### Envs  
Put here you environment variables  
##### Dependencies  
Put here the dependencies do you need to install in your container  
##### Locales  
Configure the locals to the zone do you need  
##### Crons  
Add Cron jobs to do you need and put the shell script in the folder crons  
    * you can use test cron like example  
##### Python  
If you change de requirements mode for any other, you need change the method to install the python packages here  

