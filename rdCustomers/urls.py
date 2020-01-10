from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


from rdCustomers import views

urlpatterns  = [
    path('<uuid:id>/',views.index,name = 'rd_customer_view'),
    path('activate/<uuid:id>/',views.activate,name = 'rd_customer_activate'),
    # path('data/<uuid:id>',views.data, name  = 'rd_customer_data'),
    path('paykisht/<uuid:id>/', views.paykisht, name='pay_kisht'),
]