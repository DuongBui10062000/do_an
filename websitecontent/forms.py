from .models import Blogs
from django import forms

class AddBlogsForm(forms.ModelForm):
	class Meta:
		model = Blogs
		fields = '__all__'
		widgets = {'author': forms.HiddenInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name']. widget.attrs.update({'class': 'form-control', })
		self.fields['description']. widget.attrs.update({'class': 'form-control', })
		self.fields['postcontent']. widget.attrs.update({'class': 'form-control', })
		self.fields['topictype']. widget.attrs.update({'class': 'form-control', })
		self.fields['contact']. widget.attrs.update({'class': 'form-control', })
		self.fields['picture']. widget.attrs.update({'class': 'form-control', })