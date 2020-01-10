from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    count = User.objects.count()

    return render(request,'agents/home.html', {
        'count':count
    })

def signup(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html', {
        'form':form
    })

def dashboard(request):
    return render(request, 'agents/dashboard.html')