from django import forms
from models import SignUpModel, ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'pin', 'phno', 'query', 'device']


#
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = ['name', 'email', 'username', 'password']


#
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    fields = ['username', 'password']


