from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('certificates/', views.certificates, name='certificates'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('search/', views.search, name='search'),
]
