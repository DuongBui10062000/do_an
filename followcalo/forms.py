from .models import CaloEachDay
from django import forms

class AddCaloTodayForm(forms.ModelForm):
	class Meta:
		model = CaloEachDay
		fields = '__all__'
		widgets = {'user_id': forms.HiddenInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['user_id']. widget.attrs.update({'class': 'form-control', })
		self.fields['calo_in']. widget.attrs.update({'class': 'form-control', })
		self.fields['calo_out']. widget.attrs.update({'class': 'form-control', })