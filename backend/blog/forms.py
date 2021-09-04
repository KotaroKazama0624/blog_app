from django import forms
from .models import Post, Comment

# DjangoのModelFormでは強力なValidationを使える
class PostCreateForm(forms.ModelForm):

    class Meta:
        # Post モデルと接続し、Postモデルの内容に応じてformを作ってくれる
        model = Post
        # 入力するカラムを指定
        fields = ('title', 'text')

class CommentCreateForm(forms.ModelForm):
    #コメントフォーム
    class Meta:
        model = Comment
        exclude = ('target', 'date')
