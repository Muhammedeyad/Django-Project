from django import forms
from .models import MyModel
class ContactForms(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'message']
        labels ={
            'name': "Name",
            'email': "Email",
            'message': 'Message'
        }

    # name = forms.CharField(label='Name', required=True)
    # email = forms.EmailField(label='Email', required=True)
   
