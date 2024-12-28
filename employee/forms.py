from django import forms
from .models import employee_data

class EmployeeDataForm(forms.ModelForm):
    class Meta:
        model = employee_data
        fields = ['Name', 'image', 'Salary', 'Joining_Date']
        widgets = {
            'Name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter Name'}),
            'Joining_Date': forms.DateInput(attrs={'type': 'date'}),
        }
