from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from haystack.views import SearchView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.project_list, name='project_list'),
    #path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('projects/', views.list_projects, name='projects'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('create_project/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),

    
    path('search/', SearchView(), name='search'),  # Use haystack's SearchView



    path('profile/<str:username>/follow/', views.follow_user, name="follow_user"),
    path('project/<int:project_id>/like/', views.like_project, name="like_project"),
    


    path('default-profile/', views.show_default_profile, name='default_profile_url'),
    
    



    path('project/<int:project_id>/request_collaboration/', views.send_collaboration_request, name='send_collaboration_request'),
    path('collaboration_request/<int:request_id>/accept/', views.accept_collaboration_request, name='accept_collaboration_request'),
    path('collaboration_request/<int:request_id>/reject/', views.reject_collaboration_request, name='reject_collaboration_request'),

]