from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
   
]


urlpatterns += [
    path('', views.home, name='home'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('projects/', views.projects, name='projects'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='pwd_reset/pwd_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pwd_reset/pwd_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pwd_reset/pwd_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pwd_reset/pwd_reset_complete.html'), name='password_reset_complete'),
]


