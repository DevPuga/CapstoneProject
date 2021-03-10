from django.shortcuts import render, redirect
from .forms import UGGraduation

#The main dashboard view
def dashboard(request):
  if request.user.is_authenticated:
      # Checks the group the authenticated user is in
      # if request.user.groups.filter(name="Faculty").exists():
      #     template = loader.get_template('DeanProject/dash-faculty.html')
      # elif request.user.groups.filter(name="Student").exists():
      #     template = loader.get_template('DeanProject/dash-student.html')
      # else:
      #     template = loader.get_template('DeanProject/error.html')
      context = {"dashboard_page": "active"}
      return render(request, 'DeanProject/dashboard.html', context)
  else:
      return redirect('/login')

def pending(request):
    context = {"pending_page": "active"}
    return render(request, 'DeanProject/pending.html', context)

def approved(request):
    context = {"approved_page": "active"}
    return render(request, 'DeanProject/approved.html', context)

def denied(request):
    context = {"denied_page": "active"}
    return render(request, 'DeanProject/denied.html', context)
