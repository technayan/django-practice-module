from django import forms
from album.models import Album
import datetime

class albumForm (forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'