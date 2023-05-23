from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.auteur)
admin.site.register(models.Categorie)
admin.site.register(models.Book)