from django.shortcuts import render, get_object_or_404, redirect
from rdCustomers.models import *
from customers.models import  *
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import Item
from django.forms.models import modelform_factory
from .forms import DateSelectorWidget, ActivateCustomerForm , PayKishtForm
from django import forms
from django.forms import widgets
# Create your views here.

def index(request, id=id):
    rd_customer = get_object_or_404(RdUser,pk=id)
    customer = rd_customer.customer
    return render(request,'rdCustomers/index.html',{'customer':customer ,'rd_customer':rd_customer})

def activate(request,id=id):
    customer = get_object_or_404(Customer, pk=id)

    if request.method == 'POST':
        form = ActivateCustomerForm(request.POST)
        if form.is_valid():
            active_rd = form.save(commit=False)
            active_rd.customer = customer
            active_rd.save()
            return redirect('rd_customer_view', id = active_rd.id)
    else:
        form = ActivateCustomerForm()
    return render(request, 'rdCustomers/activate_user.html',{'form': form,'customer':customer})


def paykisht(request, id):
    rd_customer = get_object_or_404(RdUser, pk=id)
    customer = rd_customer.customer


    if request.method == 'POST':
        form = PayKishtForm(request.POST)
        if form.is_valid():
            rd_kisht = form.save(commit=False)
            rd_kisht.rd_user = rd_customer
            rd_kisht.save()
            return redirect('rd_customer_view', id=rd_kisht.rd_user.id)
    else:
        form = PayKishtForm()
        context = {

            'customer': customer,
            'rd_customer': rd_customer,
            'form': form
        }
        return render(request, 'rdCustomers/payKisht.html', (context))




def kishtdata(request, id):
    rd_customer = get_object_or_404(RdUser, pk=id)

    context = {

        'rd_customer': rd_customer,
    }
    return render(request, 'rdCustomers/kishtData.html', (context))