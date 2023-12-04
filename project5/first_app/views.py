from django.shortcuts import render
from . forms import contactForm, PaswordValidationProject

# Create your views here.
def Home(req):
    return render (req, "first_app/home.html")

def About(req):
    print(req.POST)
    if req.method == 'POST':
        name = req.POST.get('user-name')
        email = req.POST.get('user-email')
        rating = req.POST.get('rating')
        return render (req, "first_app/about.html", {'name': name, 'email': email, 'rating': rating})
    return render (req, "first_app/about.html")

def Form(req):
    return render (req, "first_app/form.html")

def Django_form(req):
    if req.method == 'POST':
        form = contactForm(req.POST, req.FILES)        # req.POST for storing the value
        if form.is_valid():                 # Is the form values are valid
            # file = form.cleaned_data['file']    # store the file
            # with open ('first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)        # cleaned_data to extract the data only not html
        return render (req, "first_app/django_form.html", {'form': form})
    else:
        form = contactForm()    # blank form
        return render (req, 'first_app/django_form.html', {'form': form})
    

def PasswordValidationProject(req):
    if req.method == "POST":
        form = PaswordValidationProject(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PaswordValidationProject()
    return render(req, 'first_app/password_validation.html', {'form': form})