from django import forms
from posts.models import Post

class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'