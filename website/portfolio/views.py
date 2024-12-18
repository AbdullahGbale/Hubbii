from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here;


# List all posts or create a new one
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# Retrieve, update, or delete a specific post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

