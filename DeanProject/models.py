from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  tech_id = models.CharField(max_length=9, default="")
  name = models.CharField(max_length=20, default="Person")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

class permitToRegister(models.Model):

  class Meta:
    verbose_name = "Permit to Register"

  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  registration_semester = models.CharField(max_length=10)
  registration_year = models.DecimalField(decimal_places = 0, max_digits=4)
  comments = models.TextField(max_length=100)
  total_hours_enrolled = models.DecimalField(decimal_places = 0, max_digits=2)
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
  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

class add_dropClass(models.Model):

  class Meta:
    verbose_name = "Add/Drop Class"

  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  recieves_financial_aid = models.BooleanField() #Yes/No
  #Add Drop table would go here
  total_hours_enrolled_after_change = models.DecimalField(decimal_places = 0, max_digits=2)
  comments = models.TextField(max_length=100)
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
  dropCRN0 = models.CharField(max_length=10, blank=True)
  dropCRN1 = models.CharField(max_length=10, blank=True)
  dropCRN2 = models.CharField(max_length=10, blank=True)
  dropCRN3 = models.CharField(max_length=10, blank=True)
  dropCRN4 = models.CharField(max_length=10, blank=True)
  dropCRN5 = models.CharField(max_length=10, blank=True)
  addCRN0 = models.CharField(max_length=10, blank=True)
  addCRN1 = models.CharField(max_length=10, blank=True)
  addCRN2 = models.CharField(max_length=10, blank=True)
  addCRN3 = models.CharField(max_length=10, blank=True)
  addCRN4 = models.CharField(max_length=10, blank=True)
  addCRN5 = models.CharField(max_length=10, blank=True)
  dropPrefix0 = models.CharField(max_length=10, blank=True)
  dropPrefix1 = models.CharField(max_length=10, blank=True)
  dropPrefix2 = models.CharField(max_length=10, blank=True)
  dropPrefix3 = models.CharField(max_length=10, blank=True)
  dropPrefix4 = models.CharField(max_length=10, blank=True)
  dropPrefix5 = models.CharField(max_length=10, blank=True)
  addPrefix0 = models.CharField(max_length=10, blank=True)
  addPrefix1 = models.CharField(max_length=10, blank=True)
  addPrefix2 = models.CharField(max_length=10, blank=True)
  addPrefix3 = models.CharField(max_length=10, blank=True)
  addPrefix4 = models.CharField(max_length=10, blank=True)
  addPrefix5 = models.CharField(max_length=10, blank=True)
  dropCourseNum0 = models.CharField(max_length=10, blank=True)
  dropCourseNum1 = models.CharField(max_length=10, blank=True)
  dropCourseNum2 = models.CharField(max_length=10, blank=True)
  dropCourseNum3 = models.CharField(max_length=10, blank=True)
  dropCourseNum4 = models.CharField(max_length=10, blank=True)
  dropCourseNum5 = models.CharField(max_length=10, blank=True)
  addCourseNum0 = models.CharField(max_length=10, blank=True)
  addCourseNum1 = models.CharField(max_length=10, blank=True)
  addCourseNum2 = models.CharField(max_length=10, blank=True)
  addCourseNum3 = models.CharField(max_length=10, blank=True)
  addCourseNum4 = models.CharField(max_length=10, blank=True)
  addCourseNum5 = models.CharField(max_length=10, blank=True)
  dropSecNo0 = models.CharField(max_length=10, blank=True)
  dropSecNo1 = models.CharField(max_length=10, blank=True)
  dropSecNo2 = models.CharField(max_length=10, blank=True)
  dropSecNo3 = models.CharField(max_length=10, blank=True)
  dropSecNo4 = models.CharField(max_length=10, blank=True)
  dropSecNo5 = models.CharField(max_length=10, blank=True)
  addSecNo0 = models.CharField(max_length=10, blank=True)
  addSecNo1 = models.CharField(max_length=10, blank=True)
  addSecNo2 = models.CharField(max_length=10, blank=True)
  addSecNo3 = models.CharField(max_length=10, blank=True)
  addSecNo4 = models.CharField(max_length=10, blank=True)
  addSecNo5 = models.CharField(max_length=10, blank=True)
  dropDidAttend0 = models.BooleanField()
  dropDidAttend1 = models.BooleanField()
  dropDidAttend2 = models.BooleanField()
  dropDidAttend3 = models.BooleanField()
  dropDidAttend4 = models.BooleanField()
  dropDidAttend5 = models.BooleanField()
  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

