from django.shortcuts import render, redirect
from calculator.models import NameOfFood, ARM
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json
import requests
from django.contrib import messages
from .forms import FormCaloPerDay

# Create your views here.
def tableCalo(request):
	object_list = NameOfFood.objects.all()
	return render(request, 'calculator/tablecalo.html', { 'object_list' : object_list })

def getJson(request):
	data = list(NameOfFood.objects.values())
	return JsonResponse(data, safe=False)


def calculateCalorites(request):
	current_calo = 0
	data = {}

	url = "http://127.0.0.1:8000/Calculator/getjson"
	params = {"q" : "girl"}
	responese = requests.get(url, params)
	if responese.status_code == 200:
		data = json.loads(responese.text)

	if request.method == "POST":
		try:
			food = int(request.POST.get('current_food',''))
			quantity = int(request.POST.get('quantity_g',''))
			for i in data:
				if i['id'] == food:
					current_calo = (quantity / i['unit']) * i['calo']
		except:
			messages.success(request,'You must entering a number into Quanlity field.')
			return redirect('/Calculator/cal/')

	return render(request, 'calculator/cal_calories.html', { 'data' : data, 'current_calo' : current_calo })


def caloCaloPerDay(request):
	form = FormCaloPerDay()
	AMR = 0
	if request.method == "POST":
		if request.POST.get('sex') == 'Female':
			a = int(request.POST.get('age'))
			w = int(request.POST.get('weight'))
			h = int(request.POST.get('height'))
			ei = ARM.objects.get(exertion_intensity=request.POST.get('exertion_intensity'))
			BRM = 655.1 + (9.563 * w) + (1.850 * h) - (4.676 * a)
			AMR = BRM * ei.ARM_factor
		if request.POST.get('sex') == 'Male':
			a = int(request.POST.get('age'))
			w = int(request.POST.get('weight'))
			h = int(request.POST.get('height'))
			ei = ARM.objects.get(exertion_intensity=request.POST.get('exertion_intensity'))
			BRM = 66.47 + (13.75 * w) + (5.003 * h) - (6.755 * a)
			AMR = BRM * ei.ARM_factor

	context = {
		'form': form,
		'AMR': AMR,
		}
	return render(request, 'calculator/calo_per_day.html', context)