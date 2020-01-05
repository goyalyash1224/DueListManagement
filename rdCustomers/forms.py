from django import forms
from django.forms import widgets
from datetime import date
from rdCustomers.models import *

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        days = [(d, d) for d in range(1,32)]
        months = [(m, m) for m in range(1,13)]
        years = [(year, year) for year in (2011, 2012, 2013)]
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        D = date(
                day=int(datelist[0]),month=int(datelist[1]),year=int(datelist[2]),
            )
        return D

class ItemForm(forms.Form):
    partial_date_part = forms.CharField(widget=forms.RadioSelect)
    partial_date_date = DateSelectorWidget( )




class ActivateCustomerForm(forms.ModelForm):


    class Meta:
        model = RdUser
        fields = ['serial_no','Denom_value','start_date','total_policy_year']