class UGGraduation(models.Model):

  class Meta:
    verbose_name = "Undergraduate Graduation"

  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=20)
  diploma_name = models.CharField(max_length=50)
  name_pronunciation = models.CharField(max_length=50)
  pronunciation_recorded = models.BooleanField() #Weird
  parents_completed_bachelor_degree = models.BooleanField() #Yes/No
  expected_graduation_term = models.CharField(max_length=6, choices=SEASON_CHOICES)
  expected_graduation_year = models.DecimalField(decimal_places = 0, max_digits=4)
  #Catalog table would go here
  preferred_degree = models.CharField(max_length=100)
  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

class masterGraduation(models.Model):

  class Meta:
    verbose_name = "Master's Graduation"

  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  mailing_address = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2, choices=US_STATE_CHOICES)
  zip_code = models.DecimalField(decimal_places = 0, max_digits=5)
  phone_number = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  student_starting_semester = models.CharField(max_length=6, choices=SEASON_CHOICES)
  student_starting_year = models.DecimalField(decimal_places = 0, max_digits=4)
  diploma_name = models.CharField(max_length=50)
  name_pronunciation = models.CharField(max_length=50)
  expected_graduation_term = models.CharField(max_length=6, choices=SEASON_CHOICES)
  expected_graduation_year = models.DecimalField(decimal_places = 0, max_digits=4)
  degree_name = models.CharField(max_length=100) #In reality this would be a dropdown
  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

class degreeAudit(models.Model):

  class Meta:
    verbose_name = "Degree Audit"

  student_id_number = models.CharField(max_length=10)
  date = models.DateField(default = '')
  catalog_year = models.DecimalField(decimal_places = 0, max_digits=4)
  name_enrolled_under = models.CharField(max_length=50)
  major_or_minor_name = models.CharField(max_length=100)
  major_was_chosen = models.BooleanField()
  minor_was_chosen = models.BooleanField()
  semester = models.CharField(max_length=6, choices=SEASON_CHOICES)
  year = models.DecimalField(decimal_places = 0, max_digits=4)
  subCourse0A = models.CharField(max_length=15, blank=True)
  subCourse0B = models.CharField(max_length=15, blank=True)
  subCourse1A = models.CharField(max_length=15, blank=True)
  subCourse1B = models.CharField(max_length=15, blank=True)
  subCourse2A = models.CharField(max_length=15, blank=True)
  subCourse2B = models.CharField(max_length=15, blank=True)
  subCourse3A = models.CharField(max_length=15, blank=True)
  subCourse3B = models.CharField(max_length=15, blank=True)
  subCourse4A = models.CharField(max_length=15, blank=True)
  subCourse4B = models.CharField(max_length=15, blank=True)
  subCourse5A = models.CharField(max_length=15, blank=True)
  subCourse5B = models.CharField(max_length=15, blank=True)
  subCourse6A = models.CharField(max_length=15, blank=True)
  subCourse6B = models.CharField(max_length=15, blank=True)
  subCourse7A = models.CharField(max_length=15, blank=True)
  subCourse7B = models.CharField(max_length=15, blank=True)
  reqWaiver0 = models.CharField(max_length=10, blank=True)
  reqWaiver1 = models.CharField(max_length=10, blank=True)
  collegeDistinction0 = models.CharField(max_length=15, blank=True)
  collegeDistinction1 = models.CharField(max_length=15, blank=True)
  reqCourse0A = models.CharField(max_length=15, blank=True)
  reqCourse0B = models.CharField(max_length=15, blank=True)
  reqCourse1A = models.CharField(max_length=15, blank=True)
  reqCourse1B = models.CharField(max_length=15, blank=True)
  reqCourse2A = models.CharField(max_length=15, blank=True)
  reqCourse2B = models.CharField(max_length=15, blank=True)
  reqCourse3A = models.CharField(max_length=15, blank=True)
  reqCourse3B = models.CharField(max_length=15, blank=True)
  reqCourse4A = models.CharField(max_length=15, blank=True)
  reqCourse4B = models.CharField(max_length=15, blank=True)
  reqCourse5A = models.CharField(max_length=15, blank=True)
  reqCourse5B = models.CharField(max_length=15, blank=True)
  reqCourse6A = models.CharField(max_length=15, blank=True)
  reqCourse6B = models.CharField(max_length=15, blank=True)
  reqCourse7A = models.CharField(max_length=15, blank=True)
  reqCourse7B = models.CharField(max_length=15, blank=True)
  lowDivHours = models.DecimalField(decimal_places = 0, max_digits=2, blank=True)
  upDivHours = models.DecimalField(decimal_places = 0, max_digits=2, blank=True)
  currentEHRS = models.CharField(max_length=5, blank=True)
  lessDupCredit = models.CharField(max_length=5, blank=True)
  hoursTowardGraduation = models.CharField(max_length=5, blank=True)
  plusHoursOnAudit = models.CharField(max_length=5, blank=True)
  minReqHours = models.CharField(max_length=5, blank=True)
  UDReqSatisfied = models.CharField(max_length=5, blank=True)
  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

