from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


# from django.db import models

# class Employee(models.Model):
#     firts_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     email=models.EmailField(unique=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"










#step of upload csv in django

# 1)create a django project - django-admin startproject projectname
# -- navigate to the project directory: cd projectname

# 2)create a django app - py manage.py startapp appname

# 3) define model: in model.py file , define a model to represent the data you want to store from the CSV file

# 4) migration:  run on terminal

# python manage.py makemigrations
# python manage.py migrate

# 5) create from: create form.py in your app, create a form for handling file uploads:

# 6) create a view: Create a view to handle the file upload in your views.py file:

# 7)create templates: create a templates folder in your app, in templtaes folder create .html file to render the format

# 8)define urls: create urls.py file in your app, Define URLs for your views in the urls.py file within the  app:

# 9)Include these URLs in the projects  urls.py:

# 10) run the server:  python manage.py runserver

# Visit http://127.0.0.1:8000/csv/upload-csv/ in your browser, and you should see the file upload form.






