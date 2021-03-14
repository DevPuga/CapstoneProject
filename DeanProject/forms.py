from django import forms
from .models import permitToRegister, add_dropClass, UGGraduation, masterGraduation, degreeAudit, transcriptRequest

class permitToRegisterForm(forms.ModelForm):
  class Meta:
    model = permitToRegister
    fields = [
      'student_id_number',
      'date',
      'name_enrolled_under',
      'registration_semester',
      'registration_year',
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'registration_semester': 'Registration Semester',
      'registration_year': 'Registration Year',
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
    ]
    labels = {
      'student_id_number': 'T Number',
      'date': 'Date',
      'name_enrolled_under': 'Name Enrolled Under (Last, First, Middle, Other)',
      'recieves_financial_aid': 'Do you receive financial aid? (loans, grants, scholarships)', #Yes/No
      'financial_aid_representative_signature': 'Financial Aid Representative Signature', #Signature
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
    }

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