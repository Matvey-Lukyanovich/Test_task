from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Shortcut_link



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class LinkForm(ModelForm):
	class Meta:
		model = Shortcut_link
		fields = ['link_info','user_info','link_short']
		widgets = {
			"link_info": TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Введите ссылку...'
			}),
			"link_short": TextInput(attrs={
			'class': 'form-control',
			'type' : "hidden",
			'value': 'Link'
			}),
			"user_info": TextInput(attrs={
			'class': 'form-control',
			'type' : "hidden",
			'value': 'user'
			})
		}