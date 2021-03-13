from django import forms

class permitToRegister(forms.Form):
  student_id_number = forms.CharField(label="TNumber", max_length=10)
  date = forms.DateField(label="Date")
  name_enrolled_under = forms.CharField(label="Name Enrolled Under (Last, First, Middle, Other)", max_length=50)
  registration_season = "hjdaski"
#The class for the undergraduate graduation form.

class UGGraduation(forms.Form):
  student_id_number = forms.CharField(label="TNumber", max_length=10)
  date = forms.DateField()
  name_enrolled_under = forms.CharField(label="Name Enrolled Under (Last, Your mom, Middle, Other)", max_length=50)
  phone_number = forms.CharField(label="Phone Number", max_length=20)
  diploma_name = forms.CharField(label="Print Your Name Exactly As You Want It To Appear On Your Diploma", max_length=100)
  name_pronunciation = forms.CharField(label="Name Pronounciation", max_length=100)
  #TODO: need to add parent bachelor degree, term completed, catalog, major, and minor

class add_dropClass(forms.Form):
  student_id_number = forms.CharField(label="TNumber", max_length=10)
  date = forms.DateField(label="Date")
  name_enrolled_under = forms.CharField(label="Name Enrolled Under (Last, First, Middle, Other)", max_length=50)
  recieves_financial_aid = forms.BooleanField(label="Do you receive financial aid (loans, grants, scholarships)?")

# class masterGraduation(django.forms.Form):

# class degreeAudit(django.forms.Form):

# class transcriptRequest(django.forms.Form):