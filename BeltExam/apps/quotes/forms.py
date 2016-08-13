from django import forms
from datetime import datetime
from .models import User

class RegisterForm(forms.ModelForm):
	password_confirm = forms.CharField(widget=forms.PasswordInput())


	class Meta:
		model=User
		fields=('name', 'alias', 'email', 'password', 'password_confirm')
		widgets={
			'password' : forms.PasswordInput
		}

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)



