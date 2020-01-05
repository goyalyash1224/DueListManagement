from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


from rdCustomers import views

urlpatterns  = [
    path('customer/<int:id>/',views.index,name = 'rd_customer_data'),
    path('customer/activate/<int:id>',views.activate,name = 'rd_customer_activate')
]