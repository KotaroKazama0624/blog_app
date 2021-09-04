from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self): # Post モデルが直接呼び出された時に返す値を定義
        return self.title # 記事タイトルを返す

class Comment(models.Model):
    #記事に対するコメント
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象記事')
    date = models.DateTimeField('作成日', default=timezone.now)
 
    def __str__(self):
        return self.text[:20]