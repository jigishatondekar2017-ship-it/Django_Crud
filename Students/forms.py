from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['rno', 'name', 'email', 'course', 'fees']
        widgets={
            'rno':forms.NumberInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'fees':forms.NumberInput(attrs={'class':'form-control', 'step': '0.01', 'min': '0'}),
        }

        