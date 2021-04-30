from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'all_posts': posts,
    }
    return render(request, 'index.html', context)

def uploadPost(request):
    if request.method == "POST":
        Post.objects.create(desc=request.POST['post'])
        context = {
            'all_posts': Post.objects.all(),
        }
        return render(request, 'posts_index.html', context)