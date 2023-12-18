from django import forms
from posts.models import Post
from .models import Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'body': 'Comment'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5})
        }