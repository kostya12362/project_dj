import os
import random
import string

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.conf import settings
from .models import *
from django.http import HttpResponse, JsonResponse


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('main')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

def main(request):
	days = Day.objects.filter(group=request.user.group)
	data = []
	for day in days:
		day_data = {"day": day.date}
		pars = []
		for i in range(1,6):
			para = getattr(day, 'para{}'.format(i))
			if para:
				pars.append({"name": para.name, "teacher": para.teacher, "room": para.room})
		day_data['pars'] = pars
		data.append(day_data)
	return render(request, "main.html", {})
	#return JsonResponse({"data": data})

