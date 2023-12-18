"""Libraryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from book.views import welcome,create_book,edit_book,delete_book,show_deleted_books,restore_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', welcome, name='home'),
    path('add-book/',create_book,name="add_book"),
    path('edit-book/<int:bid>/', edit_book , name="edit_book"),
    path('delete-book/<int:bid>/', delete_book , name="delete_book"),
    path('delete-books/',show_deleted_books , name="show_deleted_books"),
    path('restore_book/<int:bid>/', restore_book, name='restore_book'),

  
    # path('index/', index),  
    # path('file_list/', file_list, name='file_list'),
    # path('upload_file/', upload_file, name='upload_file'),
   


    path('csv/', include('csv_upload.urls')), # include all the urls from csv_upload app, 
]


# http://127.0.0.1:8000/csv/upload-csv/


# from django.conf import settings
# from django.conf.urls.static import static

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)