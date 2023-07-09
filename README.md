# Education_coursework_6
## WORK WITH DJANGO
### Allow to create scheduler transmission for sending messages to clients
## Requirements.
* Python
* Rest
* Postgres
## Installation
* Download repo
* Install requirements (pip install -r requirements.txt)
* Change env file
* Use Rest
## Prepare 
* prepare .env file
* create database for postgres
* prepare migrations (python .\manage.py makemigrations)
* make migrations(python .\manage.py migrate)
* prepare platform (python .\manage.py prepare_platform)
* add test data if you need (python .\manage.py loaddata .\data.json)
## Info about users and groups
After prepare platform you will have 
* groups moderator and users
* user admin@gmail.com (password admin)
* user moderator@gmail.com (password moderator)
* user test@gmail.com (password test)

! If you want to register new user, after creation you should add it to suitable group !

## How it works.
* Create messages
* Create clients for sending
* Create transmissions for sending (You can use scheduler)

## Interface
![img_1.png](img_1.png)

![img_2.png](img_2.png)

![img_3.png](img_3.png)

![img.png](img.png)

## Additional
* Author: Avramenko Nikolay
* Date of release: 2023/07/10
