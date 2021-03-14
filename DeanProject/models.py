from django.db import models

US_STATE_CHOICES = (
    ('ar','AR'), ('aa','AA'), ('ae','AE'), ('ak','AK'), ('al','AL'),
    ('ap','AP'), ('as','AS'), ('az','AZ'), ('ca','CA'), ('co','CO'),
    ('ct','CT'), ('de','DE'), ('dc','DC'), ('fl','FL'), ('ga','GA'),
    ('gu','GU'), ('hi','HI'), ('id','ID'), ('il','IL'), ('in','IN'),
    ('ia','IA'), ('ks','KS'), ('ky','KY'), ('la','LA'), ('me','ME'),
    ('md','MD'), ('ma','MA'), ('mi','MI'), ('mn','MN'), ('ms','MS'),
    ('mo','MO'), ('mt','MT'), ('ne','NE'), ('nv','NV'), ('nh','NH'),
    ('nj','NJ'), ('nm','NM'), ('ny','NY'), ('nc','NC'), ('nd','ND'),
    ('mp','MP'), ('oh','OH'), ('ok','OK'), ('or','OR'), ('pa','PA'),
    ('pr','PR'), ('ri','RI'), ('sc','SC'), ('sd','SD'), ('tn','TN'),
    ('tx','TX'), ('ut','UT'), ('vt','VT'), ('va','VA'), ('vi','VI'),
    ('wa','WA'), ('wv','WV'), ('wi','WI'), ('wy','WY'),
)

SEASON_CHOICES = (
    ('spring', 'Spring'),
    ('summer', 'Summer'),
    ('fall', 'Fall'),
    ('winter', 'Winter'),
)

class permitToRegister(models.Model):
  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  registration_semester = models.CharField(max_length=10)
  registration_year = models.DecimalField(decimal_places = 0, max_digits=4)
  #Still Needs Work

class add_dropClass(models.Model):
  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  recieves_financial_aid = models.BooleanField() #Yes/No
  financial_aid_representative_signature = models.CharField(max_length=50) #Signature
  #Still Needs Work

class UGGraduation(models.Model):
  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=20)
  student_signature = models.CharField(max_length=50) #Signature
  diploma_name = models.CharField(max_length=50)
  name_pronunciation = models.CharField(max_length=50)
  pronunciation_recorded = models.BooleanField() #Weird
  parents_completed_bachelor_degree = models.BooleanField() #Yes/No
  expected_graduation_term = models.CharField(max_length=6, choices=SEASON_CHOICES)
  expected_graduation_year = models.DecimalField(decimal_places = 0, max_digits=4)
  #Still Needs Work


class masterGraduation(models.Model):
  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  mailing_address = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2, choices=US_STATE_CHOICES)
  zip_code = models.DecimalField(decimal_places = 0, max_digits=5)
  phone_number = models.DecimalField(decimal_places = 0, max_digits=9)
  email = models.CharField(max_length=50)
  student_starting_semester = models.CharField(max_length=6, choices=SEASON_CHOICES)
  student_starting_year = models.DecimalField(decimal_places = 0, max_digits=4)
  diploma_name = models.CharField(max_length=50)
  name_pronunciation = models.CharField(max_length=50)
  expected_graduation_term = models.CharField(max_length=6, choices=SEASON_CHOICES)
  expected_graduation_year = models.DecimalField(decimal_places = 0, max_digits=4)
  degree_name = models.CharField(max_length=100) #In reality this would be a dropdown

class degreeAudit(models.Model):
  student_id_number = models.CharField(max_length=10)
  catalog_year = models.DecimalField(decimal_places = 0, max_digits=4)
  name_enrolled_under = models.CharField(max_length=50)
  major_or_minor_name = models.CharField(max_length=100)
  major_was_chosen = models.BooleanField()
  minor_was_chosen = models.BooleanField()
  semester = models.CharField(max_length=6, choices=SEASON_CHOICES)
  year = models.DecimalField(decimal_places = 0, max_digits=4)
  #Still Needs Work

class transcriptRequest(models.Model):
  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  birth_date = models.DateField()
  mailing_address = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2, choices=US_STATE_CHOICES)
  zip_code = models.DecimalField(decimal_places = 0, max_digits=5)
  phone_number = models.DecimalField(decimal_places = 0, max_digits=9)
  student_signature = models.CharField(max_length=50) #Signature
  adhe = models.BooleanField()
  sacm = models.BooleanField()
  embassy_of_kuwait = models.BooleanField()
  ade_licensure = models.BooleanField()
  arsbn = models.BooleanField()
  #Still Needs Work