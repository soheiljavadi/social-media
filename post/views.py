from django.shortcuts import render
from rest_framework import generics
from . models import Blog
from .serializer import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset =Blog .objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer