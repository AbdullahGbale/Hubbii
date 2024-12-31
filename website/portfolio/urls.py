from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
]


urlpatterns += [
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('projects/', views.projects, name='projects'),
    path('portfolio-section/', views.portfolio_section_list, name='portfolio_section_list'),
   


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

