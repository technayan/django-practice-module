from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home (req, category_slug = None):
    posts = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        posts = Post.objects.filter(categories = category)
    categories = Category.objects.all()
    return render (req, 'index.html', {'posts': posts, 'categories': categories})