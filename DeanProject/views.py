from django.http import HttpResponse
import datetime

#The main dashboard view
def home_view(request):
  now = datetime.datetime.now()
  html = "<html><body>It is now %s.</body></html>" % now
  return HttpResponse(html)