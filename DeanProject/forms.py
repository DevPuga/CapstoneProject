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
      'crn0',
      'prefix0',
      'courseNum0',
      'secNo0',
      'crn1',
      'prefix1',
      'courseNum1',
      'secNo1',
      'crn2',
      'prefix2',
      'courseNum2',
      'secNo2',
      'crn3',
      'prefix3',
      'courseNum3',
      'secNo3',
      'crn4',
      'prefix4',
      'courseNum4',
      'secNo4',
      'crn5',
      'prefix5',
      'courseNum5',
      'secNo5',
      'crn6',
      'prefix6',
      'courseNum6',
      'secNo6',
      'crn7',
      'prefix7',
      'courseNum7',
      'secNo7',
      'crn8',
      'prefix8',
      'courseNum8',
      'secNo8',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'registration_semester': 'Registration Semester',
      'registration_year': 'Registration Year',
      'comments': 'Comments',
      'total_hours_enrolled': 'Total hours enrolled',
      'crn0': 'CRN',
      'crn1': '',
      'crn2': '',
      'crn3': '',
      'crn4': '',
      'crn5': '',
      'crn6': '',
      'crn7': '',
      'crn8': '',
      'prefix0': 'Course Prefix',
      'prefix1': '',
      'prefix2': '',
      'prefix3': '',
      'prefix4': '',
      'prefix5': '',
      'prefix6': '',
      'prefix7': '',
      'prefix8': '',
      'courseNum0': 'Course Number',
      'courseNum1': '',
      'courseNum2': '',
      'courseNum3': '',
      'courseNum4': '',
      'courseNum5': '',
      'courseNum6': '',
      'courseNum7': '',
      'courseNum8': '',
      'secNo0': 'Sec No.',
      'secNo1': '',
      'secNo2': '',
      'secNo3': '',
      'secNo4': '',
      'secNo5': '',
      'secNo6': '',
      'secNo7': '',
      'secNo8': '',
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
            HTML('''<p class='my-1'><strong>All obligations to Arkansas Tech
                University must be satisfied and holds lifted before Registration
                is permitted.
                Check OneTech for any existing Registration Holds, and contact
                the appropriate office to resolve.</strong></p>'''),
            HTML("<p class='my-1'>Please enter all courses you wish to enroll in:</p>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('crn0', css_class='col'),
                Div('prefix0', css_class='col'),
                Div('courseNum0', css_class='col'),
                Div('secNo0', css_class='col'),
            css_class='row'),
            Div(
                Div('crn1', css_class='col'),
                Div('prefix1', css_class='col'),
                Div('courseNum1', css_class='col'),
                Div('secNo1', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn2', css_class='col'),
                Div('prefix2', css_class='col'),
                Div('courseNum2', css_class='col'),
                Div('secNo2', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn3', css_class='col'),
                Div('prefix3', css_class='col'),
                Div('courseNum3', css_class='col'),
                Div('secNo3', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn4', css_class='col'),
                Div('prefix4', css_class='col'),
                Div('courseNum4', css_class='col'),
                Div('secNo4', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn5', css_class='col'),
                Div('prefix5', css_class='col'),
                Div('courseNum5', css_class='col'),
                Div('secNo5', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn6', css_class='col'),
                Div('prefix6', css_class='col'),
                Div('courseNum6', css_class='col'),
                Div('secNo6', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn7', css_class='col'),
                Div('prefix7', css_class='col'),
                Div('courseNum7', css_class='col'),
                Div('secNo7', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('crn8', css_class='col'),
                Div('prefix8', css_class='col'),
                Div('courseNum8', css_class='col'),
                Div('secNo8', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('total_hours_enrolled', css_class='col'),
            css_class='row pt-1'),
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
      'dropCRN0',
      'dropCRN1',
      'dropCRN2',
      'dropCRN3',
      'dropCRN4',
      'dropCRN5',
      'addCRN0',
      'addCRN1',
      'addCRN2',
      'addCRN3',
      'addCRN4',
      'addCRN5',
      'dropPrefix0',
      'dropPrefix1',
      'dropPrefix2',
      'dropPrefix3',
      'dropPrefix4',
      'dropPrefix5',
      'addPrefix0',
      'addPrefix1',
      'addPrefix2',
      'addPrefix3',
      'addPrefix4',
      'addPrefix5',
      'dropCourseNum0',
      'dropCourseNum1',
      'dropCourseNum2',
      'dropCourseNum3',
      'dropCourseNum4',
      'dropCourseNum5',
      'addCourseNum0',
      'addCourseNum1',
      'addCourseNum2',
      'addCourseNum3',
      'addCourseNum4',
      'addCourseNum5',
      'dropSecNo0',
      'dropSecNo1',
      'dropSecNo2',
      'dropSecNo3',
      'dropSecNo4',
      'dropSecNo5',
      'addSecNo0',
      'addSecNo1',
      'addSecNo2',
      'addSecNo3',
      'addSecNo4',
      'addSecNo5',
      'dropDidAttend0',
      'dropDidAttend1',
      'dropDidAttend2',
      'dropDidAttend3',
      'dropDidAttend4',
      'dropDidAttend5',
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
      'dropCRN0': 'CRN',
      'dropCRN1': '',
      'dropCRN2': '',
      'dropCRN3': '',
      'dropCRN4': '',
      'dropCRN5': '',
      'addCRN0': 'CRN',
      'addCRN1': '',
      'addCRN2': '',
      'addCRN3': '',
      'addCRN4': '',
      'addCRN5': '',
      'dropPrefix0': 'Course Prefix',
      'dropPrefix1': '',
      'dropPrefix2': '',
      'dropPrefix3': '',
      'dropPrefix4': '',
      'dropPrefix5': '',
      'addPrefix0': 'Course Prefix',
      'addPrefix1': '',
      'addPrefix2': '',
      'addPrefix3': '',
      'addPrefix4': '',
      'addPrefix5': '',
      'dropCourseNum0': 'Course Number',
      'dropCourseNum1': '',
      'dropCourseNum2': '',
      'dropCourseNum3': '',
      'dropCourseNum4': '',
      'dropCourseNum5': '',
      'addCourseNum0': 'Course Number',
      'addCourseNum1': '',
      'addCourseNum2': '',
      'addCourseNum3': '',
      'addCourseNum4': '',
      'addCourseNum5': '',
      'dropSecNo0': 'Section No.',
      'dropSecNo1': '',
      'dropSecNo2': '',
      'dropSecNo3': '',
      'dropSecNo4': '',
      'dropSecNo5': '',
      'addSecNo0': 'Section No.',
      'addSecNo1': '',
      'addSecNo2': '',
      'addSecNo3': '',
      'addSecNo4': '',
      'addSecNo5': '',
      'dropDidAttend0': 'I attended this class',
      'dropDidAttend1': 'I attended this class',
      'dropDidAttend2': 'I attended this class',
      'dropDidAttend3': 'I attended this class',
      'dropDidAttend4': 'I attended this class',
      'dropDidAttend5': 'I attended this class',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div(
            HTML("<h2 class='mt-4\'>Add/Drop Course</h2>"),
            HTML("<hr class='solid my-1\'>"),
            HTML('''<p class='my-2'><strong>Dropping ALL of your courses? Do not complete this form;
                contact the Office of the Registrar to begin the total withdrawal
                 process.</strong></p>'''),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('student_id_number', css_class='col'),
            css_class='row'),
            Div(
                Div('recieves_financial_aid', css_class='col'),
                Div('date', css_class='col-4'),
            css_class='row my-1'),
            HTML('''<h5 class='mt-4'><strong>Dates below are for full-term classes: January 11 - May 4, 2021</strong></h5>'''),
            HTML('''<p class='my-1'>Last day 100% refund - tuition/fees: <strong>January 15</strong></p>'''),
            HTML('''<p class='my-1'>Last day to add/change sections : <strong>January 15</strong></p>'''),
            HTML('''<p class='my-1'>Last day to drop with course(s) not reflected on transcript: <strong>January 26</strong></p>'''),
            HTML('''<p class='my-1'>Last day 80% reduction/tuition: <strong>January 26</strong></p>'''),
            HTML('''<p class='my-1'>Last day to drop with a "W" or change to audit: <strong>April 16</strong></p>'''),
            HTML('''<p><strong>For condensed class dates visit Condensed Courses on the Registration tab in OneTech or click <a href="https://ssbprod.atu.edu/pls/PROD/hws9date.p_displayForm" target="_blank">here</a></strong></p>'''),
            HTML('''<h4 style="text-decoration:underline;"><strong>*WARNING: DROPPING A COURSE MAY RESULT IN LOSS OF YOUR FINANCIAL AID or VETERAN BENEFITS</strong></h4>'''),
            HTML('''<p class='my-1'><strong>SCHOLARSHIPS</strong> - Academic scholarships require completion of at least 15 hours. Requirements for private scholarships vary in required number of hours.</p>'''),
            HTML('''<p class='my-1'><strong>LOANS</strong> - Requirements vary based on policy.</p>'''),
            HTML('''<p class='my-1'><strong>GRANTS</strong> - Requirements vary in conjunction with the amount of grant you receive.</p>'''),
            HTML('''<p class='my-1'>For questions concerning scholarships, loans and grants, please contact the Financial Aid Office: Brown Hall, Suite 206 or call 479-968-0399.</p>'''),
            HTML('''<p class='my-1'><strong>VETERANS BENEFITS</strong> - Dropping below full-time may affect benefits; please contact Veteran Services: Doc Bryan, Suite 104 or call 479-968-0445.</p>'''),
            HTML('''<h4 class='mt-4'>Dropping:</h4>'''),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('dropCRN0', css_class='col'),
                Div('dropPrefix0', css_class='col'),
                Div('dropCourseNum0', css_class='col'),
                Div('dropSecNo0', css_class='col'),
                Div('dropDidAttend0', css_class='col', style='margin-top: 32px;'),
            css_class='row pt-1'),
            Div(
                Div('dropCRN1', css_class='col'),
                Div('dropPrefix1', css_class='col'),
                Div('dropCourseNum1', css_class='col'),
                Div('dropSecNo1', css_class='col'),
                Div('dropDidAttend1', css_class='col my-auto'),
            css_class='row pt-1'),
            Div(
                Div('dropCRN2', css_class='col'),
                Div('dropPrefix2', css_class='col'),
                Div('dropCourseNum2', css_class='col'),
                Div('dropSecNo2', css_class='col'),
                Div('dropDidAttend2', css_class='col my-auto'),
            css_class='row pt-1'),
            Div(
                Div('dropCRN3', css_class='col'),
                Div('dropPrefix3', css_class='col'),
                Div('dropCourseNum3', css_class='col'),
                Div('dropSecNo3', css_class='col'),
                Div('dropDidAttend3', css_class='col my-auto'),
            css_class='row pt-1'),
            Div(
                Div('dropCRN4', css_class='col'),
                Div('dropPrefix4', css_class='col'),
                Div('dropCourseNum4', css_class='col'),
                Div('dropSecNo4', css_class='col'),
                Div('dropDidAttend4', css_class='col my-auto'),
            css_class='row pt-1'),
            Div(
                Div('dropCRN5', css_class='col'),
                Div('dropPrefix5', css_class='col'),
                Div('dropCourseNum5', css_class='col'),
                Div('dropSecNo5', css_class='col'),
                Div('dropDidAttend5', css_class='col my-auto'),
            css_class='row pt-1'),
            HTML('''<h4 class='mt-4'>Adding:</h4>'''),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('addCRN0', css_class='col'),
                Div('addPrefix0', css_class='col'),
                Div('addCourseNum0', css_class='col'),
                Div('addSecNo0', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('addCRN1', css_class='col'),
                Div('addPrefix1', css_class='col'),
                Div('addCourseNum1', css_class='col'),
                Div('addSecNo1', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('addCRN2', css_class='col'),
                Div('addPrefix2', css_class='col'),
                Div('addCourseNum2', css_class='col'),
                Div('addSecNo2', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('addCRN3', css_class='col'),
                Div('addPrefix3', css_class='col'),
                Div('addCourseNum3', css_class='col'),
                Div('addSecNo3', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('addCRN4', css_class='col'),
                Div('addPrefix4', css_class='col'),
                Div('addCourseNum4', css_class='col'),
                Div('addSecNo4', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('addCRN5', css_class='col'),
                Div('addPrefix5', css_class='col'),
                Div('addCourseNum5', css_class='col'),
                Div('addSecNo5', css_class='col'),
            css_class='row pt-1 mb-2'),
            Div(
                Div('total_hours_enrolled_after_change', css_class='col'),
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
            css_class='row my-2'),
        css_class=''),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-primary')
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
      'subCourse0A',
      'subCourse0B',
      'subCourse1A',
      'subCourse1B',
      'subCourse2A',
      'subCourse2B',
      'subCourse3A',
      'subCourse3B',
      'subCourse4A',
      'subCourse4B',
      'subCourse5A',
      'subCourse5B',
      'subCourse6A',
      'subCourse6B',
      'subCourse7A',
      'subCourse7B',
      'reqCourse0A',
      'reqCourse0B',
      'reqCourse1A',
      'reqCourse1B',
      'reqCourse2A',
      'reqCourse2B',
      'reqCourse3A',
      'reqCourse3B',
      'reqCourse4A',
      'reqCourse4B',
      'reqCourse5A',
      'reqCourse5B',
      'reqCourse6A',
      'reqCourse6B',
      'reqCourse7A',
      'reqCourse7B',
      'collegeDistinction0',
      'collegeDistinction1',
      'lowDivHours',
      'upDivHours',
      'currentEHRS',
      'lessDupCredit',
      'hoursTowardGraduation',
      'plusHoursOnAudit',
      'minReqHours',
      'UDReqSatisfied',
      'reqWaiver0',
      'reqWaiver1',
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
      'subCourse0A': 'Course Prefix/Number',
      'subCourse0B': 'Course Prefix/Number',
      'subCourse1A': '',
      'subCourse1B': '',
      'subCourse2A': '',
      'subCourse2B': '',
      'subCourse3A': '',
      'subCourse3B': '',
      'subCourse4A': '',
      'subCourse4B': '',
      'subCourse5A': '',
      'subCourse5B': '',
      'subCourse6A': '',
      'subCourse6B': '',
      'subCourse7A': '',
      'subCourse7B': '',
      'reqWaiver0': 'Course Prefix/Number',
      'reqWaiver1': 'Course Prefix/Number',
      'reqCourse0A': 'Course Prefix/Number',
      'reqCourse0B': 'Course Prefix/Number',
      'reqCourse1A': '',
      'reqCourse1B': '',
      'reqCourse2A': '',
      'reqCourse2B': '',
      'reqCourse3A': '',
      'reqCourse3B': '',
      'reqCourse4A': '',
      'reqCourse4B': '',
      'reqCourse5A': '',
      'reqCourse5B': '',
      'reqCourse6A': '',
      'reqCourse6B': '',
      'reqCourse7A': '',
      'reqCourse7B': '',
      'collegeDistinction0': '',
      'collegeDistinction1': '',
      'lowDivHours': '<strong>ELECTIVES</strong> (Lower Division, number of hours required)',
      'upDivHours': '<strong>ELECTIVES</strong> (Upper Division, number of hours required)',
      'currentEHRS': 'Current EHRS',
      'lessDupCredit': 'Less duplicate credit, repeats, excess PE',
      'hoursTowardGraduation': 'Hours toward graduation',
      'plusHoursOnAudit': 'Plus hours on audit',
      'minReqHours': 'Min. of req\'d hours for degree or minor',
      'UDReqSatisfied': '40 hour UD requirement satisfied',
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
            HTML('''<p class='my-2'>All substitutions for required courses and all waivers of
            degree requirements must receive the recommendation from the advisor,
            Department Head, and the Dean of your College.</p>'''),
            HTML("<h4 class='my-1'><strong>Requested Substitutions:</strong></h4>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('subCourse0A', css_class='col'),
                Div('subCourse0B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse1A', css_class='col'),
                Div('subCourse1B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse2A', css_class='col'),
                Div('subCourse2B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse3A', css_class='col'),
                Div('subCourse3B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse4A', css_class='col'),
                Div('subCourse4B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse5A', css_class='col'),
                Div('subCourse5B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse6A', css_class='col'),
                Div('subCourse6B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('subCourse7A', css_class='col'),
                Div('subCourse7B', css_class='col'),
            css_class='row pt-1'),
            HTML("<p class='mt-1 mb-0'><strong>Requested Waivers:</strong></p>"),
            Div(
                Div('reqWaiver0', css_class='col'),
                Div('reqWaiver1', css_class='col'),
            css_class='row'),
            HTML("<p class='my-1'><strong>College Distinction:</strong></p>"),
            Div(
                Div('collegeDistinction0', css_class='col'),
                Div('collegeDistinction1', css_class='col'),
            css_class='row pt-1'),
            HTML('''<p class='my-2'><strong>Listed below are all courses not completed and
                required to complete my degree, including
                correspondence and other off-campus classes.</strong></p>'''),
            HTML('''<p class='my-2'>Please list course numbers for <strong>required</strong> classes only.
                If electives are required, list the total hours of electives
                and whether lower or upper-level.</p>'''),
            HTML("<h4 class='my-1'><strong>Required Substitutions:</strong></h4>"),
            HTML("<hr class='solid my-1\'>"),
            Div(
                Div('reqCourse0A', css_class='col'),
                Div('reqCourse0B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse1A', css_class='col'),
                Div('reqCourse1B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse2A', css_class='col'),
                Div('reqCourse2B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse3A', css_class='col'),
                Div('reqCourse3B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse4A', css_class='col'),
                Div('reqCourse4B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse5A', css_class='col'),
                Div('reqCourse5B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse6A', css_class='col'),
                Div('reqCourse6B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('reqCourse7A', css_class='col'),
                Div('reqCourse7B', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('lowDivHours', css_class='col'),
                Div('upDivHours', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('currentEHRS', css_class='col'),
                Div('lessDupCredit', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('hoursTowardGraduation', css_class='col'),
                Div('plusHoursOnAudit', css_class='col'),
            css_class='row pt-1'),
            Div(
                Div('minReqHours', css_class='col'),
                Div('UDReqSatisfied', css_class='col'),
            css_class='row pt-1'),
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
      'atu_course_number1',
      'semester_taken1',
      'atu_course_prefix1B',
      'atu_course_num1B',
      'atu_course_prefix2',
      'atu_course_number2',
      'semester_taken2B',
      'atu_course_prefix2B',
      'atu_course_num2B',
      'atu_course_prefix3',
      'atu_course_number3',
      'semester_taken3B',
      'atu_course_prefix3B',
      'atu_course_num3B',
      'atu_course_prefix4',
      'atu_course_number4',
      'comments4',
      'atu_course_prefix5',
      'atu_course_number5',
      'comments5',
      'atu_course_prefix6',
      'atu_course_number6',
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
      'transfer_Institution': '',
      'course_subject': '',
      'course_num': '',
      'grade': '',
      'semester_taken': '',
      'atu_course_subject': '',
      'atu_course_num': '',
      'course_equivalent': '',
      'course_Substitution': '',
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
      'atu_course_number1':'Course Number',
      'semester_taken1':'Semester Taken',
      'atu_course_prefix1B':'Course Prefix',
      'atu_course_num1B':'Course Number',
      'atu_course_prefix2':'',
      'atu_course_number2':'',
      'semester_taken2B':'',
      'atu_course_prefix2B':'',
      'atu_course_num2B':'',
      'atu_course_prefix3':'',
      'atu_course_number3':'',
      'semester_taken3B':'',
      'atu_course_prefix3B':'',
      'atu_course_num3B':'',
      'atu_course_prefix4':'Course Prefix',
      'atu_course_number4':'Course Number',
      'comments4':'Comments',
      'atu_course_prefix5':'',
      'atu_course_number5':'',
      'comments5':'',
      'atu_course_prefix6':'',
      'atu_course_number6': '',
      'comments6': '',
      'college_distinction': '1.',
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
                Div('catalog_year', css_class='col-2'),
            css_class='row'),
            Div(
                Div('name_enrolled_under', css_class='col-8'),
                Div('major_was_chosen', css_class='col-2'),
                Div('change_grad_Term_to', css_class='col-2'),
            css_class='row'),
            HTML("<h6 class='my-1'>An <strong>EQUIVALENCY</strong> is a course you are requesting to be used as the same course required.</h6>"),
            HTML("<h6 class='my-1'>A <strong>SUBSTITUTION</strong> is a course you are requesting to be used <u>in place</u> of the course that is required.</h6>"),
            HTML("<h6 class='my-1'>A <strong>WAIVER</strong> is a course you are requesting the student not to complete.</h6>"),
            Div(css_class='row pt-2'),
            
         Div(
            HTML("<h6 class ='col-2'>Transfer Institution</h6>"),
            HTML("<h6 class ='col-1'>Course Subject</h6>"),
            HTML("<h6 class ='col-1'>Course Number</h6>"),
            HTML("<h6 class ='col-1'>Grade</h6>"),
            HTML("<h6 class ='col-1'>Semester Taken</h6>"),
            HTML("<h6 class ='col-1'>ATU Course Subject</h6>"),
            HTML("<h6 class ='col-1'>ATU Course Number</h6>"),
            HTML("<h6 class ='col-2'>Course Equivalent</h6>"),
            HTML("<h6 class ='col-2'>Course Substitution</h6>"),
            css_class = 'row'),
            Div(
                Div('transfer_Institution',css_class='col-2'),
                Div('course_subject',css_class='col-1'),
                Div('course_num',css_class='col-1'),
                Div('grade',css_class='col-1'),
                Div('semester_taken',css_class = 'col-1'),
                Div('atu_course_subject',css_class = 'col-1'),
                Div('atu_course_num',css_class = 'col-1'),
                Div('course_equivalent',css_class = 'col-2'),
                Div('course_Substitution',css_class = 'col-2'),
            css_class='row pt-1'),
            Div(
                Div('transfer_Institution2',css_class='col-2'),
                Div('course_subject2',css_class='col-1'),
                Div('course_num2',css_class='col-1'),
                Div('grade2',css_class='col-1'),
                Div('semester_taken2',css_class = 'col-1'),
                Div('atu_course_subject2',css_class = 'col-1'),
                Div('atu_course_num2',css_class = 'col-1'),
                Div('course_equivalent2',css_class = 'col-2'),
                Div('course_Substitution2',css_class = 'col-2'),
            css_class='row pt-1'),
            Div(
                Div('transfer_Institution3',css_class='col-2'),
                Div('course_subject3',css_class='col-1'),
                Div('course_num3',css_class='col-1'),
                Div('grade3',css_class='col-1'),
                Div('semester_taken3',css_class = 'col-1'),
                Div('atu_course_subject3',css_class = 'col-1'),
                Div('atu_course_num3',css_class = 'col-1'),
                Div('course_equivalent3',css_class = 'col-2'),
                Div('course_Substitution3',css_class = 'col-2'),
            css_class='row pt-1'),
            Div(
                Div('transfer_Institution4',css_class='col-2'),
                Div('course_subject4',css_class='col-1'),
                Div('course_num4',css_class='col-1'),
                Div('grade4',css_class='col-1'),
                Div('semester_taken4',css_class = 'col-1'),
                Div('atu_course_subject4',css_class = 'col-1'),
                Div('atu_course_num4',css_class = 'col-1'),
                Div('course_equivalent4',css_class = 'col-2'),
                Div('course_Substitution4',css_class = 'col-2'),
            css_class='row pt-1'),
            Div(
                Div('transfer_Institution5',css_class='col-2'),
                Div('course_subject5',css_class='col-1'),
                Div('course_num5',css_class='col-1'),
                Div('grade5',css_class='col-1'),
                Div('semester_taken5',css_class = 'col-1'),
                Div('atu_course_subject5',css_class = 'col-1'),
                Div('atu_course_num5',css_class = 'col-1'),
                Div('course_equivalent5',css_class = 'col-2'),
                Div('course_Substitution5',css_class = 'col-2'),
            css_class='row pt-1'),
            HTML("<h6>I understand that if taken at another college/university, official transcripts for the above course(s) must be on file in the Registrar's Office by.</h6>"),
            HTML("<h6>the date Arkansas Tech University final grades are due. It is my responsibility to see that this requirement is met by the deadline, or my.</h6>"),
            HTML("<h6>graduation will be postponed to the next term. I am also aware of the Grading Policy and Graduation Requirements as put forth in the Catalog.</h6>"),
            
            Div(css_class='row pt-3'),
            
            Div(
                HTML(" <class = 'row'>Please substitute following <strong><u>ARKANSAS TECH UNIVERSITY</u></strong> course(s):</h6>"),
                css_class='row' 
            ),
            
            Div( 
                HTML("<h6 class ='col-7'>SUBSTITUTE THESE ATU COURSES:</h6>"),
                HTML("<h6 class ='col-4'>FOR THESE ATU COURSES:</h6>"),
                css_class = 'row pt-3'),
        
            Div(
                Div('atu_course_prefix1',css_class='col-2'),
                Div('atu_course_number1',css_class='col-2'),
                Div('semester_taken1',css_class='col-2'),
                Div(css_class = 'col-1'),
                Div('atu_course_prefix1B',css_class='col-2'),
                Div('atu_course_num1B',css_class='col-2'),
            css_class='row pt-2'),
            Div(
                Div('atu_course_prefix2',css_class = 'col-2'),
                Div('atu_course_number2',css_class = 'col-2'),
                Div('semester_taken2B',css_class = 'col-2'),
                Div(css_class = 'col-1'),
                Div('atu_course_prefix2B',css_class = 'col-2'),
                Div('atu_course_num2B',css_class = 'col-2'),
            css_class='row pt-1'),
            
            Div(
                Div('atu_course_prefix3',css_class = 'col-2'),
                Div('atu_course_number3',css_class = 'col-2'),
                Div('semester_taken3B',css_class = 'col-2'),
                Div(css_class = 'col-1'),
                Div('atu_course_prefix3B',css_class = 'col-2'),
                Div('atu_course_num3B',css_class = 'col-2'),
            css_class='row pt-1'),
            Div( 
                HTML("<h6 class ='col-7'>Please waive the following course requirement(s):</h6>"),
                css_class = 'row pt-3'),
            Div(
                Div('atu_course_prefix4',css_class='col-3'),
                Div('atu_course_number4',css_class='col-3'),
                Div('comments4',css_class='col-5'),
            css_class='row pt-2'),
            Div(
                Div('atu_course_prefix5',css_class = 'col-3'),
                Div('atu_course_number5',css_class = 'col-3'),
                Div('comments5',css_class = 'col-5'),
            css_class='row pt-1'),
            Div(
                Div('atu_course_prefix6',css_class = 'col-3'),
                Div('atu_course_number6',css_class = 'col-3'),
                Div('comments6',css_class = 'col-5'),
            css_class='row pt-1'),
            
            Div(
                HTML("<h6> College Distinction </h6>"),
                Div('college_distinction',css_class = 'col-2'),
                Div('college_distinction2',css_class = 'col-2'),
                css_class='row pt-5'),
            Div(
                Div('comments',css_class = 'col-8'),
                Div('date',css_class='col-2'),
                css_class='row pt-5'),
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
