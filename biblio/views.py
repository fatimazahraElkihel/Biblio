from django.shortcuts import render


def cart(request):
    context= {}
    return render(request,'biblio\cart.html',context)
def checkout(request):
    context= {}
    return render(request,'biblio\checkout.html',context)
def store(request):
    context= {}
    return render(request,'biblio\store.html',context)



