from django.shortcuts import render, redirect
from musician.forms import musicianForm
from musician.models import Musician

# Create your views here.
def add_musician(req):
    if req.method == "POST":
        form = musicianForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = musicianForm()
    return render(req, 'musician/add_musician.html', {'form': form})


def edit_musician(req, id):
    musician = Musician.objects.get(pk = id)
    form = musicianForm(instance=musician)
    if req.method == "POST":
        form = musicianForm(req.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'musician/edit_musician.html', {'form': form})


def delete_musician(req, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')