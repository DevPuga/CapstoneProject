from django.db import models

US_STATE_CHOICES = (
    ('ar','AR'), ('aa','AA'), ('ae','AE'), ('ak','AK'), ('al','AL'),
    ('ap','AP'), ('as','AS'), ('az','AZ'), ('ca','CA'), ('co','CO'),
    ('ct','CT'), ('dc','DC'), ('de','DE'), ('fl','FL'), ('ga','GA'),
    ('gu','GU'), ('hi','HI'), ('ia','IA'), ('id','ID'), ('il','IL'),
    ('in','IN'), ('ks','KS'), ('ky','KY'), ('la','LA'), ('ma','MA'),
    ('md','MD'), ('me','ME'), ('mi','MI'), ('mn','MN'), ('mo','MO'),
    ('mp','MP'), ('ms','MS'), ('mt','MT'), ('nc','NC'), ('nd','ND'),
    ('ne','NE'), ('nh','NH'), ('nj','NJ'), ('nm','NM'), ('nv','NV'),
    ('ny','NY'), ('oh','OH'), ('ok','OK'), ('or','OR'), ('pa','PA'),
    ('pr','PR'), ('ri','RI'), ('sc','SC'), ('sd','SD'), ('tn','TN'),
    ('tx','TX'), ('ut','UT'), ('va','VA'), ('vi','VI'), ('vt','VT'),
    ('wa','WA'), ('wi','WI'), ('wv','WV'), ('wy','WY'),
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
  #Course Table would go here
  comments = models.TextField(max_length=100)
  total_hours_enrolled = models.DecimalField(decimal_places = 0, max_digits=2)
  dean_signature = models.CharField(max_length=50) #Signature
  advisor_signature = models.CharField(max_length=50) #Signature
  student_signature = models.CharField(max_length=50) #Signature
  crn0 = models.CharField(max_length=10, blank=True)
  crn1 = models.CharField(max_length=10, blank=True)
  crn2 = models.CharField(max_length=10, blank=True)
  crn3 = models.CharField(max_length=10, blank=True)
  crn4 = models.CharField(max_length=10, blank=True)
  crn5 = models.CharField(max_length=10, blank=True)
  crn6 = models.CharField(max_length=10, blank=True)
  crn7 = models.CharField(max_length=10, blank=True)
  crn8 = models.CharField(max_length=10, blank=True)
  prefix0 = models.CharField(max_length=10, blank=True)
  prefix1 = models.CharField(max_length=10, blank=True)
  prefix2 = models.CharField(max_length=10, blank=True)
  prefix3 = models.CharField(max_length=10, blank=True)
  prefix4 = models.CharField(max_length=10, blank=True)
  prefix5 = models.CharField(max_length=10, blank=True)
  prefix6 = models.CharField(max_length=10, blank=True)
  prefix7 = models.CharField(max_length=10, blank=True)
  prefix8 = models.CharField(max_length=10, blank=True)
  courseNum0 = models.CharField(max_length=10, blank=True)
  courseNum1 = models.CharField(max_length=10, blank=True)
  courseNum2 = models.CharField(max_length=10, blank=True)
  courseNum3 = models.CharField(max_length=10, blank=True)
  courseNum4 = models.CharField(max_length=10, blank=True)
  courseNum5 = models.CharField(max_length=10, blank=True)
  courseNum6 = models.CharField(max_length=10, blank=True)
  courseNum7 = models.CharField(max_length=10, blank=True)
  courseNum8 = models.CharField(max_length=10, blank=True)
  secNo0 = models.CharField(max_length=10, blank=True)
  secNo1 = models.CharField(max_length=10, blank=True)
  secNo2 = models.CharField(max_length=10, blank=True)
  secNo3 = models.CharField(max_length=10, blank=True)
  secNo4 = models.CharField(max_length=10, blank=True)
  secNo5 = models.CharField(max_length=10, blank=True)
  secNo6 = models.CharField(max_length=10, blank=True)
  secNo7 = models.CharField(max_length=10, blank=True)
  secNo8 = models.CharField(max_length=10, blank=True)


class add_dropClass(models.Model):
  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  recieves_financial_aid = models.BooleanField() #Yes/No
  financial_aid_representative_signature = models.CharField(max_length=50) #Signature
  #Add Drop table would go here
  total_hours_enrolled_after_change = models.DecimalField(decimal_places = 0, max_digits=2)
  comments = models.TextField(max_length=100)
  advisor_signature = models.CharField(max_length=50) #Signature
  student_signature = models.CharField(max_length=50) #Signature
  atu_comments = models.TextField(max_length=100)
  #Section: Academic Issues
  another_course_fits_schedule = models.BooleanField()
  changing_major = models.BooleanField()
  changing_minor = models.BooleanField()
  classes_too_large = models.BooleanField()
  could_not_understand_the_instructor_course_or_materials = models.BooleanField()
  course_not_required_for_major = models.BooleanField()
  inadequate_academic_support_services  = models.BooleanField()
  insufficient_high_school_preparation = models.BooleanField()
  lack_of_academic_challenge = models.BooleanField()
  lack_of_progress_in_the_courses = models.BooleanField()
  need_to_re_enroll_in_classes_next_semester = models.BooleanField()
  need_to_re_enroll_in_classes_with_different_instructor = models.BooleanField()
  quality_of_instruction_did_not_meet_expections = models.BooleanField()
  reduce_course_load = models.BooleanField()
  wanted_classes_face_to_face = models.BooleanField()
  wanted_classes_online = models.BooleanField()
  #Section: Financial Issues
  change_in_family_financial_circumstances = models.BooleanField()
  didnt_have_enough_money_to_continue= models.BooleanField()
  financial_aid_was_not_sufficient = models.BooleanField()
  increases_in_tuition_and_fees = models.BooleanField()
  incurred_too_much_debt = models.BooleanField()
  needed_Course_for_financial_aid_eligibility = models.BooleanField()
  scholarship_Grant_was_not_renewed = models.BooleanField()
  #Section: Family Issues
  family_illness_responsibility = models.BooleanField()
  homesick = models.BooleanField()
  wanted_to_be_closer_to_family_and_friends = models.BooleanField()
  #Section: Housing and Travel Issues
  commute_too_long = models.BooleanField()
  moved_out_of_the_area = models.BooleanField()
  #Section: Personal and Transition Issues
  distracted_Social_life = models.BooleanField()
  felt_class_climate_unwelcoming = models.BooleanField()
  felt_out_of_place_in_class = models.BooleanField()
  impact_of_natural_disaster = models.BooleanField()
  inadequate_study_skills_or_lack_of_academic_success = models.BooleanField()
  military_obligations = models.BooleanField()
  personal_health = models.BooleanField()
  personal_emergency = models.BooleanField()
  unmotivated_for_this_courses_or_tired_of_school = models.BooleanField()
  working_too_many_hours = models.BooleanField()

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
  #Catalog table would go here
  preferred_degree = models.CharField(max_length=100)

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
  #Tables need to be added

class courseInfo(models.Model): #WIP (not WAP)
  crn = models.DecimalField(decimal_places=0, max_digits=5)
  course_prefix = models.CharField(max_length=4)
  course_number = models.DecimalField(decimal_places=0, max_digits=4)
  sec_no = models.CharField(max_length=3)

class substitutionRequest(models.Model): #WIP (not WAP)
  current_course = models.CharField(max_length=50)
  requested_course = models.CharField(max_length=50)

class empty(models.Model):
    empty = models.BooleanField()
