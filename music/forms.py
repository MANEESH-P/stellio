from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username', 'email' ,'password',]

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'password']
