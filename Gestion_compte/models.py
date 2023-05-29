from django.db import models
from django.conf import settings
from Gestion_book.models import Book

# Create your models here.
class client(models.Model):  
    photo = models.FileField(upload_to="uploads/")
    bio = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=False)
    name=models.CharField(max_length=200,null=True)
    User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class order(models.Model):
    client = models.ForeignKey(client,on_delete=models.SET_NULL,blank=True,null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.transaction_id) 

class orderItem(models.Model):
    produit =models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(order,on_delete=models.SET_NULL,null=True)
    quantite = models.IntegerField(default=0,null=True,blank=True)
    date_ajoute=models.DateTimeField(auto_now_add=True)

class adresse_livraison(models.Model):
    client=models.ForeignKey(client,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(order,on_delete=models.SET_NULL,null=True)
    adress = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=100,null=False)
    zipcode = models.CharField(max_length=50,null=False)
    date_ajout=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adress
