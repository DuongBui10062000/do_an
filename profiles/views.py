from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, FormView, View
from django.views.generic.edit import UpdateView
#from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .forms import ResgisterForm, ProfileEditForm
from django.contrib.auth import get_user_model
from followcalo.models import CaloEachDay
from .models import User

User = get_user_model()

class SiteLoginView(LoginView):
	template_name = 'profiles/memberlogin.html'


class SiteRegisterView(FormView):
	template_name = 'profiles/memberegister.html'
	form_class = ResgisterForm

	def form_valid(self, form):
		data = form.cleaned_data
		new_user = User.objects.create_user(username=data['username'],
											password=data['password1'],
											email=data['email'])
#		from pprint import pprint; pprint(data)#check infor ten cmd
		url =f"{reverse('register_ok')}?username={new_user.username}"
		from pprint import pprint; pprint(url)
		return redirect(url)


class SiteResgisterOkView(TemplateView):
	template_name = 'profiles/register_ok.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['username'] = self.request.GET.get('username')
		return context


class SiteLogoutView(LogoutView):
	template_name = 'profiles/memberlogout.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
	template_name = 'profiles/updateprofile.html'
	model = User
	form_class = ProfileEditForm
	success_url = reverse_lazy('nameInforProfile')

	def get_object(self, queryset=None):
		return self.request.user


class ProfilesContent(LoginRequiredMixin, View):
	def get(self, request):
		caloin = []
		caloout = []
		datetime = []
		get_current_user = User.objects.get(pk=request.user.id)
		data_filter = get_current_user.caloeachday_set.all().values()

		for i in data_filter:
			caloin.append(i.get('calo_in'))
			caloout.append(i.get('calo_out'))
			datetime.append(str(i.get('date_time_save')))

		context = {
			'caloin': caloin,
			'caloout': caloout,
			'datetime': datetime,
			}
		return render(request, 'profiles/profile.html', context)