python -m pip install --upgrade pip
pip install django
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
python manage.py runserver

# При изменении бд
python manage.py makemigrations
python manage.py migrate
# Регистрация админа
python manage.py createsuperuser

Maxim
max@mail.com
123456

pip install pillow

venv\Scripts\activate