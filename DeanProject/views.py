from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .forms import UGGraduation

#The main dashboard view
def home_view(request):
  if request.user.is_authenticated:
      if request.user.groups.filter(name="Faculty").exists():
          template = loader.get_template('DeanProject/dash-faculty.html')
      elif request.user.groups.filter(name="Student").exists():
          template = loader.get_template('DeanProject/dash-student.html')
      else:
          template = loader.get_template('DeanProject/error.html')
      return HttpResponse(template.render())
  else:
      return redirect('/login')
