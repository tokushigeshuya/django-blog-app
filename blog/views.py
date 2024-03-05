from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView,DetailView
from blog.models import Post,Category,Tag

class PostListView(ListView):
  # モデルの継承
  model = Post
  # HTMLを指定
  template_name = 'blog/post_list.html'
  context_object_name = "posts"
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
    
class CategoryPostListView(ListView):
  # カテゴリで検索しても表示するのはブログ記事なので使用するモデルはPOST
  model = Post
  template_name = "blog/post_list.html"
  # オブジェクトリストのpost_listとなっていた、HTMLで取り出す値の名前を変更する。（html側でobject_listではなくpostsでforからの取り出しが可能）
  context_object_name = "posts"

  def get_queryset(self):
    # print("=" * 30)
    # クラスで使用しているselfは自分自身という意味（このクラス自体）
    # print(vars(self))
    # {'slug': 'django'}この形がself.kwargs。これのkeyをself.kwargs['slug']で入れてる
    # print(self.kwargs)

    # トップページでアクセスのあったカテゴリーのURLをキーワードwargsから取得して変数に入れる
    slug = self.kwargs['slug']
    # 存在しないカテゴリーの場合は404エラーを発生させる ※カテゴリーが存在した場合はself.categoryに格納
    self.category = get_object_or_404(Category, slug=slug)
    return super().get_queryset().filter(category=self.category)
  # 任意の値を渡してあげる
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["category"] = self.category
    # print(context)
    return context
  
class TagPostListView(ListView):
  model = Post
  template_name = "blog/post_list.html"
  context_object_name = "posts"
  # タグの存在チェックと絞り込み
  def get_queryset(self):
    slug = self.kwargs['slug']
    self.tag = get_object_or_404(Tag, slug=slug)
    return super().get_queryset().filter(tag=self.tag)
  # タグをqueryに追加してオブジェクトを使用可能にする
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tag'] = self.tag
    return context
  