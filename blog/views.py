from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'blog/about.html', context=context)