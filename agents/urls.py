from django.urls import path, include, re_path

from django.contrib.auth import urls
from django.contrib.auth import views as auth_views

from agents import views as agents_views


urlpatterns = [
    path('',agents_views.home, name = "Home"),
    path('login/', auth_views.LoginView.as_view(template_name='registrations/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',agents_views.signup,name = 'signup'),
    path('profile/',agents_views.view_profile,name = 'view_profile'),
    path('profile/edit',agents_views.edit_profile,name = 'edit_profile'),
    path('change-password/',agents_views.change_password,name = 'change_password'),
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registrations/password_change_done.html'),
    name='password_change_done'),



re_path(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='registrations/password_reset.html',
        email_template_name='registrations/password_reset_email.html',
        subject_template_name='registrations/password_reset_subject.txt'
    ),
    name='password_reset'),
re_path(r'^reset/done/$',
    auth_views.PasswordResetDoneView.as_view(template_name='registrations/password_reset_done.html'),
    name='password_reset_done'),
re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='registrations/password_reset_confirm.html'),
    name='password_reset_confirm'),
re_path(r'^reset/complete/$',
    auth_views.PasswordResetCompleteView.as_view(template_name='registrations/password_reset_complete.html'),
    name='password_reset_complete'),




]