from django.db import models

# Create your models here.

class CustomBookManager(models.Manager):
    def get_active_objects(self):            
        return self.filter(isdeleted=False)   #give only active data


    def get_inactive_objects(self):            
        return self.filter(isdeleted=True)   #gives only in_active data


class Book(models.Model):
    PUBLICATION_CHOICE =[
        ('PB1','publication 1'),
        ('PB2','publication 2'),
        ('PB3','publication 3'),
        ('PB4', 'PUBLICATION 4')
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isdeleted = models.BooleanField(default=False)
    price = models.IntegerField()
    objects = CustomBookManager()
    publication_name = models.CharField(max_length=3, choices=PUBLICATION_CHOICE, null=True)
    


    def __str__(self):
        return self.title
    
    class Meta:              #for remane
        db_table="book"
