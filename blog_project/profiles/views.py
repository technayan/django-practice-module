from django.shortcuts import render, redirect
from profiles.forms import addProfileForm

# Create your views here.
def add_profile(req):
    if req.method == 'POST':
        form = addProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(add_profile)
    else:
        form = addProfileForm()
    return render(req, 'profiles/add_profile.html', {'form': form})