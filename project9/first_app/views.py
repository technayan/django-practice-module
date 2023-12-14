from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateDataForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(req):
    return render (req, 'first_app/home.html')

def register(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = RegisterForm(req.POST)
            if form.is_valid():
                form.save()
                messages.success(req, 'Registraion Successful.')
        else:
            form = RegisterForm()
        return render (req, 'first_app/register.html', {'form': form})
    else:
        return redirect('profile')

def user_login(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = AuthenticationForm(request = req, data = req.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                pass_word = form.cleaned_data['password']
                user = authenticate(username= user_name, password = pass_word)
                if user is not None:
                    login(req, user)
                    return redirect ('profile')
                
        else:
            form = AuthenticationForm()
        return render (req, 'first_app/login.html', {'form': form})
    else:
        return redirect('profile')
    
def user_logout (req):
    logout(req)
    return redirect('login')
    
def profile (req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = UpdateDataForm(req.POST, instance = req.user)
            if form.is_valid():
                form.save()
                messages.success(req, 'Updated Successfully.')
        else:
            form = UpdateDataForm(instance = req.user)
        return render (req, 'first_app/profile.html', {'form': form, 'user': req.user})
    else:
        return redirect('login')
    

def change_pass (req):      # with old pass
    if req.user.is_authenticated:
        if req.method == "POST":
            form = PasswordChangeForm(user = req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = req.user)
        return render(req, 'first_app/change_pass.html', {'form': form})
    else:
        return redirect('login')
    
def set_pass (req):        # without old pass
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = SetPasswordForm(user = req.user, data = req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user)
                return redirect ('profile')
        else:
            form = SetPasswordForm(user = req.user)
        return render (req, 'first_app/change_pass.html', {'form': form})
    
    else:
        return redirect ('login')
    

def update_data (req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = UpdateDataForm(req.POST, instance = req.user)
            if form.is_valid():
                form.save()
                messages.success(req, 'Updated Successfully.')
        else:
            form = UpdateDataForm(instance = req.user)
        return render (req, 'first_app/register.html', {'form': form})
    else:
        return redirect('login')