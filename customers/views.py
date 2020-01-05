from django.shortcuts import render,redirect
from django.http import HttpResponse
from customers.models import *
from django.contrib.auth.decorators import login_required
from .forms import NewCustomerForm

from django.contrib.auth.models import User

# Create your views here.
@login_required
def customers_home(request):
    if request.user.is_authenticated:
        return render(request, 'customers/home.html',{'user':request.user})
    else:
        return redirect('Home')




def add_new_customer(request):
    user = request.user

    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.agent = user
            customer.save()
            return redirect('customers_home')
    else:
        form = NewCustomerForm()
    return render(request, 'customers/new_customer.html',{'form': form})
