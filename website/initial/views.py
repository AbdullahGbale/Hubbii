from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import generics
from .models import Post, Project, Portfolio
from .serializers import PostSerializer, ProjectSerializer, PortfolioSerializer

# Create your views here;

# List all posts or create a new one
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Retrieve, update, or delete a specific post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# List all projects with filtering, searching, and ordering
class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']  # Allow filtering by 'status'
    search_fields = ['title', 'description']  # Allow searching by these fields
    ordering_fields = ['created_at', 'title']  # Allow ordering by these fields

# List and Create API with filtering, search, and ordering for Portfolio
class PortfolioListCreateAPIView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'status']  # Fields you can filter by
    search_fields = ['title', 'description']  # Fields you can search in
    ordering_fields = ['title', 'created_at']  # Fields you can order by

# Retrieve, Update, Delete API for Portfolio
class PortfolioDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

