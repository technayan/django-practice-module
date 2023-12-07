from django import forms
import datetime

class myForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    email = forms.EmailField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years= BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField(required=False)
    message = forms.CharField(max_length=10, label="Enter your message")
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial= datetime.date.today)
    FAVORITE_COLOR_CHOICES = [('blue', 'Blue'), ('green', 'Green'), ('red', 'Red')]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLOR_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLOR_CHOICES)
    favorite_color3 = forms.MultipleChoiceField(choices=FAVORITE_COLOR_CHOICES)
    favorite_color4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLOR_CHOICES)
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll")
    password = forms.CharField(widget=forms.PasswordInput())