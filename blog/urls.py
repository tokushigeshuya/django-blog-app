from django.contrib import admin
from django.urls import path
from blog.views import PostListView

# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

urlpatterns = [
    path('', PostListView.as_view(), name='post-list')
]
