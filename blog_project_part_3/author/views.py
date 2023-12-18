from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.

# Function based Create view
def register(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Registered Successfully.')
        else:
            messages.error(req, 'Registration Failed.')

        return redirect('register')
    else:
        form = RegistrationForm()

    return render(req, 'register.html', {'form': form, 'type': 'Register'})


# Function based Login view
def user_login(req):
    if req.method == "POST":
        form = AuthenticationForm(request= req, data = req.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            user = authenticate(username = user_name, password = pass_word)
            if user is not None:
                login(req, user)
                return redirect('home')
            else:
                messages.success(req, 'Incorrect Information.')
                return redirect('register')
            
    else:
        form = AuthenticationForm()
    return render (req, 'register.html', {'form': form, 'type': 'Login'})


# Class based Login view
class UserLoginView (LoginView):
    template_name = 'register.html'

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.info(self.request, 'Invalid information.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def get_success_url (self):
        return reverse_lazy('home')


# Function based Logout view
def user_logout (req):
    logout(req)
    return redirect('login')


# Class based Logout view
class UserLogoutView (LogoutView):
    def get_success_url (self):
        return reverse_lazy('login')


@login_required
def profile (req):
    posts = Post.objects.filter(author = req.user)
    return render (req, 'profile.html', {'posts': posts})


@login_required
def update_profile (req):
    if req.method == "POST":
        form = ChangeUserForm(req.POST, instance = req.user)
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile Updated Successfully.')
        else:
            messages.error(req, 'Profile Update Failed.')
        return redirect('edit_profile')

    else:
        form = ChangeUserForm(instance = req.user)
    return render (req, 'edit_profile.html', {'form': form})


def change_password (req):
    if req.method == 'POST':
        form = PasswordChangeForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            messages.success(req, 'Password changed successfully.')
            return redirect('profile')

    else:
        form = PasswordChangeForm(user = req.user)
    return render (req, 'change_pass.html', {'form': form})



