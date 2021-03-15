from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from .models import *

class permitToRegisterForm(forms.ModelForm):
  class Meta:
    model = permitToRegister
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'registration_semester',
      'registration_year',
      'comments',
      'total_hours_enrolled',
      'dean_signature',
      'advisor_signature',
      'student_signature',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'registration_semester': 'Registration Semester',
      'registration_year': 'Registration Year',
      'comments': 'Comments',
      'total_hours_enrolled': 'Total hours enrolled',
      'dean_signature': 'Dean’s Signature, Overload Approval',
      'advisor_signature': 'Advisor’s Signature',
      'student_signature': 'Student’s Signature',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            Div(
                Div('name_enrolled_under', css_class='col'),
            css_class='row'),
            Div(
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('registration_semester', css_class='col'),
                Div('registration_year', css_class='col'),
            css_class='row'),
            Div(
                Div('total_hours_enrolled', css_class='col'),
                Div('dean_signature', css_class='col-8'),
            css_class='row'),
            Div(
                Div('student_signature', css_class='col-8'),
                Div('date', css_class='col-4'),
            css_class='row'),
            Div(
                Div('advisor_signature', css_class='col'),
            css_class='row'),
            Div(
                Div('comments', css_class='col'),
            css_class='row'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )

class courseInfoForm(forms.ModelForm): #WIP (not WAP)
  class Meta:
    model = courseInfo
    fields = [
      'crn',
      'course_prefix',
      'course_number',
      'sec_no',
    ]
    labels = {
      'crn': 'CRN',
      'course_prefix': 'Course Prefix',
      'course_number': 'Course Number',
      'sec_no': 'Sec No.',
    }

class add_dropClassForm(forms.ModelForm):
  class Meta:
    model = add_dropClass
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'recieves_financial_aid', #Yes/No
      'financial_aid_representative_signature', #Signature
      'total_hours_enrolled_after_change',
      'comments',
      'advisor_signature', #Signature
      'student_signature', #Signature
      'atu_comments',
      'another_course_fits_schedule', #Academic Issues
      'changing_major',
      'changing_minor',
      'classes_too_large',
      'could_not_understand_the_instructor_course_or_materials',
      'course_not_required_for_major',
      'inadequate_academic_support_services',
      'insufficient_high_school_preparation',
      'lack_of_academic_challenge',
      'lack_of_progress_in_the_courses',
      'need_to_re_enroll_in_classes_next_semester',
      'need_to_re_enroll_in_classes_with_different_instructor',
      'quality_of_instruction_did_not_meet_expections',
      'reduce_course_load',
      'wanted_classes_face_to_face',
      'wanted_classes_online',
      'change_in_family_financial_circumstances', #Financial Issues
      'didnt_have_enough_money_to_continue',
      'financial_aid_was_not_sufficient',
      'increases_in_tuition_and_fees',
      'incurred_too_much_debt',
      'needed_Course_for_financial_aid_eligibility',
      'scholarship_Grant_was_not_renewed',
      'family_illness_responsibility', #Family Issues
      'homesick',
      'wanted_to_be_closer_to_family_and_friends',
      'commute_too_long', #Housing and Travel Issues
      'moved_out_of_the_area',
      'distracted_Social_life', #Personal and Transition Issues
      'felt_class_climate_unwelcoming',
      'felt_out_of_place_in_class',
      'impact_of_natural_disaster',
      'inadequate_study_skills_or_lack_of_academic_success',
      'military_obligations',
      'personal_health',
      'personal_emergency',
      'unmotivated_for_this_courses_or_tired_of_school',
      'working_too_many_hours',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'recieves_financial_aid': 'Do you receive financial aid? (loans, grants, scholarships)', #Yes/No
      'financial_aid_representative_signature': 'Financial Aid Representative Signature', #Signature
      'total_hours_enrolled_after_change': 'Total Hours Enrolled After Change',
      'comments': 'Comments',
      'advisor_signature': 'Advisor\'s Signature', #Signature
      'student_signature': 'Student\'s Signature', #Signature
      'atu_comments': 'Do you feel ATU could have done more to meet your needs? If so please tell us how',
      'another_course_fits_schedule': 'Another Course fits schedule', #Academic Issues
      'changing_major': 'Changing Major',
      'classes_too_large': 'Classes too large',
      'could_not_understand_the_instructor_course_or_materials': 'Could not understand the instructor course or material',
      'course_not_required_for_major': 'Course not required for Major',
      'inadequate_academic_support_services': 'Inadequate academic support services',
      'insufficient_high_school_preparation': 'Insufficient high school preparation',
      'lack_of_academic_challenge': 'Lack of academic challenge',
      'lack_of_progress_in_the_courses': 'Lack of progress in the course(s)',
      'need_to_re_enroll_in_classes_next_semester': 'Need to re-enroll in class(es) next semester',
      'need_to_re_enroll_in_classes_with_different_instructor': 'Need to re-enroll in class(es) with different instructor',
      'quality_of_instruction_did_not_meet_expections': 'Quality of instruction did not meet expectations',
      'reduce_course_load': 'Reduce course load',
      'wanted_classes_face_to_face': 'Wanted class(es) face to face',
      'wanted_classes_online': 'Wanted class(es) online',
      'change_in_family_financial_circumstances': 'Changing in Family Circumstances', #Financial Issues
      'didnt_have_enough_money_to_continue': 'Didn’t have enough money to continue',
      'financial_aid_was_not_sufficient': 'Financial aid was not sufficient',
      'increases_in_tuition_and_fees': 'Increases in tuition and fees ',
      'incurred_too_much_debt': 'Incurred too much debt',
      'needed_Course_for_financial_aid_eligibility': 'Needed course for financial aid eligibility',
      'scholarship_Grant_was_not_renewed': 'Scholarship/grant was not renewed',
      'family_illness_responsibility': 'Family illness/responsibility', #Family Issues
      'homesick': 'Homesick',
      'wanted_to_be_closer_to_family_and_friends': ' Wanted to be closer to family and friends',
      'commute_too_long': 'Commute too long ', #Housing and Travel Issues
      'moved_out_of_the_area': 'Moved out of the area ',
      'distracted_Social_life': 'Distracted by social life ', #Personal and Transition Issues
      'felt_class_climate_unwelcoming': 'Felt class climate unwelcoming',
      'felt_out_of_place_in_class': 'Felt out of place in class',
      'impact_of_natural_disaster': 'Impact of natural disaster',
      'inadequate_study_skills_or_lack_of_academic_success': 'Inadequate study skills or lack of academic success',
      'military_obligations': 'Military obligations',
      'personal_health': 'Personal health',
      'personal_emergency': 'Personal emergency ',
      'unmotivated_for_this_courses_or_tired_of_school': 'Unmotivated for this course(s) or tired of school ',
      'working_too_many_hours': 'Working too many hours',
    }

