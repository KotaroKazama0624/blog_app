from django import forms
from .models import Post

# DjangoのModelFormでは強力なValidationを使える
class PostCreateForm(forms.ModelForm):

    class Meta:
        # Post モデルと接続し、Post モデルの内容に応じてformを作ってくれる
        model = Post
        # 入力するカラムを指定
        fields = ('title', 'text') 