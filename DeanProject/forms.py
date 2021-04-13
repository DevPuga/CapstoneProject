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
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'registration_semester': 'Registration Semester',
      'registration_year': 'Registration Year',
      'comments': 'Comments',
      'total_hours_enrolled': 'Total hours enrolled',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.layout = Layout(
        Div(
            HTML("<h2 class='mt-4\'>Permit to Register</h2>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('name_enrolled_under', css_class='col'),
                Div('date', css_class='col-4'),
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
                Div('comments', css_class='col'),
            css_class='row'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )
    self.helper.form_action = '/permitToRegisterForm/'

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
      'total_hours_enrolled_after_change',
      'comments',
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
      'total_hours_enrolled_after_change': 'Total Hours Enrolled After Change',
      'comments': 'Comments',
      'atu_comments': 'Do you feel ATU could have done more to meet your needs? If so please tell us how',
      'another_course_fits_schedule': 'Another Course fits schedule', #Academic Issues
      'changing_major': 'Changing Major',
      'classes_too_large': 'Classes too large',
      'could_not_understand_the_instructor_course_or_materials': 'Couldn\'t understand the instructor course or material',
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

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            HTML("<h2 class='mt-4\'>Add/Drop Course</h2>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('recieves_financial_aid', css_class='col'),
                Div('date', css_class='col-4'),
            css_class='row'),
            Div(
                Div('total_hours_enrolled_after_change', css_class='col'),
                Div('financial_aid_representative_signature', css_class='col-8'),
            css_class='row'),
            Div(
                Div(
                    HTML("<h6 class='mb-0'>Academic issues</h6>"),
                    Div('another_course_fits_schedule'),
                    Div('changing_major'),
                    Div('classes_too_large'),
                    Div('could_not_understand_the_instructor_course_or_materials'),
                    Div('course_not_required_for_major'),
                    Div('inadequate_academic_support_services'),
                    Div('insufficient_high_school_preparation'),
                    Div('lack_of_academic_challenge'),
                    Div('lack_of_progress_in_the_courses'),
                    Div('need_to_re_enroll_in_classes_next_semester'),
                    Div('need_to_re_enroll_in_classes_with_different_instructor'),
                    Div('quality_of_instruction_did_not_meet_expections'),
                    Div('reduce_course_load'),
                    Div('wanted_classes_face_to_face'),
                    Div('wanted_classes_online'),
                    HTML("<h6 class='mt-2 mb-0'>Financial issues</h6>"),
                    Div('change_in_family_financial_circumstances'),
                    Div('didnt_have_enough_money_to_continue'),
                    Div('financial_aid_was_not_sufficient'),
                    Div('increases_in_tuition_and_fees'),
                css_class='col-6'),
                Div(
                    Div('incurred_too_much_debt'),
                    Div('needed_Course_for_financial_aid_eligibility'),
                    Div('scholarship_Grant_was_not_renewed'),
                    HTML("<h6 class='mt-2 mb-0'>Family issues</h6>"),
                    Div('family_illness_responsibility'),
                    Div('homesick'),
                    Div('wanted_to_be_closer_to_family_and_friends'),
                    HTML("<h6 class='mt-2 mb-0'>Housing and travel issues</h6>"),
                    Div('commute_too_long'),
                    Div('moved_out_of_the_area'),
                    HTML("<h6 class='mt-2 mb-0'>Personal and transition issues</h6>"),
                    Div('distracted_Social_life'),
                    Div('felt_class_climate_unwelcoming'),
                    Div('felt_out_of_place_in_class'),
                    Div('impact_of_natural_disaster'),
                    Div('inadequate_study_skills_or_lack_of_academic_success'),
                    Div('military_obligations'),
                    Div('personal_health'),
                    Div('personal_emergency'),
                    Div('unmotivated_for_this_courses_or_tired_of_school'),
                    Div('working_too_many_hours'),
                css_class='col'),
            css_class='row mb-2'),
            Div(
                Div('comments', css_class='col'),
            css_class='row'),
            Div(
                Div('atu_comments', css_class='col'),
            css_class='row'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )

class UGGraduationForm(forms.ModelForm):
  class Meta:
    model = UGGraduation
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'phone_number',
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
            HTML("<h2 class='mt-4\'>Undergraduate Graduation Application</h2>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
                Div('date', css_class='col-4'),
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
            HTML("<h2 class='mt-4\'>Master's Graduation Application</h2>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('mailing_address', css_class='col'),
                Div('date', css_class='col'),
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
      'date',
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
      'date': 'Submit Date',
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
            HTML("<h2 class='mt-4\'>Degree Audit</h2>"),
            HTML("<hr class='solid my-1\'>"),
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
                Div('date', css_class='col'),
            css_class='row'),

        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary mt-2')
        )
    )

class degreeAuditAmendmentRequestForm(forms.ModelForm):
  class Meta:
    model = degreeAuditAmendmentRequest
    fields = [
      'student_id_number',
      'catalog_year',
      'date',
      'name_enrolled_under',
      'major_was_chosen',
      'change_grad_Term_to',
      'transfer_Institution',
      'course_subject',
      'course_num',
      'grade',
      'semester_taken',
      'atu_course_subject',
      'atu_course_num',
      'course_equivalent',
      'course_Substitution',
      'transfer_Institution2',
      'course_subject2',
      'course_num2',
      'grade2',
      'semester_taken2',
      'atu_course_subject2',
      'atu_course_num2',
      'course_equivalent2',
      'course_Substitution2',
      'transfer_Institution3',
      'course_subject3',
      'course_num3',
      'grade3',
      'semester_taken3',
      'atu_course_subject3',
      'atu_course_num3',
      'course_equivalent3',
      'course_Substitution3',
      'transfer_Institution4',
      'course_subject4',
      'course_num4',
      'grade4',
      'semester_taken4',
      'atu_course_subject4',
      'atu_course_num4',
      'course_equivalent4',
      'course_Substitution4',
      'transfer_Institution5',
      'course_subject5',
      'course_num5',
      'grade5',
      'semester_taken5',
      'atu_course_subject5',
      'atu_course_num5',
      'course_equivalent5',
      'course_Substitution5',
      'atu_course_prefix1',
      'atu_course_num1',
      'semester_taken1',
      'atu_course_prefix1B',
      'atu_course_num1B',
      'atu_course_prefix2',
      'atu_course_num2',
      'semester_taken2',
      'atu_course_prefix2B',
      'atu_course_num2B',
      'atu_course_prefix3',
      'atu_course_num3',
      'semester_taken3',
      'atu_course_prefix3B',
      'atu_course_num3B',
      'atu_course_prefix4',
      'atu_course_num4',
      'comments4',
      'atu_course_prefix5',
      'atu_course_num5',
      'comments5',
      'atu_course_prefix6',
      'atu_course_num6',
      'comments6',
      'college_distinction',
      'college_distinction2',
      'comments',
    ]
    labels = {
      'student_id_number': 'T Number',
      'catalog_year': 'Catalog Year',
      'date': 'Submit Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'major_was_chosen': 'Major',
      'change_grad_Term_to': 'Change Graduation Term to',
      'transfer_Institution': 'Transfer Institution',
      'course_subject': 'Course Subject',
      'course_num': 'Course Number',
      'grade': 'Grade',
      'semester_taken': 'Semester Taken',
      'atu_course_subject': 'ATU Course Subject',
      'atu_course_num': 'ATU Course Number',
      'course_equivalent': 'Course Equivalent',
      'course_Substitution': 'Course Substitution',
      'transfer_Institution2':'',
      'course_subject2': '',
      'course_num2': '',
      'grade2': '',
      'semester_taken2': '',
      'atu_course_subject2':'',
      'atu_course_num2':'',
      'course_equivalent2':'',
      'course_Substitution2':'',
      'transfer_Institution3':'',
      'course_subject3':'',
      'course_num3':'',
      'grade3':'',
      'semester_taken3':'',
      'atu_course_subject3':'',
      'atu_course_num3':'',
      'course_equivalent3':'',
      'course_Substitution3':'',
      'transfer_Institution4':'',
      'course_subject4':'',
      'course_num4':'',
      'grade4':'',
      'semester_taken4':'',
      'atu_course_subject4':'',
      'atu_course_num4':'',
      'course_equivalent4':'',
      'course_Substitution4':'',
      'transfer_Institution5':'',
      'course_subject5':'',
      'course_num5':'',
      'grade5':'',
      'semester_taken5':'',
      'atu_course_subject5':'',
      'atu_course_num5':'',
      'course_equivalent5':'',
      'course_Substitution5':'',
      'atu_course_prefix1':'Course Prefix',
      'atu_course_num1':'Course Number',
      'semester_taken1':'Semester Taken',
      'atu_course_prefix1B':'',
      'atu_course_num1B':'',
      'atu_course_prefix2':'',
      'atu_course_num2':'',
      'semester_taken2':'',
      'atu_course_prefix2B':'',
      'atu_course_num2B':'',
      'atu_course_prefix3':'',
      'atu_course_num3':'',
      'semester_taken3':'',
      'atu_course_prefix3B':'',
      'atu_course_num3B':'',
      'atu_course_prefix4':'Course Prefix',
      'atu_course_num4':'Course Number',
      'comments4':'Comments',
      'atu_course_prefix5':'',
      'atu_course_num5':'',
      'comments5':'',
      'atu_course_prefix6':'',
      'atu_course_num6': '',
      'comments6': '',
      'college_distinction': 'College Distinction 1.',
      'college_distinction2': '2.',
      'comments': 'Comments',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            HTML("<h2 class='mt-4\'>Degree Audit Amendment Request</h2>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('student_id_number', css_class='col'),
                Div('catalog_year', css_class='col'),
            css_class='row'),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('major_was_chosen', css_class='row mt-3'),
                Div('change_grad_Term_to', css_class='row mt-3'),
            css_class='row'),
            Div(
                Div('transfer_Institution',css_class='col-8'),
                Div('course_subject',css_class='col-8'),
                Div('course_num',css_class='col-8'),
                Div('grade',css_class='col-8'),
                Div('semester_taken',css_class = 'col-8'),
                Div('atu_course_subject',css_class = 'col-8'),
                Div('atu_course_number',css_class = 'col-8'),
                Div('course_equivalent',css_class = 'col-8'),
                Div('course_substitution',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('transfer_Institution2',css_class='col-8'),
                Div('course_subject2',css_class='col-8'),
                Div('course_num2',css_class='col-8'),
                Div('grade2',css_class='col-8'),
                Div('semester_taken2',css_class = 'col-8'),
                Div('atu_course_subject2',css_class = 'col-8'),
                Div('atu_course_number2',css_class = 'col-8'),
                Div('course_equivalent2',css_class = 'col-8'),
                Div('course_substitution2',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('transfer_Institution3',css_class='col-8'),
                Div('course_subject3',css_class='col-8'),
                Div('course_num3',css_class='col-8'),
                Div('grade3',css_class='col-8'),
                Div('semester_taken3',css_class = 'col-8'),
                Div('atu_course_subject3',css_class = 'col-8'),
                Div('atu_course_number3',css_class = 'col-8'),
                Div('course_equivalent3',css_class = 'col-8'),
                Div('course_substitution3',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('transfer_Institution4',css_class='col-8'),
                Div('course_subject4',css_class='col-8'),
                Div('course_num4',css_class='col-8'),
                Div('grade4',css_class='col-8'),
                Div('semester_taken4',css_class = 'col-8'),
                Div('atu_course_subject4',css_class = 'col-8'),
                Div('atu_course_number4',css_class = 'col-8'),
                Div('course_equivalent4',css_class = 'col-8'),
                Div('course_substitution4',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('transfer_Institution5',css_class='col-8'),
                Div('course_subject5',css_class='col-8'),
                Div('course_num5',css_class='col-8'),
                Div('grade5',css_class='col-8'),
                Div('semester_taken5',css_class = 'col-8'),
                Div('atu_course_subject5',css_class = 'col-8'),
                Div('atu_course_number5',css_class = 'col-8'),
                Div('course_equivalent5',css_class = 'col-8'),
                Div('course_substitution5',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('atu_course_prefix',css_class='col-8'),
                Div('atu_course_num1',css_class='col-8'),
                Div('semester_taken1',css_class='col-8'),
                Div('atu_course_prefix1B',css_class='col-8'),
                Div('atu_course_num1B',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('atu_course_prefix2',css_class = 'col-8'),
                Div('atu_course_num2',css_class = 'col-8'),
                Div('semester_taken2',css_class = 'col-8'),
                Div('atu_course_prefix2B',css_class = 'col-8'),
                Div('atu_course_num2B',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('atu_course_prefix3',css_class = 'col-8'),
                Div('atu_course_num3',css_class = 'col-8'),
                Div('semester_taken3',css_class = 'col-8'),
                Div('atu_course_prefix3B',css_class = 'col-8'),
                Div('atu_course_num3B',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('atu_course_prefix4',css_class='col-8'),
                Div('atu_course_num4',css_class='col-8'),
                Div('semester_taken4',css_class='col-8'),
                Div('comments4',css_class='col-8'),
            css_class='row'),
            Div(
                Div('atu_course_prefix5',css_class = 'col-8'),
                Div('atu_course_num5',css_class = 'col-8'),
                Div('semester_taken5',css_class = 'col-8'),
                Div('comments5',css_class = 'col-8'),
            css_class='row'),
            Div(
                Div('atu_course_prefix6',css_class = 'col-8'),
                Div('atu_course_num6',css_class = 'col-8'),
                Div('semester_taken6',css_class = 'col-8'),
                Div('comments6',css_class = 'col-8'),
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
      'adhe': 'ADHE (AR Lottery Scholarship)',
      'sacm': 'SACM (Saudi Arabian Cultural Mission)',
      'embassy_of_kuwait': 'Embassy of Kuwait',
      'ade_licensure': 'ADE Licensure (AR Dept. of Ed.)',
      'arsbn': 'ARSBN (AR State Board of Nursing)',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            HTML("<h2 class='mt-4\'>Transcript Request</h2>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('mailing_address', css_class='col'),
                Div('date', css_class='col'),
            css_class='row'),
            Div(
                Div('city', css_class='col-8'),
                Div('state', css_class='col'),
                Div('zip_code', css_class='col'),
            css_class='row'),
            Div(
                Div('phone_number', css_class='col'),
                Div('birth_date', css_class='col'),
            css_class='row'),
            Div(
            HTML("<p class='my-2'>Send my transcript to:</p>"),
                Div(
                    Div('adhe', css_class='row'),
                    Div('sacm', css_class='row'),
                    Div('embassy_of_kuwait', css_class='row'),
                css_class='col'),
                Div(
                    Div('ade_licensure', css_class='row'),
                    Div('arsbn', css_class='row'),
                css_class='col'),
            css_class='row mb-2'),
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
