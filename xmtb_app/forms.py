from django import forms
from django.forms import Textarea, TextInput, CharField, Form



class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
