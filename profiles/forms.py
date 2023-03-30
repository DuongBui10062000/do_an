from captcha.fields import ReCaptchaField
from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class ResgisterForm(UserCreationForm): # overwrite Form mặc định
	email = forms.EmailField(required=True)
	captcha = ReCaptchaField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'captcha')
		field_classes = {'username' : UsernameField}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username']. widget.attrs.update({'class': 'form-control', })
		self.fields['email']. widget.attrs.update({'class': 'form-control', })
		self.fields['password1']. widget.attrs.update({'class': 'form-control', })
		self.fields['password2']. widget.attrs.update({'class': 'form-control', })


class ProfileEditForm(forms.ModelForm):
	class Meta:#lop con cua models form
		model = User
		fields = ('full_name', 'address', 'year_birth', 'about')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['full_name']. widget.attrs.update({'class': 'form-control', })
		self.fields['address']. widget.attrs.update({'class': 'form-control', })
		self.fields['year_birth']. widget.attrs.update({'class': 'form-control', })
		self.fields['about'].widget.attrs.update({'class': 'form-control', })