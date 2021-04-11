from django.shortcuts import render, redirect
from .forms import *
import sqlite3

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
          return processPermitToRegister(request)
      elif requestedPage == "addDropClass":
          return processAddDropClass(request)
      elif requestedPage == "UGGraduation":
          return processUGGraduation(request)
      elif requestedPage == "masterGraduation":
          return processMasterGraduation(request)
      elif requestedPage == "degreeAudit":
          return processDegreeAudit(request)
      elif requestedPage == "transcriptRequest":
          return processTranscriptRequest(request)

      return render(request, 'DeanProject/%s.html'%requestedPage, context)
  else:
      return redirect('/login')

# Should return all forms for authenticated user as dictionary or array
def getForms(request):
    forms = {'all' : range(13), 'pending' : range(3), 'approved' : range(9), 'denied' : range(1)}
    return forms

def processPermitToRegister(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_permittoregister(student_id_number, date, name_enrolled_under, registration_semester, registration_year, comments, total_hours_enrolled, dean_signature, advisor_signature, student_signature)
            VALUES(?,?,?,?,?,?,?,?,?,?)''', (request.POST['student_id_number'], request.POST['date'], request.POST['name_enrolled_under'], request.POST['registration_semester'], request.POST['registration_year'], request.POST['comments'], request.POST['total_hours_enrolled'], request.POST['dean_signature'], request.POST['advisor_signature'], request.POST['student_signature']))
      db.commit()
      db.close()
      return redirect('/error')

def processAddDropClass(request):
      return redirect('/error')

def processUGGraduation(request):
      try:
          if (request.POST['pronunciation_recorded'] == 'on'):
              pronunciation_recorded = True
      except:
          pronunciation_recorded = False
      try:
          if (request.POST['parents_completed_bachelor_degree'] == 'on'):
              parents_completed_bachelor_degree = True
      except:
          parents_completed_bachelor_degree = False
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_uggraduation(student_id_number, date, name_enrolled_under, phone_number, student_signature, diploma_name, name_pronunciation, pronunciation_recorded, parents_completed_bachelor_degree, expected_graduation_term, expected_graduation_year, preferred_degree)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (request.POST['student_id_number'], request.POST['date'], request.POST['name_enrolled_under'], request.POST['phone_number'], request.POST['student_signature'], request.POST['diploma_name'], request.POST['name_pronunciation'], pronunciation_recorded, parents_completed_bachelor_degree, request.POST['expected_graduation_term'], request.POST['expected_graduation_year'], request.POST['preferred_degree']))
      db.commit()
      db.close()
      return redirect('/error')

def processMasterGraduation(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_mastergraduation(student_id_number, date, name_enrolled_under, mailing_address, city, state, zip_code, phone_number, email, student_starting_semester, student_starting_year, diploma_name, name_pronunciation, expected_graduation_term, expected_graduation_year, degree_name)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (request.POST['student_id_number'], request.POST['date'], request.POST['name_enrolled_under'], request.POST['mailing_address'], request.POST['city'], request.POST['state'], request.POST['zip_code'], request.POST['phone_number'], request.POST['email'], request.POST['student_starting_semester'], request.POST['student_starting_year'], request.POST['diploma_name'], request.POST['name_pronunciation'], request.POST['expected_graduation_term'], request.POST['expected_graduation_year'], request.POST['degree_name']))
      db.commit()
      db.close()
      return redirect('/error')

def processDegreeAudit(request):
      try:
          if (request.POST['major_was_chosen'] == 'on'):
              major_was_chosen = True
      except:
          major_was_chosen = False
      try:
          if (request.POST['minor_was_chosen'] == 'on'):
              minor_was_chosen = True
      except:
          minor_was_chosen = False
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_degreeaudit(student_id_number, catalog_year, name_enrolled_under, major_or_minor_name, major_was_chosen, minor_was_chosen, semester, year)
            VALUES(?,?,?,?,?,?,?,?)''', (request.POST['student_id_number'], request.POST['catalog_year'], request.POST['name_enrolled_under'], request.POST['major_or_minor_name'], major_was_chosen, minor_was_chosen, request.POST['semester'], request.POST['year']))
      db.commit()
      db.close()

def processTranscriptRequest(request):
      try:
          if (request.POST['adhe'] == 'on'):
              adhe = True
      except:
          adhe = False
      try:
          if (request.POST['sacm'] == 'on'):
              sacm = True
      except:
          sacm = False
      try:
          if (request.POST['embassy_of_kuwait'] == 'on'):
              embassy_of_kuwait = True
      except:
          embassy_of_kuwait = False
      try:
          if (request.POST['ade_licensure'] == 'on'):
              ade_licensure = True
      except:
          ade_licensure = False
      try:
          if (request.POST['arsbn'] == 'on'):
              arsbn = True
      except:
          arsbn = False

      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_transcriptrequest(student_id_number, date, name_enrolled_under, birth_date, mailing_address, city, state, zip_code, phone_number, student_signature, adhe, sacm, embassy_of_kuwait, ade_licensure, arsbn)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (request.POST['student_id_number'], request.POST['date'], request.POST['name_enrolled_under'], request.POST['birth_date'], request.POST['mailing_address'], request.POST['city'], request.POST['state'], request.POST['zip_code'], request.POST['phone_number'], request.POST['student_signature'], adhe, sacm, embassy_of_kuwait, ade_licensure, arsbn))
      db.commit()
      db.close()
      return redirect('/error')

def error(request):
    return render(request, 'DeanProject/error.html')
