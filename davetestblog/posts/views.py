from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # use QuerySet API order_by() to query the Post model entries in database
    posts = Post.objects.order_by('pub_date')

    return render(request, 'posts/home.html', {
        'posts': posts
    })
