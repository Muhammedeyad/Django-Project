from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Message', required=True)
