from django.shortcuts import render, redirect
from categories.forms import addCategoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_category(req):
    if req.method == 'POST':
        form = addCategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(add_category)
    else:
        form = addCategoryForm()
    return render (req, 'categories/add_category.html', {'form': form})