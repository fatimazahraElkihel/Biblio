from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()

# Create your views here.

def signup(request):
   if request.method == "POST":
      form = SignupForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         messages.success(request, "Registration successful." )
         return redirect("store")

      messages.error(request, "Unsuccessful registration. Invalid information.")

   else:
      form = SignupForm()

   context = {"form" : form}

   return render (request, "accounts/signup.html", context)
