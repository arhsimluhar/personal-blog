from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.published_manager.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, published__year=year,
                             published__month=month, published__day=day,
                             status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
