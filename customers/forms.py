from django import forms
from .models import Customer


class NewCustomerForm(forms.ModelForm):


    class Meta:
        model = Customer
        exclude =('id','agent','created_at','last_updated')