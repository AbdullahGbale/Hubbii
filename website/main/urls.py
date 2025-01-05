from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/delete/<int:project_id>/', views.project_delete, name='project_delete'),
    path('default-profile/', views.default_profile, name='default_profile_url'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('certificates/', views.certificates, name='certificates'),
    path('search/', views.search, name='search'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('portfolio/', views.portfolio, name='portfolio'),
    #path('', views.portfolio, name='portfolio'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

