from django.urls import path
from .views import PostList, PostDetail
from .views import ProjectListAPIView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
]
