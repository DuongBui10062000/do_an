from django import forms
from django.forms import ModelForm
from .models import ARM


SEX = (
	('Female', 'Female'),
	('Male', 'Male'),
	)

class FormNameOfFood(forms.Form):
	name_food = forms.CharField(max_length=100)
	unit = forms.IntegerField()
	calo = forms.IntegerField()
	quantity = forms.IntegerField()

class FormCaloPerDay(forms.ModelForm):
	sex = forms.RadioSelect
	age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	class Meta:
		model = ARM
		fields = ['exertion_intensity',]
		widgets = {
            'exertion_intensity': forms.Select(attrs={'class': 'form-select'}),
        }
	


