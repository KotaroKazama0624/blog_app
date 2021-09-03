from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm 
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def usercreatefunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'usercreate.html')
        except IntegrityError:
            return render(request, 'usercreate.html', {'error':'このユーザーはすでに登録されています'})
    return render(request, 'usercreate.html')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:post_list')
        else:
            return render(request, 'login.html', {'context':'ログインできませんでした'})
    return render(request, 'login.html', {'context':'get method'})

def logoutfunc(request):
    logout(request)
    return redirect('blog:login')


class PostListView(generic.ListView):
    template_name = 'post_list.html'
    model = Post

class PostCreateView(generic.CreateView):
    template_name = 'post_form.html'
    #作成したい model を指定
    model = Post
    # 作成した form クラスを指定
    form_class = PostCreateForm
    # 記事作成に成功した時のリダイレクト先を指定
    success_url = reverse_lazy('blog:post_list')

class PostDetailView(generic.DetailView):
    template_name = 'post_detail.html'
    model = Post 

class PostUpdateView(generic.UpdateView):
    template_name = 'post_form.html'
    model = Post
    form_class = PostCreateForm 
    success_url = reverse_lazy('blog:post_detail')

class PostDeleteView(generic.DeleteView):
    template_name = 'post_confirm_delete.html'
    model = Post
    #削除をしてしまうとアクセス対象の記事がなくなってしまうので、詳細画面 (post_detail) にはリダイレクトさせない
    success_url = reverse_lazy('blog:post_list')