from django.shortcuts import render
from first_app.forms import myForm

# Create your views here.
def home(req):
    form = myForm()
    return render (req, 'first_app/home.html', {'form': form})