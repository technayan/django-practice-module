from django import forms
from django.core import validators

# class contactForm (forms.Form):                 # Inherite from Form
#     name = forms.CharField(label="Full Name:", initial="Rahim", help_text='Total length 50 chars', required=False)
#     email = forms.EmailField(label="user email")
    # address = forms.CharField(widget= forms.Textarea(attrs= {'id': 'addr', 'class': 'cls-1 cls2 cls-3', 'placeholder': 'Enter Address'}))
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    # check = forms.BooleanField()
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # ADDONS = [('P', 'Pepperoni'), ('C', 'Cheese'), ('MS', 'Mashroom')]
    # addons = forms.MultipleChoiceField(choices=ADDONS, widget=forms.CheckboxSelectMultiple)
    # file = forms.FileField()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('Must more than 10 character')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain .com')


class contactForm (forms.Form):
    name = forms.CharField(label="Full Name:", initial="Rahim", required=False, validators= [validators.MinLengthValidator(10, message="At least 10 chars")])
    email = forms.EmailField(label="Email", validators=[validators.EmailValidator(message='Enter valid email')])
    age = forms.IntegerField(label="Age", validators=[validators.MaxValueValidator(15, message='At most 15 years'), validators.MinValueValidator(10, message='At lease 10 years')])


class PaswordValidationProject (forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valPass = self.cleaned_data['password']
        valConPass = self.cleaned_data['confirmPassword']
        valName = self.cleaned_data['name']

        if valPass != valConPass:
            raise forms.ValidationError('Password doesn\'t match')  
        if len(valName) < 10:
            raise forms.ValidationError('At least 10 characters')  
