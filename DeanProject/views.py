from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .forms import UGGraduation

#The main dashboard view
def home_view(request):
  template = loader.get_template('DeanProject/dashboard.html')
  return HttpResponse(template.render())

def form_view(request):
  form = UGGraduation()
  return render(request, 'DeanProject/forms_page.html', {'form' : form})