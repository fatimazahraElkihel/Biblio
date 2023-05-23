from django.shortcuts import render
from .models import auteur

# Create your views here.
def main(request):
    auteur(nom="Berchil", desc="tktktktktk").save()
