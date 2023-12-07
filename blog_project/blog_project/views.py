from django.shortcuts import render
from posts.models import Post

def home (req):
    posts = Post.objects.all()
    return render (req, 'index.html', {'posts': posts})