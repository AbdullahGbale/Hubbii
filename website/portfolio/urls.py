from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
   
]


urlpatterns += [
    path('', views.home, name='home'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('projects/', views.projects, name='projects'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),  # User profile
 
    path('search/', views.search_users, name='search_users'),



    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/collaborate/', views.collaborate, name='collaborate'),


    path('collaborate/', views.collaborate, name='collaborate'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),



    path('certificate/', views.certificate, name='certificate'),  # Display certificates
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),  # Add portfolio post
    path('add_certificate/', views.add_certificate, name='add_certificate'),  # Add certificate post
    path('add_project/', views.add_project, name='add_project'),  # Add project post



    path('posts/', views.post_list, name='post_list'),  # URL for viewing posts
    path('create/', views.create_post, name='create_post'),
    path('category/<str:category>/', views.posts_by_category, name='posts_by_category'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),





    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='pwd_reset/pwd_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pwd_reset/pwd_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pwd_reset/pwd_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pwd_reset/pwd_reset_complete.html'), name='password_reset_complete'),
]


