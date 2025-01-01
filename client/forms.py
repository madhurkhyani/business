from django import forms
from .models import ClientData

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientData
        exclude = ["note"]
        widgets = {
            'Name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter Name'}),
            'Company_Name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter Company Name'}),
            'email': forms.TextInput(attrs={'type': 'email', 'placeholder': 'Enter Email'}),
        }