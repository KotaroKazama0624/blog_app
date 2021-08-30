from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm 
from .models import Post

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

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