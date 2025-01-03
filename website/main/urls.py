from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('default-profile/', views.default_profile, name='default_profile_url'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('certificates/', views.certificates, name='certificates'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('search/', views.search, name='search'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
