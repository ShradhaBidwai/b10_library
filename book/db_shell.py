from book.models import Book

# exec(open(r"D:\SHRADA PYTHON B10\b10_env\Django_projects\Libraryproject\book\db_shell.py").read())  #for reading perpose

'''custom model manager in django----
In Django, a model manager is a class that encapsulates queries for a particular
model. You can create a custom model manager by defining a class that inherits 
from django.db.models.Manager and then attaching an instance of this manager to
your model.'''


# Book.objects.filter(isdeleted=True)  #in_active     #hey n use karta apn custom objects throug karu shakto , tya sati ek class create karycha in models.py madhe i.e. CustomBookManager
# Book.objects.filter(isdeleted=False)   #active

#custom model manager:

# print(Book.objects.all())    
#o/p: <QuerySet [<Book: Book1>, <Book: Book2>, <Book: Book3>, <Book: Book4>]>


#print(Book.objects.get_active_objects())   #gives filter data i.e. gives only active data
# o/p:   <QuerySet [<Book: Book1>, <Book: Book2>]>     false


# print(Book.objects.get_inactive_objects())   #give only inactive data i.e True
# o/p: <QuerySet [<Book: Book3>, <Book: Book4>]>
