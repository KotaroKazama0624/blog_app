from django.urls import path, include
from .views import PostListView, IndexView, PostCreateView

app_name = 'blog'

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('post_list', PostListView.as_view(), name='post_list'),
   path('post_create', PostCreateView.as_view(), name='post_create'),
]
