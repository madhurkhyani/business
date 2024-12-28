from django import forms
from .models import Cash_in,Cash_out,Sales

class Cash_in_form(forms.ModelForm):
    class Meta:
        model=Cash_in
        fields = ['amount','description']

class Cash_out_form(forms.ModelForm):
    class Meta:
        model=Cash_out
        fields = ['amount','description']

class Sales_form(forms.ModelForm):
    class Meta:
        model=Sales
        fields = ['amount','description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assign ids to the fields
        self.fields['amount'].widget.attrs.update({'id': 'amount'})
        self.fields['description'].widget.attrs.update({'id': 'description'})