from django.shortcuts import render, redirect
from author.forms import addAuthorForm

# Create your views here.
def add_author(req):
    if req.method == "POST":
        form = addAuthorForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect(add_author)
    else:
        form = addAuthorForm()
    return render(req, 'author/add_author.html', {'form': form})