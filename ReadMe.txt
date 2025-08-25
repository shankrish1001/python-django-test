Django:
--a back-end server side web framework.
--to build web pages using Python.

1- Install Django
(.venv) PS D:\workpy\python-django-test> python -m pip install Django
(.venv) PS D:\workpy\python-django-test> pip install django

2- Django Create Project:
(.venv) PS D:\workpy\python-django-test> django-admin startproject my_test_project

--check dir list:
my_test_project
    manage.py
    my_test_project/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py

3- Run Django Project
(.venv) PS D:\workpy\python-django-test\my_test_project> python manage.py runserver

--check in browser, type 127.0.0.1:8000 in the address bar.

4- Create Django Create App
An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

(.venv) PS D:\workpy\python-django-test\my_test_project> python manage.py startapp my_test_app

5- append in settings.py at INSTALLED_APPS = ['my_test_app',]

6- update Django Views in views.py.
from django.http import HttpResponse

def shantest(request):
    return HttpResponse("Hi Shan, Welcome!")

6- update Django URLs in urls.py.
from django.contrib import admin
from django.urls import path
from demo import views  # import your view here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shantest),
]


7- Run Django Project
(.venv) PS D:\workpy\python-django-test\my_test_project> python manage.py runserver
