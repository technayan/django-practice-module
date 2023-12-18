from django.shortcuts import render, redirect
from posts.forms import AddPostForm, CommentForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.

# Function Based Add Post View
@login_required
def add_post(req):
    if req.method == 'POST':
        form = AddPostForm(req.POST)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(req, 'posts/add_post.html', {'form': form})

# Class Based Add Post View
@method_decorator(login_required, name = 'dispatch')
class AddPostView (CreateView):
    model = Post
    form_class = AddPostForm
    success_url = reverse_lazy('home')
    template_name = 'posts/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# Function Based Edit Post View
@login_required
def edit_post(req, id):
    post = Post.objects.get(pk=id)
    form = AddPostForm(instance=post)
    if req.method == 'POST':
        form = AddPostForm(req.POST, instance=post)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return redirect('home')
    return render(req, 'posts/edit_post.html', {'form': form})


# Class Based Edit Post View
@method_decorator(login_required, name = "dispatch")
class EditPostView(UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Function Based Delete Post View
@login_required
def delete_post(req, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

# Class Based Delete Post View
@method_decorator(login_required, name = 'dispatch')
class DeletePostView (DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    template_name = 'posts/delete_post.html'


# Class Based Details View
class PostDetailsView (DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/post_details.html'

    def post (self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)    
        post = self.get_object()        
        if request.method == 'POST' and comment_form.is_valid():
            new_comment = comment_form.save(commit = False)     
            new_comment.post = post            
            new_comment.save()
            
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        post = self.object                  
        comments = post.comments.all()      
        comment_form = CommentForm()

        context['comments'] = comments                  
        context['comment_form'] = comment_form          

        return context


    
