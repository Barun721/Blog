from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm



class user_login2(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    captcha = ReCaptchaField()