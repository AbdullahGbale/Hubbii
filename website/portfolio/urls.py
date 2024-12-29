from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
]


urlpatterns += [
    path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('projects/', views.projects, name='projects'),
    path('portfolio-section/', views.portfolio_section_list, name='portfolio_section_list'),
    path('portfolio-section/add/', views.portfolio_section_add, name='portfolio_section_add'),
    path('contact/', views.contact_detail, name='contact_detail'),
    path('contact/edit/', views.contact_edit, name='contact_edit'),
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/add/', views.experience_add, name='experience_add'),
    path('skill/', views.skill_list, name='skill_list'),
    path('skill/add/', views.skill_add, name='skill_add'),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

