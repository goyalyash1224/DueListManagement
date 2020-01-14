from django import forms
from .models import Customer, Document


class NewCustomerForm(forms.ModelForm):


    class Meta:
        model = Customer
        exclude =('id','agent','created_at','last_updated')






class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)

