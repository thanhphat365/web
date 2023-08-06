from django import forms
from django.contrib.auth.models import User

# class RegistrationForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields=['username', 'password', 'email']
#         widgets ={
#             'password':forms.PasswordInput(),

#         }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    