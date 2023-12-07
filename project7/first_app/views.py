from django.shortcuts import render
from first_app.forms import StudentForm

# Create your views here.
def home(req):
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render (req, 'first_app/home.html', {'form' : form})