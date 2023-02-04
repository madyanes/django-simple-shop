# Simple Shop
This simple shop system is built on top of Python 3.11 using Django framework.

## Requirements
- Python 3.11
- Pipenv

## Before running locally
1. Create a file named `.env` inside this project root directory.
2. Add a variable `SECRET_KEY=[your_secret_key]`.

## Run locally
1. If you're running this project for the first time: `pipenv install`
2. Use the virtual environment: `pipenv shell`
3. Migrate the database: `python manage.py migrate`
4. Make sure you have a superuser to login to django admin page: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver 8000`
