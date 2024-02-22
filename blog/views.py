from django.shortcuts import render
from django.views.generic import ListView,DetailView
from blog.models import Post

class PostListView(ListView):
  # モデルの継承
  model = Post
  # HTMLを指定
  template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
