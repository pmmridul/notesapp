# Simple Notes App

This is a simple notes app built with React, Django and PostgreSQL.

Originally forked from [https://github.com/Hitstar53/notesapp](https://github.com/Hitstar53/notesapp).

## Requirements

1. Python
2. Node.js
3. React
4. PostgreSQL

## PostgreSQL Configuration
1. Create the user
```
CREATE ROLE myuser WITH LOGIN PASSWORD 'password' CREATEDB;
```
2. Create database
```
CREATE DATABASE mydatabase
    WITH OWNER = myuser
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;
```

## Installation
1. Clone the repository
```
git clone https://github.com/pmmridul/notesapp.git
```
2. Create a virtual environment and activate it
```
virtualenv venv
source venv/bin/activate
```
3. Install the requirements
```
pip install -r requirements.txt
```
4. To apply database migrations
```
python manage.py migrate
```
5. To create Django admin user
```
python manage.py createsuperuser
```
6. Run the server
```
python manage.py runserver
```

## Frontend - React
1. Open another terminal and navigate to the mynotes directory
```
cd mynotes
```
2. Install the dependencies
```
npm install
```
3. Run the app
```
npm start
```
