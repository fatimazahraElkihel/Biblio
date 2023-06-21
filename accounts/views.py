from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib import messages
#from .forms import OrderForm, CreateUserForm
#from .filters import OrderFilter
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

def registerPage(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def loginPage(request):
     context = {}
     return render(request, 'accounts/login.html',context)

