from django.shortcuts import render, redirect
from .forms import *
# from .forms import permitToRegisterForm, add_dropClassForm, UGGraduationForm, masterGraduationForm, degreeAuditForm, transcriptRequestForm, courseInfoForm

#Used in navbar to check if user is faculty
userGroup = ''

def checkIf(group, request):
    if request.user.groups.filter(name="%s"%group).exists():
        global userGroup
        userGroup = group
        return True
    else:
        return False

def get(request):
  checkIf("Faculty", request)
  checkIf("Student", request)
  requestedPage = (request.path).strip("/")
  if request.user.is_authenticated:
      if requestedPage == "":
          requestedPage = "dashboard"

      # Only allow faculty to access faculty page
      if requestedPage == "faculty":
          if checkIf("Faculty", request):
              pass
          else:
              return redirect('/error')
      
      # Get user's forms so we can populate them as cards
      forms = getForms(request)
      numPending = max(forms["pending"]) + 1

      # Set tab as active, render faculty tab if faculty, give forms to html
      context = {"%s_page"%requestedPage: "active", "userGroup": userGroup, "forms": forms, "numPending": numPending}
      
      #For newform.html page
      if requestedPage == "newform":
        if request.method == "POST":
            selected_form = request.POST['form-selector']
            if selected_form == '1':
                context['form_selector'] = permitToRegisterForm()
            elif selected_form == '2':
                context['form_selector'] = add_dropClassForm()
            elif selected_form == '3':
                context['form_selector'] = UGGraduationForm()
            elif selected_form == '4':
                context['form_selector'] = masterGraduationForm()
            elif selected_form == '5':
                context['form_selector'] = degreeAuditForm()
            elif selected_form == '6':
                context['form_selector'] = transcriptRequestForm()
      return render(request, 'DeanProject/%s.html'%requestedPage, context)
  else:
      return redirect('/login')

# Should return all forms for authenticated user as dictionary or array
def getForms(request):
    forms = {'all' : range(13), 'pending' : range(3), 'approved' : range(9), 'denied' : range(1)}
    return forms

def error(request):
    return render(request, 'DeanProject/error.html')
