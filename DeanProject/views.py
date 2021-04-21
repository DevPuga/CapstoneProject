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
            elif selected_form == '7':
                context['form_selector'] = degreeAuditAmendmentRequestForm()
                context['currentForm'] = "/degreeAuditAmendmentRequest"

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
      elif requestedPage == "degreeAuditAmendmentRequest":
          return processDegreeAuditAmendmentRequest(request)

      return render(request, 'DeanProject/%s.html'%requestedPage, context)
  else:
      return redirect('/login')

# Should return all forms for authenticated user as dictionary or array
def getForms(request):
    #forms = {'all' : range(13), 'pending' : range(3), 'approved' : range(9), 'denied' : range(1)}

    results = ""

    pending = []
    approved = []
    denied = []

    if request.user.groups.filter(name="Student").exists():
        user_id = request.user.profile.tech_id

        permitToRegisterData = permitToRegister.objects.filter(student_id_number=user_id)
        addDropClassData = add_dropClass.objects.filter(student_id_number=user_id)
        ugGraduationData = UGGraduation.objects.filter(student_id_number=user_id)
        masterGraduationData = masterGraduation.objects.filter(student_id_number=user_id)
        degreeAuditData = degreeAudit.objects.filter(student_id_number=user_id)
        transcriptRequestData = transcriptRequest.objects.filter(student_id_number=user_id)
        degreeAuditAmendmentRequestData = degreeAuditAmendmentRequest.objects.filter(student_id_number=user_id)

        results = list(chain(permitToRegisterData, addDropClassData, ugGraduationData, masterGraduationData, degreeAuditData, transcriptRequestData, degreeAuditAmendmentRequestData))

        for form in results:
            if form.isPending:
                pending.append(form)
            elif form.isApproved:
                approved.append(form)
            elif form.isDenied:
                denied.append(form)

    elif request.user.groups.filter(name="Faculty").exists():
        user_ids = request.user.profile.advisees["advisees"]
        user_ids.append(request.user.profile.tech_id)

        for id in user_ids:
            permitToRegisterData = permitToRegister.objects.filter(student_id_number=id)
            addDropClassData = add_dropClass.objects.filter(student_id_number=id)
            ugGraduationData = UGGraduation.objects.filter(student_id_number=id)
            masterGraduationData = masterGraduation.objects.filter(student_id_number=id)
            degreeAuditData = degreeAudit.objects.filter(student_id_number=id)
            transcriptRequestData = transcriptRequest.objects.filter(student_id_number=id)
            degreeAuditAmendmentRequestData = degreeAuditAmendmentRequest.objects.filter(student_id_number=id)
            results = list(chain(permitToRegisterData, addDropClassData, ugGraduationData, masterGraduationData, degreeAuditData, transcriptRequestData, degreeAuditAmendmentRequestData))

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
          crn0,
          crn1,
          crn2,
          crn3,
          crn4,
          crn5,
          crn6,
          crn7,
          crn8,
          prefix0,
          prefix1,
          prefix2,
          prefix3,
          prefix4,
          prefix5,
          prefix6,
          prefix7,
          prefix8,
          courseNum0,
          courseNum1,
          courseNum2,
          courseNum3,
          courseNum4,
          courseNum5,
          courseNum6,
          courseNum7,
          courseNum8,
          secNo0,
          secNo1,
          secNo2,
          secNo3,
          secNo4,
          secNo5,
          secNo6,
          secNo7,
          secNo8,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['registration_semester'],
          request.POST['registration_year'],
          request.POST['comments'],
          request.POST['total_hours_enrolled'],
          request.POST['crn0'],
          request.POST['crn1'],
          request.POST['crn2'],
          request.POST['crn3'],
          request.POST['crn4'],
          request.POST['crn5'],
          request.POST['crn6'],
          request.POST['crn7'],
          request.POST['crn8'],
          request.POST['prefix0'],
          request.POST['prefix1'],
          request.POST['prefix2'],
          request.POST['prefix3'],
          request.POST['prefix4'],
          request.POST['prefix5'],
          request.POST['prefix6'],
          request.POST['prefix7'],
          request.POST['prefix8'],
          request.POST['courseNum0'],
          request.POST['courseNum1'],
          request.POST['courseNum2'],
          request.POST['courseNum3'],
          request.POST['courseNum4'],
          request.POST['courseNum5'],
          request.POST['courseNum6'],
          request.POST['courseNum7'],
          request.POST['courseNum8'],
          request.POST['secNo0'],
          request.POST['secNo1'],
          request.POST['secNo2'],
          request.POST['secNo3'],
          request.POST['secNo4'],
          request.POST['secNo5'],
          request.POST['secNo6'],
          request.POST['secNo7'],
          request.POST['secNo8'],
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
          total_hours_enrolled_after_change,
          comments,
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
          dropCRN0,
          dropCRN1,
          dropCRN2,
          dropCRN3,
          dropCRN4,
          dropCRN5,
          addCRN0,
          addCRN1,
          addCRN2,
          addCRN3,
          addCRN4,
          addCRN5,
          dropPrefix0,
          dropPrefix1,
          dropPrefix2,
          dropPrefix3,
          dropPrefix4,
          dropPrefix5,
          addPrefix0,
          addPrefix1,
          addPrefix2,
          addPrefix3,
          addPrefix4,
          addPrefix5,
          dropCourseNum0,
          dropCourseNum1,
          dropCourseNum2,
          dropCourseNum3,
          dropCourseNum4,
          dropCourseNum5,
          addCourseNum0,
          addCourseNum1,
          addCourseNum2,
          addCourseNum3,
          addCourseNum4,
          addCourseNum5,
          dropSecNo0,
          dropSecNo1,
          dropSecNo2,
          dropSecNo3,
          dropSecNo4,
          dropSecNo5,
          addSecNo0,
          addSecNo1,
          addSecNo2,
          addSecNo3,
          addSecNo4,
          addSecNo5,
          dropDidAttend0,
          dropDidAttend1,
          dropDidAttend2,
          dropDidAttend3,
          dropDidAttend4,
          dropDidAttend5,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          trySetBool(request, 'recieves_financial_aid'),
          request.POST['total_hours_enrolled_after_change'],
          request.POST['comments'],
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
          request.POST['dropCRN0'],
          request.POST['dropCRN1'],
          request.POST['dropCRN2'],
          request.POST['dropCRN3'],
          request.POST['dropCRN4'],
          request.POST['dropCRN5'],
          request.POST['addCRN0'],
          request.POST['addCRN1'],
          request.POST['addCRN2'],
          request.POST['addCRN3'],
          request.POST['addCRN4'],
          request.POST['addCRN5'],
          request.POST['dropPrefix0'],
          request.POST['dropPrefix1'],
          request.POST['dropPrefix2'],
          request.POST['dropPrefix3'],
          request.POST['dropPrefix4'],
          request.POST['dropPrefix5'],
          request.POST['addPrefix0'],
          request.POST['addPrefix1'],
          request.POST['addPrefix2'],
          request.POST['addPrefix3'],
          request.POST['addPrefix4'],
          request.POST['addPrefix5'],
          request.POST['dropCourseNum0'],
          request.POST['dropCourseNum1'],
          request.POST['dropCourseNum2'],
          request.POST['dropCourseNum3'],
          request.POST['dropCourseNum4'],
          request.POST['dropCourseNum5'],
          request.POST['addCourseNum0'],
          request.POST['addCourseNum1'],
          request.POST['addCourseNum2'],
          request.POST['addCourseNum3'],
          request.POST['addCourseNum4'],
          request.POST['addCourseNum5'],
          request.POST['dropSecNo0'],
          request.POST['dropSecNo1'],
          request.POST['dropSecNo2'],
          request.POST['dropSecNo3'],
          request.POST['dropSecNo4'],
          request.POST['dropSecNo5'],
          request.POST['addSecNo0'],
          request.POST['addSecNo1'],
          request.POST['addSecNo2'],
          request.POST['addSecNo3'],
          request.POST['addSecNo4'],
          request.POST['addSecNo5'],
          trySetBool(request, 'dropDidAttend0'),
          trySetBool(request, 'dropDidAttend1'),
          trySetBool(request, 'dropDidAttend2'),
          trySetBool(request, 'dropDidAttend3'),
          trySetBool(request, 'dropDidAttend4'),
          trySetBool(request, 'dropDidAttend5'),
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
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['phone_number'],
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
          date,
          catalog_year,
          name_enrolled_under,
          major_or_minor_name,
          major_was_chosen,
          minor_was_chosen,
          semester,
          year,
          subCourse0A,
          subCourse0B,
          subCourse1A,
          subCourse1B,
          subCourse2A,
          subCourse2B,
          subCourse3A,
          subCourse3B,
          subCourse4A,
          subCourse4B,
          subCourse5A,
          subCourse5B,
          subCourse6A,
          subCourse6B,
          subCourse7A,
          subCourse7B,
          reqCourse0A,
          reqCourse0B,
          reqCourse1A,
          reqCourse1B,
          reqCourse2A,
          reqCourse2B,
          reqCourse3A,
          reqCourse3B,
          reqCourse4A,
          reqCourse4B,
          reqCourse5A,
          reqCourse5B,
          reqCourse6A,
          reqCourse6B,
          reqCourse7A,
          reqCourse7B,
          collegeDistinction0,
          collegeDistinction1,
          lowDivHours,
          upDivHours,
          currentEHRS,
          lessDupCredit,
          hoursTowardGraduation,
          plusHoursOnAudit,
          minReqHours,
          UDReqSatisfied,
          reqWaiver0,
          reqWaiver1,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['catalog_year'],
          request.POST['name_enrolled_under'],
          request.POST['major_or_minor_name'],
          trySetBool(request, 'major_was_chosen'),
          trySetBool(request, 'minor_was_chosen'),
          request.POST['semester'],
          request.POST['year'],
          request.POST['subCourse0A'],
          request.POST['subCourse0B'],
          request.POST['subCourse1A'],
          request.POST['subCourse1B'],
          request.POST['subCourse2A'],
          request.POST['subCourse2B'],
          request.POST['subCourse3A'],
          request.POST['subCourse3B'],
          request.POST['subCourse4A'],
          request.POST['subCourse4B'],
          request.POST['subCourse5A'],
          request.POST['subCourse5B'],
          request.POST['subCourse6A'],
          request.POST['subCourse6B'],
          request.POST['subCourse7A'],
          request.POST['subCourse7B'],
          request.POST['reqCourse0A'],
          request.POST['reqCourse0B'],
          request.POST['reqCourse1A'],
          request.POST['reqCourse1B'],
          request.POST['reqCourse2A'],
          request.POST['reqCourse2B'],
          request.POST['reqCourse3A'],
          request.POST['reqCourse3B'],
          request.POST['reqCourse4A'],
          request.POST['reqCourse4B'],
          request.POST['reqCourse5A'],
          request.POST['reqCourse5B'],
          request.POST['reqCourse6A'],
          request.POST['reqCourse6B'],
          request.POST['reqCourse7A'],
          request.POST['reqCourse7B'],
          request.POST['collegeDistinction0'],
          request.POST['collegeDistinction1'],
          request.POST['lowDivHours'],
          request.POST['upDivHours'],
          request.POST['currentEHRS'],
          request.POST['lessDupCredit'],
          request.POST['hoursTowardGraduation'],
          request.POST['plusHoursOnAudit'],
          request.POST['minReqHours'],
          request.POST['UDReqSatisfied'],
          request.POST['reqWaiver0'],
          request.POST['reqWaiver1'],
          True,
          False,
          False))
      db.commit()
      db.close()
      return redirect('/success')

