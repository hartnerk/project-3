from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Prospect
from .forms import ProspectForm
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt

def service(request):
  template = loader.get_template('service-details.html')
  return HttpResponse(template.render())

def prizes(request):
  template = loader.get_template('portfolio-details.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def signup(request):
  if request.method == 'GET':
    prospectform = ProspectForm(request.GET)
    return render(request, 'signup.html', {'prospectform': prospectform})
  elif request.method == 'POST':
    prospectform = ProspectForm(request.POST)
    if prospectform.is_valid():
      prospectform = Prospect(
          name = prospectform.cleaned_data['name'],
          email = prospectform.cleaned_data['email'],  
          message = prospectform.cleaned_data['message']
      )
      prospectform.save()
    else:
      prospectform = ProspectForm()
    return render(request, 'index.html', {'prospectform': prospectform})