from django.shortcuts import render, redirect
from django.views import View
from .forms import AddCaloTodayForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AddCaloToday(LoginRequiredMixin, View):
	def get(self, request):
		initial_data = {
			'user_id': request.user
		}
		f = AddCaloTodayForm(initial=initial_data)
		context = { 'fm': f }
		return render(request, 'followcalo/add_calo_today.html', context)

	def post(self, request):
		f = AddCaloTodayForm(request.POST)
		#if request.user.has_perm('profiles.add_caloeachday'):
		f.save()
		#else:
		#	return HttpResponse('Ban khong co quyen')
		return redirect('nameInforProfile')

