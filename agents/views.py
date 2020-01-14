from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'agents/home.html')

def signup(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request,'registrations/signup.html', {
        'form':form
    })

def view_profile(request):
    args = {'user':request.user}
    return render(request,'agents/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view_profile')

    else:
        form = EditProfileForm()
        args = {'form':form}
        return render(request, 'agents/edit_profile.html',args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('password_change_done')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'registrations/password_change.html',args)

