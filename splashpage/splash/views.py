from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Prospect
from .forms import ProspectForm, QuickProspectForm
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt

def service(request):
  template = loader.get_template('service-details.html')
  return HttpResponse(template.render())

def prizes(request):
  template = loader.get_template('portfolio-details.html')
  return HttpResponse(template.render())

def index(request):
  if request.method == 'GET':
    quickform = QuickProspectForm(request.GET)
    return render(request, 'index.html', {'quickform': quickform})
  elif request.method == 'POST':
    quickform = QuickProspectForm(request.POST)
    if quickform.is_valid():
      quickform = Prospect(
          name = 'Quick Entry',
          email = quickform.cleaned_data['email'],  
          message = '',
      )
      quickform.save()
      return redirect('index')
    else:
      return redirect('index') #there should be some feedback to users that their form wasnt good

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