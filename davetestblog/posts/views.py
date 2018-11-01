from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    # use QuerySet API order_by() to query the Post model entries in database
    posts = Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {
        'posts': posts
    })

# post_id comes from url defined in urls.py
def posts_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    # post = Post.objects.get(pk=post_id)
    # Use this shortcut method would display 404 is the data entry does not exists
    post = get_object_or_404(klass=Post, pk=post_id)
    return render(request, 'posts/posts_detail.html', {
        'post': post
    })
