from django.urls import path, include
from django.urls import path
from .views import PostList, PostDetail






app_name='post'

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
