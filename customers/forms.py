from django import forms
from .models import Customer


class NewCustomerForm(forms.ModelForm):


    class Meta:
        model = Customer
        fields = ['name', 'dob']