def processDegreeAuditAmendmentRequest(request):
      db = sqlite3.connect('db.sqlite3')
      cursor = db.cursor()
      cursor.execute('''INSERT INTO DeanProject_degreeauditamendmentrequest(
          student_id_number,
          catalog_year,
          date,
          name_enrolled_under,
          major_was_chosen,
          change_grad_Term_to,
          transfer_Institution,
          course_subject,
          course_num,
          grade,
          semester_taken,
          atu_course_subject,
          atu_course_num,
          course_equivalent,
          course_Substitution,
          transfer_Institution2,
          course_subject2,
          course_num2,
          grade2,
          semester_taken2,
          atu_course_subject2,
          atu_course_num2,
          course_equivalent2,
          course_Substitution2,
          transfer_Institution3,
          course_subject3,
          course_num3,
          grade3,
          semester_taken3,
          atu_course_subject3,
          atu_course_num3,
          course_equivalent3,
          course_Substitution3,
          transfer_Institution4,
          course_subject4,
          course_num4,
          grade4,
          semester_taken4,
          atu_course_subject4,
          atu_course_num4,
          course_equivalent4,
          course_Substitution4,
          transfer_Institution5,
          course_subject5,
          course_num5,
          grade5,
          semester_taken5,
          atu_course_subject5,
          atu_course_num5,
          course_equivalent5,
          course_Substitution5,
          atu_course_prefix1,
          atu_course_number1,
          semester_taken1,
          atu_course_prefix1B,
          atu_course_num1B,
          atu_course_prefix2,
          atu_course_number2,
          semester_taken2B,
          atu_course_prefix2B,
          atu_course_num2B,
          atu_course_prefix3,
          atu_course_number3,
          semester_taken3B,
          atu_course_prefix3B,
          atu_course_num3B,
          atu_course_prefix4,
          atu_course_number4,
          comments4,
          atu_course_prefix5,
          atu_course_number5,
          comments5,
          atu_course_prefix6,
          atu_course_number6,
          comments6,
          college_distinction,
          college_distinction2,
          comments,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['catalog_year'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['major_was_chosen'],
          request.POST['change_grad_Term_to'],
          request.POST['transfer_Institution'],
          request.POST['course_subject'],
          request.POST['course_num'],
          request.POST['grade'],
          request.POST['semester_taken'],
          request.POST['atu_course_subject'],
          request.POST['atu_course_num'],
          trySetBool(request,'course_equivalent'),
          trySetBool(request,'course_Substitution'),
          request.POST['transfer_Institution2'],
          request.POST['course_subject2'],
          request.POST['course_num2'],
          request.POST['grade2'],
          request.POST['semester_taken2'],
          request.POST['atu_course_subject2'],
          request.POST['atu_course_num2'],
          trySetBool(request,'course_equivalent2'),
          trySetBool(request,'course_Substitution2'),
          request.POST['transfer_Institution3'],
          request.POST['course_subject3'],
          request.POST['course_num3'],
          request.POST['grade3'],
          request.POST['semester_taken3'],
          request.POST['atu_course_subject3'],
          request.POST['atu_course_num3'],
          trySetBool(request,'course_equivalent3'),
          trySetBool(request,'course_Substitution3'),
          request.POST['transfer_Institution4'],
          request.POST['course_subject4'],
          request.POST['course_num4'],
          request.POST['grade4'],
          request.POST['semester_taken4'],
          request.POST['atu_course_subject4'],
          request.POST['atu_course_num4'],
          trySetBool(request,'course_equivalent4'),
          trySetBool(request,'course_Substitution4'),
          request.POST['transfer_Institution5'],
          request.POST['course_subject5'],
          request.POST['course_num5'],
          request.POST['grade5'],
          request.POST['semester_taken5'],
          request.POST['atu_course_subject5'],
          request.POST['atu_course_num5'],
          trySetBool(request,'course_equivalent5'),
          trySetBool(request,'course_Substitution5'),
          request.POST['atu_course_prefix1'],
          request.POST['atu_course_number1'],
          request.POST['semester_taken1'],
          request.POST['atu_course_prefix1B'],
          request.POST['atu_course_num1B'],
          request.POST['atu_course_prefix2'],
          request.POST['atu_course_number2'],
          request.POST['semester_taken2B'],
          request.POST['atu_course_prefix2B'],
          request.POST['atu_course_num2B'],
          request.POST['atu_course_prefix3'],
          request.POST['atu_course_number3'],
          request.POST['semester_taken3B'],
          request.POST['atu_course_prefix3B'],
          request.POST['atu_course_num3B'],
          request.POST['atu_course_prefix4'],
          request.POST['atu_course_number4'],
          request.POST['comments4'],
          request.POST['atu_course_prefix5'],
          request.POST['atu_course_number5'],
          request.POST['comments5'],
          request.POST['atu_course_prefix6'],
          request.POST['atu_course_number6'],
          request.POST['comments6'],
          request.POST['college_distinction'],
          request.POST['college_distinction2'],
          request.POST['comments'],
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
          adhe,
          sacm,
          embassy_of_kuwait,
          ade_licensure,
          arsbn,
          isPending,
          isApproved,
          isDenied)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
          (request.POST['student_id_number'],
          request.POST['date'],
          request.POST['name_enrolled_under'],
          request.POST['birth_date'],
          request.POST['mailing_address'],
          request.POST['city'],
          request.POST['state'],
          request.POST['zip_code'],
          request.POST['phone_number'],
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
