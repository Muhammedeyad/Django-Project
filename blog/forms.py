from django import forms
from .models import MyModel
class ContactForms(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'message']
