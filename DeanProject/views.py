from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db import connection
from itertools import chain

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
      context = {"%s_page"%requestedPage: "active", "userGroup": userGroup, "forms": forms, "numPending": numPending, "form_selector": emptyForm(), "currentForm": ""}

      # For newform.html page
      if requestedPage == "newform":
        if request.method == "POST":
            selected_form = request.POST['form-selector']
            if selected_form == '1':
                context['form_selector'] = permitToRegisterForm()
                context['currentForm'] = "/permitToRegister"
            elif selected_form == '2':
                context['form_selector'] = add_dropClassForm()
                context['currentForm'] = "/addDropClass"
            elif selected_form == '3':
                context['form_selector'] = UGGraduationForm()
                context['currentForm'] = "/UGGraduation"
            elif selected_form == '4':
                context['form_selector'] = masterGraduationForm()
                context['currentForm'] = "/masterGraduation"
            elif selected_form == '5':
                context['form_selector'] = degreeAuditForm()
                context['currentForm'] = "/degreeAudit"
            elif selected_form == '6':
                context['form_selector'] = transcriptRequestForm()
                context['currentForm'] = "/transcriptRequest"

      # Process form submissions
      if requestedPage == "permitToRegister":
          return redirect('/success')
      elif requestedPage == "addDropClass":
          return redirect('/success')
      elif requestedPage == "UGGraduation":
          return redirect('/success')
      elif requestedPage == "masterGraduation":
          return redirect('/success')
      elif requestedPage == "degreeAudit":
          return redirect('/success')
      elif requestedPage == "transcriptRequest":
          return redirect('/success')

      return render(request, 'DeanProject/%s.html'%requestedPage, context)
  else:
      return redirect('/login')

# Should return all forms for authenticated user as dictionary or array
def getForms(request):
    #forms = {'all' : range(13), 'pending' : range(3), 'approved' : range(9), 'denied' : range(1)}
    user_id = request.user.profile.tech_id
    
    #cursor = connection.cursor()
    #print(cursor.execute('''SELECT * FROM DeanProject_permittoregister WHERE student_id_number = "%s"''' %user_id))

    permitToRegisterData = permitToRegister.objects.filter(student_id_number=user_id)
    #addDropData = add_dropClass.objects.filter(student_id_number=user_id)
    #ugGraduationData = UGGraduation.objects.filter(student_id_number=user_id)
    #masterGraduationData = masterGraduation.objects.filter(student_id_number=user_id)
    #degreeAuditData = degreeAudit.objects.filter(student_id_number=user_id)
    #transcriptRequestData = transcriptRequest.objects.filter(student_id_number=user_id)

    print(permitToRegisterData)

    forms = {
        'all' : permitToRegisterData,
        'pending' : range(1),
        'approved' : range(1),
        'denied' : range(1)
    }
    
    return forms 

def error(request):
    return render(request, 'DeanProject/error.html')
