from django import forms
from musician.models import Musician

class musicianForm (forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'