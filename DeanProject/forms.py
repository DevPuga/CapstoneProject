from django import forms

#The class for the undergraduate graduation form.
class UGGraduation(forms.Form):
  student_id_number = forms.CharField(label="TNumber", max_length=10)
  date = forms.DateField()
  student_first_name = forms.CharField(label="First Name", max_length=50)
  student_last_name = forms.CharField(label="Last Name", max_length=50)
  phone_number = forms.CharField(label="Phone Number", max_length=20)
  diploma_name = forms.CharField(label="Print Your Name Exactly As You Want It To Appear On Your Diploma", max_length=100)
  name_pronunciation = forms.CharField(label="Name Pronounciation", max_length=100)
  #TODO: need to add parent bachelor degree, term completed, catalog, major, and minor
