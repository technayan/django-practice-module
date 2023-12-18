from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
class RegistrationView (CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context


class UserLoginView (LoginView):
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')
    

class ProfileView(ListView):
    model = User
    pk_url_kwarg = 'username'
    template_name = 'profile.html'