class degreeAuditAmendmentRequest(models.Model):
    
  class Meta:
    verbose_name = "Degree Audit Amendment Request"

  student_id_number = models.CharField(max_length=10)
  catalog_year = models.DecimalField(decimal_places = 0, max_digits=4)
  date = models.DateField(default = '')
  name_enrolled_under = models.CharField(max_length=50)
  major_was_chosen = models.CharField(max_length=50)
  change_grad_Term_to = models.CharField(max_length = 50, blank = True)
  transfer_Institution = models.CharField(max_length = 100, blank = True)
  course_subject = models.CharField(max_length = 50, blank = True)
  course_num = models.CharField(max_length=10, blank=True)
  grade = models.CharField(max_length = 5, blank = True)
  semester_taken = models.CharField(max_length = 50, blank = True)
  atu_course_subject = models.CharField(max_length = 50, blank = True)
  atu_course_num = models.CharField(max_length=10, blank=True)
  course_equivalent = models.BooleanField(blank = True)
  course_Substitution = models.BooleanField(blank = True)

  transfer_Institution2 = models.CharField(max_length = 100, blank = True)
  course_subject2 = models.CharField(max_length = 50, blank = True)
  course_num2 = models.CharField(max_length=10, blank=True)
  grade2 = models.CharField(max_length = 5, blank = True)
  semester_taken2 = models.CharField(max_length = 50, blank = True)
  atu_course_subject2 = models.CharField(max_length = 50, blank = True)
  atu_course_num2 = models.CharField(max_length=10, blank=True)
  course_equivalent2 = models.BooleanField(blank = True)
  course_Substitution2 = models.BooleanField(blank = True)

  transfer_Institution3 = models.CharField(max_length = 100, blank = True)
  course_subject3 = models.CharField(max_length = 50, blank = True)
  course_num3 = models.CharField(max_length=10, blank=True)
  grade3 = models.CharField(max_length = 5, blank = True)
  semester_taken3 = models.CharField(max_length = 50, blank = True)
  atu_course_subject3 = models.CharField(max_length = 50, blank = True)
  atu_course_num3 = models.CharField(max_length=10, blank=True)
  course_equivalent3 = models.BooleanField(blank = True)
  course_Substitution3 = models.BooleanField(blank = True)

  transfer_Institution4 = models.CharField(max_length = 100, blank = True)
  course_subject4 = models.CharField(max_length = 50, blank = True)
  course_num4 = models.CharField(max_length=10, blank=True)
  grade4 = models.CharField(max_length = 5, blank = True)
  semester_taken4 = models.CharField(max_length = 50, blank = True)
  atu_course_subject4 = models.CharField(max_length = 50, blank = True)
  atu_course_num4 = models.CharField(max_length=10, blank=True)
  course_equivalent4 = models.BooleanField(blank = True)
  course_Substitution4 = models.BooleanField(blank = True)

  transfer_Institution5 = models.CharField(max_length = 100, blank = True)
  course_subject5 = models.CharField(max_length = 50, blank = True)
  course_num5 = models.CharField(max_length=10, blank=True)
  grade5 = models.CharField(max_length = 5, blank = True)
  semester_taken5 = models.CharField(max_length = 50, blank = True)
  atu_course_subject5 = models.CharField(max_length = 50, blank = True)
  atu_course_num5 = models.CharField(max_length=10, blank=True)
  course_equivalent5 = models.BooleanField(blank = True)
  course_Substitution5 = models.BooleanField(blank = True)

  atu_course_prefix1 = models.CharField(max_length = 50, blank = True)
  atu_course_number1 = models.CharField(max_length=10, blank=True)
  semester_taken1 = models.CharField(max_length = 50, blank = True)
  atu_course_prefix1B = models.CharField(max_length = 50, blank = True)
  atu_course_num1B = models.CharField(max_length=10, blank=True)

  atu_course_prefix2 = models.CharField(max_length = 50, blank = True)
  atu_course_number2 = models.CharField(max_length=10, blank=True)
  semester_taken2B = models.CharField(max_length = 50, blank = True, null = True)
  atu_course_prefix2B = models.CharField(max_length = 50, blank = True)
  atu_course_num2B = models.CharField(max_length=10, blank=True)

  atu_course_prefix3 = models.CharField(max_length = 50, blank = True)
  atu_course_number3 = models.CharField(max_length=10, blank=True)
  semester_taken3B = models.CharField(max_length = 50, blank = True, null = True)
  atu_course_prefix3B = models.CharField(max_length = 50, blank = True)
  atu_course_num3B = models.CharField(max_length=10, blank=True)

  atu_course_prefix4 = models.CharField(max_length = 50, blank = True)
  atu_course_number4 = models.CharField(max_length=10, blank=True)
  comments4 = models.CharField(max_length=100, blank = True)
  atu_course_prefix5 = models.CharField(max_length = 50, blank = True)
  atu_course_number5 = models.CharField(max_length=10, blank=True)
  comments5 = models.CharField(max_length=100, blank = True)

  atu_course_prefix6 = models.CharField(max_length = 50, blank = True)
  atu_course_number6 = models.CharField(max_length=10, blank=True)
  comments6 = models.CharField(max_length=100, blank = True)
  college_distinction = models.CharField(max_length = 50, blank = True)
  college_distinction2 = models.CharField(max_length = 50, blank = True)
  comments = models.TextField(max_length=100, blank = True)

  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

class transcriptRequest(models.Model):
  class Meta:
    verbose_name = "Transcript Request"

  student_id_number = models.CharField(max_length=10)
  date = models.DateField()
  name_enrolled_under = models.CharField(max_length=50)
  birth_date = models.DateField()
  mailing_address = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2, choices=US_STATE_CHOICES)
  zip_code = models.DecimalField(decimal_places = 0, max_digits=5)
  phone_number = models.CharField(max_length=20)
  adhe = models.BooleanField()
  sacm = models.BooleanField()
  embassy_of_kuwait = models.BooleanField()
  ade_licensure = models.BooleanField()
  arsbn = models.BooleanField()
  #Tables need to be added
  isPending = models.BooleanField(default=True)
  isApproved = models.BooleanField(default=False)
  isDenied = models.BooleanField(default=False)

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
