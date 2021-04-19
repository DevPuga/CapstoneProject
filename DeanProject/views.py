from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db import connection
from itertools import chain
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
      #numPending = max(forms["pending"]) + 1

      # Set tab as active, render faculty tab if faculty, give forms to html
      context = {"%s_page"%requestedPage: "active", "userGroup": userGroup, "forms": forms,
      #"numPending": numPending,
      "form_selector": emptyForm(), "currentForm": ""}

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
    #forms = {'all' : range(13), 'pending' : range(3), 'approved' : range(9), 'denied' : range(1)}
    user_id = request.user.profile.tech_id

    permitToRegisterData = permitToRegister.objects.filter(student_id_number=user_id)
    addDropClassData = add_dropClass.objects.filter(student_id_number=user_id)
    ugGraduationData = UGGraduation.objects.filter(student_id_number=user_id)
    masterGraduationData = masterGraduation.objects.filter(student_id_number=user_id)
    degreeAuditData = degreeAudit.objects.filter(student_id_number=user_id)
    transcriptRequestData = transcriptRequest.objects.filter(student_id_number=user_id)

    results = list(chain(permitToRegisterData, addDropClassData, ugGraduationData, masterGraduationData, degreeAuditData, transcriptRequestData))

    pending = []
    approved = []
    denied = []

    for form in results:
        if form.isPending:
            pending.append(form)
        elif form.isApproved:
            approved.append(form)
        elif form.isDenied:
            denied.append(form)

    forms = {
        'all' : results,
        'pending' : pending,
        'approved' : approved,
        'denied' : denied
    }

    return forms

