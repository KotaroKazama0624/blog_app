from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('usercreate/', views.usercreatefunc, name='usercreate'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    #path('<int:pk>', views.postcommentfunc, name='post_comment'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), 
    path('post_update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'), 
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'), 
    path('comment/create/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
]
