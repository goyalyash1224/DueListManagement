from django.urls import path, include

from django.contrib.auth import urls
from django.contrib.auth import views as auth_views

from agents import views as agents_views


urlpatterns = [
    path('',agents_views.home, name = "Home"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup',agents_views.signup,name = 'signup'),
#     path('reset/',
#     auth_views.PasswordResetView.as_view(
#         template_name='password_reset.html',
#         email_template_name='password_reset_email.html',
#         subject_template_name='password_reset_subject.txt'
#     ),
#     name='password_reset'),
#     path('reset/done/',
#     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
#     name='password_reset_done'),
# url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
#     name='password_reset_confirm'),
# url(r'^reset/complete/$',
#     auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
#     name='password_reset_complete'),
#     path('logout',auth_views.LogoutView.as_view(),name = 'logout')


]