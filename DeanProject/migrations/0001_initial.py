# Generated by Django 3.1.7 on 2021-04-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_dropClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('name_enrolled_under', models.CharField(max_length=50)),
                ('recieves_financial_aid', models.BooleanField()),
                ('financial_aid_representative_signature', models.CharField(max_length=50)),
                ('total_hours_enrolled_after_change', models.DecimalField(decimal_places=0, max_digits=2)),
                ('comments', models.TextField(max_length=100)),
                ('advisor_signature', models.CharField(max_length=50)),
                ('student_signature', models.CharField(max_length=50)),
                ('atu_comments', models.TextField(max_length=100)),
                ('another_course_fits_schedule', models.BooleanField()),
                ('changing_major', models.BooleanField()),
                ('changing_minor', models.BooleanField()),
                ('classes_too_large', models.BooleanField()),
                ('could_not_understand_the_instructor_course_or_materials', models.BooleanField()),
                ('course_not_required_for_major', models.BooleanField()),
                ('inadequate_academic_support_services', models.BooleanField()),
                ('insufficient_high_school_preparation', models.BooleanField()),
                ('lack_of_academic_challenge', models.BooleanField()),
                ('lack_of_progress_in_the_courses', models.BooleanField()),
                ('need_to_re_enroll_in_classes_next_semester', models.BooleanField()),
                ('need_to_re_enroll_in_classes_with_different_instructor', models.BooleanField()),
                ('quality_of_instruction_did_not_meet_expections', models.BooleanField()),
                ('reduce_course_load', models.BooleanField()),
                ('wanted_classes_face_to_face', models.BooleanField()),
                ('wanted_classes_online', models.BooleanField()),
                ('change_in_family_financial_circumstances', models.BooleanField()),
                ('didnt_have_enough_money_to_continue', models.BooleanField()),
                ('financial_aid_was_not_sufficient', models.BooleanField()),
                ('increases_in_tuition_and_fees', models.BooleanField()),
                ('incurred_too_much_debt', models.BooleanField()),
                ('needed_Course_for_financial_aid_eligibility', models.BooleanField()),
                ('scholarship_Grant_was_not_renewed', models.BooleanField()),
                ('family_illness_responsibility', models.BooleanField()),
                ('homesick', models.BooleanField()),
                ('wanted_to_be_closer_to_family_and_friends', models.BooleanField()),
                ('commute_too_long', models.BooleanField()),
                ('moved_out_of_the_area', models.BooleanField()),
                ('distracted_Social_life', models.BooleanField()),
                ('felt_class_climate_unwelcoming', models.BooleanField()),
                ('felt_out_of_place_in_class', models.BooleanField()),
                ('impact_of_natural_disaster', models.BooleanField()),
                ('inadequate_study_skills_or_lack_of_academic_success', models.BooleanField()),
                ('military_obligations', models.BooleanField()),
                ('personal_health', models.BooleanField()),
                ('personal_emergency', models.BooleanField()),
                ('unmotivated_for_this_courses_or_tired_of_school', models.BooleanField()),
                ('working_too_many_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='courseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.DecimalField(decimal_places=0, max_digits=5)),
                ('course_prefix', models.CharField(max_length=4)),
                ('course_number', models.DecimalField(decimal_places=0, max_digits=4)),
                ('sec_no', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='degreeAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.CharField(max_length=10)),
                ('catalog_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('name_enrolled_under', models.CharField(max_length=50)),
                ('major_or_minor_name', models.CharField(max_length=100)),
                ('major_was_chosen', models.BooleanField()),
                ('minor_was_chosen', models.BooleanField()),
                ('semester', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], max_length=6)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('date',models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='empty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='masterGraduation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('name_enrolled_under', models.CharField(max_length=50)),
                ('mailing_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('ar', 'AR'), ('aa', 'AA'), ('ae', 'AE'), ('ak', 'AK'), ('al', 'AL'), ('ap', 'AP'), ('as', 'AS'), ('az', 'AZ'), ('ca', 'CA'), ('co', 'CO'), ('ct', 'CT'), ('dc', 'DC'), ('de', 'DE'), ('fl', 'FL'), ('ga', 'GA'), ('gu', 'GU'), ('hi', 'HI'), ('ia', 'IA'), ('id', 'ID'), ('il', 'IL'), ('in', 'IN'), ('ks', 'KS'), ('ky', 'KY'), ('la', 'LA'), ('ma', 'MA'), ('md', 'MD'), ('me', 'ME'), ('mi', 'MI'), ('mn', 'MN'), ('mo', 'MO'), ('mp', 'MP'), ('ms', 'MS'), ('mt', 'MT'), ('nc', 'NC'), ('nd', 'ND'), ('ne', 'NE'), ('nh', 'NH'), ('nj', 'NJ'), ('nm', 'NM'), ('nv', 'NV'), ('ny', 'NY'), ('oh', 'OH'), ('ok', 'OK'), ('or', 'OR'), ('pa', 'PA'), ('pr', 'PR'), ('ri', 'RI'), ('sc', 'SC'), ('sd', 'SD'), ('tn', 'TN'), ('tx', 'TX'), ('ut', 'UT'), ('va', 'VA'), ('vi', 'VI'), ('vt', 'VT'), ('wa', 'WA'), ('wi', 'WI'), ('wv', 'WV'), ('wy', 'WY')], max_length=2)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('phone_number', models.DecimalField(decimal_places=0, max_digits=9)),
                ('email', models.CharField(max_length=50)),
                ('student_starting_semester', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], max_length=6)),
                ('student_starting_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('diploma_name', models.CharField(max_length=50)),
                ('name_pronunciation', models.CharField(max_length=50)),
                ('expected_graduation_term', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], max_length=6)),
                ('expected_graduation_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('degree_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='permitToRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('name_enrolled_under', models.CharField(max_length=50)),
                ('registration_semester', models.CharField(max_length=10)),
                ('registration_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('comments', models.TextField(max_length=100)),
                ('total_hours_enrolled', models.DecimalField(decimal_places=0, max_digits=2)),
                ('dean_signature', models.CharField(max_length=50)),
                ('advisor_signature', models.CharField(max_length=50)),
                ('student_signature', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='substitutionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_course', models.CharField(max_length=50)),
                ('requested_course', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='transcriptRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('name_enrolled_under', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('mailing_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('ar', 'AR'), ('aa', 'AA'), ('ae', 'AE'), ('ak', 'AK'), ('al', 'AL'), ('ap', 'AP'), ('as', 'AS'), ('az', 'AZ'), ('ca', 'CA'), ('co', 'CO'), ('ct', 'CT'), ('dc', 'DC'), ('de', 'DE'), ('fl', 'FL'), ('ga', 'GA'), ('gu', 'GU'), ('hi', 'HI'), ('ia', 'IA'), ('id', 'ID'), ('il', 'IL'), ('in', 'IN'), ('ks', 'KS'), ('ky', 'KY'), ('la', 'LA'), ('ma', 'MA'), ('md', 'MD'), ('me', 'ME'), ('mi', 'MI'), ('mn', 'MN'), ('mo', 'MO'), ('mp', 'MP'), ('ms', 'MS'), ('mt', 'MT'), ('nc', 'NC'), ('nd', 'ND'), ('ne', 'NE'), ('nh', 'NH'), ('nj', 'NJ'), ('nm', 'NM'), ('nv', 'NV'), ('ny', 'NY'), ('oh', 'OH'), ('ok', 'OK'), ('or', 'OR'), ('pa', 'PA'), ('pr', 'PR'), ('ri', 'RI'), ('sc', 'SC'), ('sd', 'SD'), ('tn', 'TN'), ('tx', 'TX'), ('ut', 'UT'), ('va', 'VA'), ('vi', 'VI'), ('vt', 'VT'), ('wa', 'WA'), ('wi', 'WI'), ('wv', 'WV'), ('wy', 'WY')], max_length=2)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('phone_number', models.DecimalField(decimal_places=0, max_digits=9)),
                ('student_signature', models.CharField(max_length=50)),
                ('adhe', models.BooleanField()),
                ('sacm', models.BooleanField()),
                ('embassy_of_kuwait', models.BooleanField()),
                ('ade_licensure', models.BooleanField()),
                ('arsbn', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UGGraduation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('name_enrolled_under', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('student_signature', models.CharField(max_length=50)),
                ('diploma_name', models.CharField(max_length=50)),
                ('name_pronunciation', models.CharField(max_length=50)),
                ('pronunciation_recorded', models.BooleanField()),
                ('parents_completed_bachelor_degree', models.BooleanField()),
                ('expected_graduation_term', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], max_length=6)),
                ('expected_graduation_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('preferred_degree', models.CharField(max_length=100)),
            ],
        ),
    ]