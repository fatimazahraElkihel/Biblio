from django.contrib import admin
from . import models

admin.site.register(models.client)
admin.site.register(models.adresse_livraison)
admin.site.register(models.order)
admin.site.register(models.orderItem)
