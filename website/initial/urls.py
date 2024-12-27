from django.urls import path
from .views import PostList, PostDetail, ProjectListAPIView, PortfolioListCreateAPIView, PortfolioDetailAPIView

urlpatterns = [
    # Post APIs
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    # Project APIs
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    
    # Portfolio APIs
    path('portfolio/', PortfolioListCreateAPIView.as_view(), name='portfolio-list'),
    path('portfolio/<int:pk>/', PortfolioDetailAPIView.as_view(), name='portfolio-detail'),
]
