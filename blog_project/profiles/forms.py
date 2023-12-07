from django import forms
from profiles.models import Profile

class addProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'