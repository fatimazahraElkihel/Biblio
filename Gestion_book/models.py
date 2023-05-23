from django.db import models

# Create your models here.
class Categorie(models.Model):
    Desc = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/")

class auteur(models.Model):
    Nom = models.CharField(max_length=50)
    Desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to="profiles/")

class Book(models.Model):
    ISBN = models.IntegerField(primary_key=True)
    Photo = models.ImageField(upload_to="books/")
    Titre = models.CharField(max_length=20)
    Edition = models.CharField(max_length=20)
    Desc = models.CharField(max_length=500)
    Prix_vente = models.FloatField()
    Prix_empr = models.FloatField()
    Audio = models.FileField(upload_to="")
    Auteur = models.ForeignKey(auteur, on_delete=models.CASCADE)
    Categorie = models.OneToOneField(Categorie, on_delete=models.CASCADE)