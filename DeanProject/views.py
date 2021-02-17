from django.http import HttpResponse
from django.template import loader

#The main dashboard view
def home_view(request):
  template = loader.get_template('DeanProject/index.html')
  return HttpResponse(template.render())