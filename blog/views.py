from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView
from blog.models import Post

class PostListView(ListView):
  # モデルの継承
  model = Post
  # HTMLを指定
  template_name = 'blog/post_list.html'
  # ---------------　記事を更新日でソートする ---------------------
  
  # querysetはデータベースから取得したデータを格納している
  def get_queryset(self):
    posts = super().get_queryset()
    # 更新日順にする「-」が必要
    return posts.order_by('-updated_at')
  
  # ---------------　記事を更新日でソートする END------------------


class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
  # ---------　ログインユーザーor公開記事のみを表示させる------------

  # クラスベースビューが持っているメソッド querysetはあるとは限らないのでデフォルトでNone
  def get_object(self, queryset=None):
    # 詳細の記事を返す 
    post = super().get_object(queryset)
    # post変数を公開記事 or ログインユーザーだけアクセスさせる
    if post.is_published or self.request.user.is_authenticated:
      return post
    else:
      # 条件に入らない時は404エラーを返す（raiseはエラー発生時に返す）
      raise Http404
    
  # --------　ログインユーザーor公開記事のみを表示させる END --------
    