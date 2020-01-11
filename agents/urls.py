from django.urls import path, include

from django.contrib.auth import urls
from django.contrib.auth import views as auth_views

from agents import views as agents_views


urlpatterns = [
    path('',agents_views.home, name = "Home"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/',agents_views.signup,name = 'signup'),



]