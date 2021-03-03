from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .forms import UGGraduation

#The main dashboard view
def home_view(request):
  if request.user.is_authenticated:
    template = loader.get_template('DeanProject/dashboard.html')
    return HttpResponse(template.render())
  else: 
    return redirect('/login')