class UGGraduationForm(forms.ModelForm):
  class Meta:
    model = UGGraduation
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'phone_number',
      'student_signature', #Signature
      'diploma_name',
      'name_pronunciation',
      'pronunciation_recorded', #Weird
      'parents_completed_bachelor_degree', #Yes/No
      'expected_graduation_term',
      'expected_graduation_year',
      'preferred_degree',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'phone_number': 'Phone Number',
      'student_signature': 'Student Signature',  #Signature
      'diploma_name': 'Print Your Name Exactly As You Want It To Appear On Your Diploma',
      'name_pronunciation': 'Name Pronounciation',
      'pronunciation_recorded': 'Pronunciation Recorded', #Weird
      'parents_completed_bachelor_degree': 'Did either of your parents complete a bachelor\'s degree?', #Yes/No
      'expected_graduation_term': 'Expected Graduation Term',
      'expected_graduation_year': 'Expected Graduation Year',
      'preferred_degree': 'If you are seeking two Bachelor’s degrees (Double Degree), please indicate which major you’d like to walk with in the ceremony',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('phone_number', css_class='col'),
                Div('expected_graduation_term', css_class='col'),
                Div('expected_graduation_year', css_class='col'),
            css_class='row'),
            Div(
                Div('preferred_degree', css_class='col'),
            css_class='row'),
            Div(
                Div('diploma_name', css_class='col-8'),
                Div('name_pronunciation', css_class='col'),
                Div('pronunciation_recorded'),
            css_class='row'),
            Div(
                Div('parents_completed_bachelor_degree', css_class='col'),
            css_class='row'),
            Div(
                Div('student_signature', css_class='col-8'),
                Div('date', css_class='col-4'),
            css_class='row'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )

