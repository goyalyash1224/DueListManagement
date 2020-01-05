from django.shortcuts import render, get_object_or_404, redirect
from rdCustomers.models import *
from customers.models import  *
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import Item
from django.forms.models import modelform_factory
from .forms import DateSelectorWidget, ActivateCustomerForm
from django import forms
from django.forms import widgets
# Create your views here.

def index(request, id):
    active_customer = get_object_or_404(Customer,pk=id)
    rd_customer = active_customer.rd_user
    return render(request,'rdCustomers/index.html',{'rd_customer':rd_customer})

def activate(request,id):
    customer = get_object_or_404(Customer, pk=id)

    if request.method == 'POST':
        form = ActivateCustomerForm(request.POST)
        if form.is_valid():
            active_rd = form.save(commit=False)
            active_rd.customer = customer
            active_rd.save()
            return redirect('rd_customer_data', id =customer.id)
    else:
        form = ActivateCustomerForm()
    return render(request, 'rdCustomers/activate_user.html',{'form': form,'customer':customer})


class MyDatAppView(View):
    form_class = modelform_factory(Item ,
                                   exclude=[],
                                   widgets={ 'partial_date_date':
                                              DateSelectorWidget() ,})
    initial = {'some_comment': '-*-', }
    template_name = 'customer/includes/form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            m=form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})