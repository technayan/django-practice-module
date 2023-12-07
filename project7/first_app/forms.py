from django import forms
from first_app.models import StudentModel

class StudentForm (forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'      # fields = ['name', 'roll'] to choose selected fields
        # exclude = 'father_name'   # except the fields
        labels = {
            'roll': 'Student\'s Roll:',
            'name': 'Student\'s Name:',
            'father_name': 'Student\'s Father\'s Name:',
            'address': 'Address: ',
        }
        widgets = {
            'roll': forms.NumberInput(),
            'name': forms.TextInput(attrs={'class': 'text-success'}),
            'father_name': forms.TextInput(),
            'address': forms.Textarea(),
        }
        error_message = {
            'name': {'required', 'Name is required'},
            'father_name': {'required', 'Father name is required'},
            'address': {'required', 'Address is required'},
        }
    
