from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def post_list(request):
    posts_list = Post.published_manager.all()
    # Pagination with 3 posts per page
    paginator = Paginator(posts_list, 2)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.get_page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.get_page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, published__year=year,
                             published__month=month, published__day=day,
                             status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
