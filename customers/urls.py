from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard, name = "dashboard"),
    path('new/',views.add_new_customer, name = 'new_customer'),
    path('<uuid:id>/',views.customer_profile,name="customer_profile"),

]