def processPermitToRegister(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_permittoregister(
          student_id_number,
          date,
          name_enrolled_under,
          registration_semester,
          registration_year,
          comments,
          total_hours_enrolled,
          dean_signature,
          advisor_signature,
          student_signature,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['registration_semester'],
          request.POST['registration_year'],
          request.POST['comments'],
          request.POST['total_hours_enrolled'],
          request.POST['dean_signature'],
          request.POST['advisor_signature'],
          request.POST['student_signature'],
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def processAddDropClass(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_add_dropclass(
          student_id_number,
          date,
          name_enrolled_under,
          recieves_financial_aid,
          financial_aid_representative_signature,
          total_hours_enrolled_after_change,
          comments,
          advisor_signature,
          student_signature,
          atu_comments,
          another_course_fits_schedule,
          changing_major,
          changing_minor,
          classes_too_large,
          could_not_understand_the_instructor_course_or_materials,
          course_not_required_for_major,
          inadequate_academic_support_services,
          insufficient_high_school_preparation,
          lack_of_academic_challenge,
          lack_of_progress_in_the_courses,
          need_to_re_enroll_in_classes_next_semester,
          need_to_re_enroll_in_classes_with_different_instructor,
          quality_of_instruction_did_not_meet_expections,
          reduce_course_load,
          wanted_classes_face_to_face,
          wanted_classes_online,
          change_in_family_financial_circumstances,
          didnt_have_enough_money_to_continue,
          financial_aid_was_not_sufficient,
          increases_in_tuition_and_fees,
          incurred_too_much_debt,
          needed_Course_for_financial_aid_eligibility,
          scholarship_Grant_was_not_renewed,
          family_illness_responsibility,
          homesick,
          wanted_to_be_closer_to_family_and_friends,
          commute_too_long, moved_out_of_the_area,
          distracted_Social_life, felt_class_climate_unwelcoming,
          felt_out_of_place_in_class,
          impact_of_natural_disaster,
          inadequate_study_skills_or_lack_of_academic_success,
          military_obligations,
          personal_health,
          personal_emergency,
          unmotivated_for_this_courses_or_tired_of_school,
          working_too_many_hours,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          trySetBool(request, 'recieves_financial_aid'),
          request.POST['financial_aid_representative_signature'],
          request.POST['total_hours_enrolled_after_change'],
          request.POST['comments'],
          request.POST['advisor_signature'],
          request.POST['student_signature'],
          request.POST['atu_comments'],
          trySetBool(request, 'another_course_fits_schedule'),
          trySetBool(request, 'changing_major'),
          trySetBool(request, 'changing_minor'),
          trySetBool(request, 'classes_too_large'),
          trySetBool(request, 'could_not_understand_the_instructor_course_or_materials'),
          trySetBool(request, 'course_not_required_for_major'),
          trySetBool(request, 'inadequate_academic_support_services'),
          trySetBool(request, 'insufficient_high_school_preparation'),
          trySetBool(request, 'lack_of_academic_challenge'),
          trySetBool(request, 'lack_of_progress_in_the_courses'),
          trySetBool(request, 'need_to_re_enroll_in_classes_next_semester'),
          trySetBool(request, 'need_to_re_enroll_in_classes_with_different_instructor'),
          trySetBool(request, 'quality_of_instruction_did_not_meet_expections'),
          trySetBool(request, 'reduce_course_load'),
          trySetBool(request, 'wanted_classes_face_to_face'),
          trySetBool(request, 'wanted_classes_online'),
          trySetBool(request, 'change_in_family_financial_circumstances'),
          trySetBool(request, 'didnt_have_enough_money_to_continue'),
          trySetBool(request, 'financial_aid_was_not_sufficient'),
          trySetBool(request, 'increases_in_tuition_and_fees'),
          trySetBool(request, 'incurred_too_much_debt'),
          trySetBool(request, 'needed_Course_for_financial_aid_eligibility'),
          trySetBool(request, 'scholarship_Grant_was_not_renewed'),
          trySetBool(request, 'family_illness_responsibility'),
          trySetBool(request, 'homesick'),
          trySetBool(request, 'wanted_to_be_closer_to_family_and_friends'),
          trySetBool(request, 'commute_too_long'),
          trySetBool(request, 'moved_out_of_the_area'),
          trySetBool(request, 'distracted_Social_life'),
          trySetBool(request, 'felt_class_climate_unwelcoming'),
          trySetBool(request, 'felt_out_of_place_in_class'),
          trySetBool(request, 'impact_of_natural_disaster'),
          trySetBool(request, 'inadequate_study_skills_or_lack_of_academic_success'),
          trySetBool(request, 'military_obligations'),
          trySetBool(request, 'personal_health'),
          trySetBool(request, 'personal_emergency'),
          trySetBool(request, 'unmotivated_for_this_courses_or_tired_of_school'),
          trySetBool(request, 'working_too_many_hours'),
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def processUGGraduation(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_uggraduation(
          student_id_number,
          date,
          name_enrolled_under,
          phone_number,
          student_signature,
          diploma_name,
          name_pronunciation,
          pronunciation_recorded,
          parents_completed_bachelor_degree,
          expected_graduation_term,
          expected_graduation_year,
          preferred_degree,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['phone_number'],
          request.POST['student_signature'],
          request.POST['diploma_name'],
          request.POST['name_pronunciation'],
          trySetBool(request,'pronunciation_recorded'),
          trySetBool(request, 'parents_completed_bachelor_degree'),
          request.POST['expected_graduation_term'],
          request.POST['expected_graduation_year'],
          request.POST['preferred_degree'],
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def processMasterGraduation(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_mastergraduation(
          student_id_number,
          date,
          name_enrolled_under,
          mailing_address,
          city,
          state,
          zip_code,
          phone_number,
          email,
          student_starting_semester,
          student_starting_year,
          diploma_name,
          name_pronunciation,
          expected_graduation_term,
          expected_graduation_year,
          degree_name,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['mailing_address'],
          request.POST['city'],
          request.POST['state'],
          request.POST['zip_code'],
          request.POST['phone_number'],
          request.POST['email'],
          request.POST['student_starting_semester'],
          request.POST['student_starting_year'],
          request.POST['diploma_name'],
          request.POST['name_pronunciation'],
          request.POST['expected_graduation_term'],
          request.POST['expected_graduation_year'],
          request.POST['degree_name'],
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def processDegreeAudit(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_degreeaudit(
          student_id_number,
          catalog_year,
          name_enrolled_under,
          major_or_minor_name,
          major_was_chosen,
          minor_was_chosen,
          semester,
          year,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['catalog_year'],
          request.POST['name_enrolled_under'],
          request.POST['major_or_minor_name'],
          trySetBool(request, 'major_was_chosen'),
          trySetBool(request, 'minor_was_chosen'),
          request.POST['semester'],
          request.POST['year'],
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def processTranscriptRequest(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_transcriptrequest(
          student_id_number,
          date,
          name_enrolled_under,
          birth_date,
          mailing_address,
          city,
          state,
          zip_code,
          phone_number,
          student_signature,
          adhe,
          sacm,
          embassy_of_kuwait,
          ade_licensure,
          arsbn,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['birth_date'],
          request.POST['mailing_address'],
          request.POST['city'],
          request.POST['state'],
          request.POST['zip_code'],
          request.POST['phone_number'],
          request.POST['student_signature'],
          trySetBool(request, 'adhe'),
          trySetBool(request, 'sacm'),
          trySetBool(request, 'embassy_of_kuwait'),
          trySetBool(request, 'ade_licensure'),
          trySetBool(request, 'arsbn'),
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def trySetBool(request, title):
      try:
          if (request.POST[title] == 'on'):
              result = True
              return result
      except:
          result = False
          return result

def error(request):
    return render(request, 'DeanProject/error.html')
