from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserCreatorForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','email','phone', 'image','profession', 'relationship']

class Login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)