class masterGraduationForm(forms.ModelForm):
  class Meta:
    model = masterGraduation
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'mailing_address',
      'city',
      'state',
      'zip_code',
      'phone_number',
      'email',
      'student_starting_semester',
      'student_starting_year',
      'diploma_name',
      'name_pronunciation',
      'expected_graduation_term',
      'expected_graduation_year',
      'degree_name',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'mailing_address': 'Mailing Address',
      'city': 'City',
      'state': 'State',
      'zip_code': 'ZIP',
      'phone_number': 'Phone Number',
      'email': 'Email',
      'student_starting_semester': 'In what semester did you begin your graduate studies?',
      'student_starting_year': 'In what year did you begin your graduate studies?',
      'diploma_name': 'PRINT YOUR NAME EXACTLY AS YOU WANT IT TO APPEAR ON YOUR DIPLOMA',
      'name_pronunciation': 'Name Pronounciation',
      'expected_graduation_term': 'Expected Term of Graduation',
      'expected_graduation_year': 'Year',
      'degree_name': 'Degree',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('mailing_address', css_class='col'),
            css_class='row'),
            Div(
                Div('city', css_class='col'),
                Div('state', css_class='col'),
                Div('zip_code', css_class='col'),
            css_class='row'),
            Div(
                Div('phone_number', css_class='col'),
                Div('email', css_class='col'),
            css_class='row'),
            Div(
                Div('student_starting_semester', css_class='col'),
            css_class='row'),
            Div(
                Div('student_starting_year', css_class='col'),
            css_class='row'),
            Div(
                Div('expected_graduation_term', css_class='col'),
                Div('expected_graduation_year', css_class='col'),
            css_class='row'),
            Div(
                Div('diploma_name', css_class='col'),
            css_class='row'),
            Div(
                Div('name_pronunciation', css_class='col'),
            css_class='row'),
            Div(
                Div('degree_name', css_class='col'),
            css_class='row'),
            Div(
                Div('date', css_class='col'),
            css_class='row'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )

class degreeAuditForm(forms.ModelForm):
  class Meta:
    model = degreeAudit
    fields = [
      'student_id_number',
      'catalog_year',
      'name_enrolled_under',
      'major_or_minor_name',
      'major_was_chosen',
      'minor_was_chosen',
      'semester',
      'year',
    ]
    labels = {
      'student_id_number': 'T Number',
      'catalog_year': 'Catalog Year',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'major_or_minor_name': 'Major or Minor',
      'major_was_chosen': 'Major',
      'minor_was_chosen': 'Minor',
      'semester': 'All requirements will be completed at the end of',
      'year': 'Year',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('major_or_minor_name', css_class='col-8'),
                Div('catalog_year', css_class='col'),
                Div(
                    Div('major_was_chosen', css_class='row mt-3'),
                    Div('minor_was_chosen', css_class='row'),
                css_class='col'),
            css_class='row'),
            Div(
                Div('semester', css_class='col'),
                Div('year', css_class='col'),
            css_class='row'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )

class transcriptRequestForm(forms.ModelForm):
  class Meta:
    model = transcriptRequest
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'birth_date',
      'mailing_address',
      'city',
      'state',
      'zip_code',
      'phone_number',
      'student_signature', #Signature
      'adhe',
      'sacm',
      'embassy_of_kuwait',
      'ade_licensure',
      'arsbn',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'birth_date': 'Date of Birth',
      'mailing_address': 'Mailing Address',
      'city': 'City',
      'state': 'State',
      'zip_code': 'ZIP',
      'phone_number': 'Phone Number',
      'student_signature': 'Student Signature',  #Signature
      'adhe': 'ADHE',
      'sacm': 'SACM',
      'embassy_of_kuwait': 'Embassy of Kuwait',
      'ade_licensure': 'ADE Licensure',
      'arsbn': 'ARSBN',
    }

class courseInfoForm(forms.ModelForm): #WIP (not WAP)
  class Meta:
    model = courseInfo
    fields = [
      'crn',
      'course_prefix',
      'course_number',
      'sec_no',
    ]
    labels = {
      'crn': 'CRN',
      'course_prefix': 'Course Prefix',
      'course_number': 'Course Number',
      'sec_no': 'Sec No.',
    }

class substitutionRequestForm(forms.ModelForm): #WIP (not WAP)
  class Meta:
    model = substitutionRequest
    fields = [
      'current_course',
      'requested_course',
    ]
    labels = {
      'current_course': 'Current Course Prefix/Number',
      'requested_course': 'Requested Course Prefix/Number',
    }

class emptyForm(forms.ModelForm):
    class Meta:
        model = empty
        fields = []
