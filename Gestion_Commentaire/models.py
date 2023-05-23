from django.db import models
from django.conf import settings
from Gestion_book.models import Book

# Create your models here.
class Commententaire(models.Model):
    description = models.CharField(max_length=200)
    nbr_star = models.IntegerField(choices=((1,"one star"),(2,"two stars"),(3,"three stars"),(4,"four stars"),(5,"five star"))) #TODO: Solve error
    book = models.ForeignKey(Book,on_delete=models.CASCADE, null=True) #TODO: define book 
    User = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    


