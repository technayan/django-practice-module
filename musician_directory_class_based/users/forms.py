from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm (UserCreationForm):
    first_name = forms.TextInput(attrs={'id': 'required'})
    last_name = forms.TextInput(attrs={'id': 'required'})
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']