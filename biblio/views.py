from django.shortcuts import render
from Gestion_book.models import Book

def cart(request):
    ontext= {}
    return render(request,'biblio\cart.html',context)
def checkout(request):
    context= {}
    return render(request,'biblio\checkout.html',context)
def store(request):
    produit = Book.objects.all()
    context= {'produit':produit}
    return render(request,'biblio\store.html',context)



