from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def signup(request):
        if request.method =="POST":
           username = request.POST.get("username")
           password = request.POST.get("password")
           user = User.objects.create_user(username=username,
                                           password=password)
           login(request, user)
           return redirect('store')
        return render(request, 'accounts/signup.html')
