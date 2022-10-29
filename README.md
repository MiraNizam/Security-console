# Security console

**Security console** is inner repository for bank employees. It records and show data about visits and visitors. 
The script uses Django framework.

## Getting Started

Below you will find instructions on how to use **Security console**.  

### Prerequisites

Please be sure that **Python3** is already installed. Version >= 3.5.0main. 

### Installing
1. Clone the repository:
```
git clone https://github.com/MiraNizam/django-orm-watching-storage.git
```
2. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
3. You should create or receive from your boss the file `.env`  with the following information:

* SECURE_ENGINE=(for example: django.db.backends.postgresql_psycopg2)
* SECURE_HOST=(used host)
* SECURE_PORT=(used port)
* SECURE_NAME=(name)
* SECURE_USER=(user)
* SECURE_PASSWORD=(user_password)
* SECURE_SECRET_KEY=(secret_key to the data)

5. How to run code:

Input: 
```
python manage.py runserver 0.0.0.0:8000
```
Go to the link: 

The server runs on [localhost 127.0.0.1:8000](http://127.0.0.1:8000/)

You see the main page "Активные карты доступа". Also you have access to the page "Список пользователей в хранилище" and the page with visits for every passcard. 
    

### Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).