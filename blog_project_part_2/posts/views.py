from django.shortcuts import render, redirect
from posts.forms import addPostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(req):
    if req.method == 'POST':
        form = addPostForm(req.POST)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return redirect('home')
    else:
        form = addPostForm()
    return render(req, 'posts/add_post.html', {'form': form})

@login_required
def edit_post(req, id):
    post = Post.objects.get(pk=id)
    form = addPostForm(instance=post)
    if req.method == 'POST':
        form = addPostForm(req.POST, instance=post)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return redirect('home')
    return render(req, 'posts/edit_post.html', {'form': form})

@login_required
def delete_post(req, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')