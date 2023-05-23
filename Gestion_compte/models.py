from django.db import models
from django.conf import settings

# Create your models here.
class profile(models.Model):
    photo = models.FileField(upload_to="uploads/")
    bio = models.CharField(max_length=50)
    User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
