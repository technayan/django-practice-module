from django.shortcuts import render
from album.models import Album

def home (req):
    data = Album.objects.all()
    return render (req, 'index.html', {'data': data})