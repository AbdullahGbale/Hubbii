from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import signin_view

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/delete/<int:project_id>/', views.project_delete, name='project_delete'),
    path('default-profile/', views.default_profile, name='default_profile_url'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('certificates/', views.certificates, name='certificates'),
    path('search/', views.search, name='search'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    #path('login/', LoginView.as_view(template_name='login.html'), name='login'),
     #path('login/', auth_views.LoginView.as_view(), name='login'),
     #path('login/', signin_view, name='login'),


    path('portfolio/', views.portfolio, name='portfolio'),
    #path('', views.portfolio, name='portfolio'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),



    path('rate/<int:project_id>/', views.rate_project, name='rate_project'),
    path('compliment/<int:project_id>/', views.compliment_project, name='compliment_project'),
    path('collaborate/<int:project_id>/', views.collaborate_project, name='collaborate_project'),
    path('react/<int:project_id>/', views.react_to_project, name='react_to_project'),
    path('share/<int:project_id>/', views.share_project, name='share_project'),
    path('team/<int:project_id>/', views.manage_team, name='manage_team'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urls.py
urlpatterns += [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
