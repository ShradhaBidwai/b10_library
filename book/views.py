from django.shortcuts import render, HttpResponse, redirect
from.models import Book



# import logging
# logger = logging.getLogger('first')

# Create your views here.
def welcome(request):
    #  return render(request,"home.html")
     # return  HttpResponse("welcome")
    books=Book.objects.all()
    return render(request,"home.html",{"all_books":books,'Model': Book})  #backend se data ayega


def create_book(request):
    print(request.method)
    if request.method == "GET":
        return render(request,"createbook.html")  #backend se data ay,{"ega
    elif request.method == "POST":

        data= request.POST
        if not data.get("Id"):
            Book.objects.create(title=data.get("title"),author=data.get("auth"),publication_date=data.get("pub_date"),price=data.get("prc"))
        else:
            book_obj=Book.objects.get(id=int(data.get("id")))
            book_obj.title = data.get("title")
            book_obj.author = data.get("auth")
            book_obj.publication_date= data.get("pub_date")
            book_obj.price= data.get("prc")
            Book.obj.save() 

        return redirect("home")



def edit_book(request, bid):
    try:
        book_obj=Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        return render(request,"createbook.html",{"book":book_obj})

import sys                    
def delete_book(request,bid):
   
   
    try:
        book_obj=Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
     
        if request.POST.get("type_of_delete") == "HardDelete":
            book_obj.delete()      # hard delete
        else:
            book_obj.isdeleted = True       #soft delete
            book_obj.save()
        return redirect("home")

def show_deleted_books(request):
    deleted_books=Book.objects.filter(isdeleted = True)
    return render(request,"deleted_books.html",{"deleted_books": deleted_books})


def restore_book(request,bid):
    try:
        book_obj=Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        # book_obj.delete()      # hard delete
        book_obj.isdeleted = False      #soft delete
        book_obj.save()
        return redirect("home")




#status code
# 200
# 3xx
# 500 internal server

# create ke liyeid nahi lagegi
# delete and get ke liye id lagti hai

#soft delete= database se delete nahi hoga uska flag delete hoga