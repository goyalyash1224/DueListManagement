from django import forms
from .models import Customer, Document


class NewCustomerForm(forms.ModelForm):


    class Meta:
        model = Customer
         HEAD
        exclude =('id','agent','created_at','last_updated')






class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)

        exclude =('id','agent','created_at','last_updated')
 ca4c233e4dc5bf499b6e3e3df1ac0f36c587e9c3
