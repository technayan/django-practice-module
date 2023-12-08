from django.shortcuts import render, redirect
from album.forms import albumForm
from album.models import Album

# Create your views here.
def add_album (req):
    if req.method == "POST":
        form = albumForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = albumForm()
    return render (req, 'album/add_album.html', {'form': form})


def edit_album (req, id):
    album = Album.objects.get(pk= id)
    form = albumForm(instance=album)
    if req.method == "POST":
        form = albumForm(req.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (req, 'album/edit_album.html', {'form': form})