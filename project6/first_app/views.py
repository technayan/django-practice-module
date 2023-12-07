from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(req):
    students = models.Student.objects.all()     # Return an array of dictionaries(object)

    return render (req, 'first_app/home.html', {"data": students})


def delete(req, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect('home')