from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/uploads/', null = True, blank = True)

    def __str__(self):
        return self.title
    

class Comment (models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self):
        return f"Comment by {self.name}"