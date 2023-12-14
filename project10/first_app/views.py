from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def register (req):
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = RegistrationForm()
    return render (req, 'register.html', {'form': form, 'title': 'Register', 'type': 'Register'})

def user_login (req):
    if req.method == 'POST':
        form = AuthenticationForm(request=req, data = req.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            user = authenticate(username = user_name, password = pass_word)
            if user is not None:
                login(req, user)
                messages.success(req, 'Logged In Successfully.')
                return redirect('profile')
        
    else:
        form = AuthenticationForm()
    return render (req, 'register.html', {'form': form, 'title':'Login', 'type': 'Login'})

@login_required
def profile (req):
    return render(req, 'profile.html')

@login_required
def user_logout (req):
    logout(req)
    messages.success(req, 'Logged Out Successfully.')
    return redirect ('home')

@login_required
def change_password(req):
    if req.method == "POST":
        form = PasswordChangeForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect ('profile')
    else:
        form = PasswordChangeForm(user = req.user)
    return render (req, 'register.html', {'form': form, 'title': 'Change Password with Old Password', 'type': 'Update'})
        
@login_required
def set_password (req):
    if req.method == "POST":
        form = SetPasswordForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user = req.user)
    return render(req, 'register.html', {'form': form, 'title': 'Change Password without Old Password', 'type': 'Update'})