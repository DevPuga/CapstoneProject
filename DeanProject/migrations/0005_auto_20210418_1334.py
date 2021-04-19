# Generated by Django 3.2 on 2021-04-18 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeanProject', '0004_degreeauditamendmentrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degreeauditamendmentrequest',
            old_name='atu_course_num1',
            new_name='atu_course_number1',
        ),
        migrations.RemoveField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num6',
        ),
        migrations.AddField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number2',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number3',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number4',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number5',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number6',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix1B',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix2B',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix3B',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_prefix6',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_subject2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_subject3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_subject4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_subject5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='change_grad_Term_to',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='college_distinction',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='college_distinction2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='comments',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='comments4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='comments5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='comments6',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_Substitution',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_Substitution2',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_Substitution3',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_Substitution4',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_Substitution5',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_equivalent',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_equivalent2',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_equivalent3',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_equivalent4',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_equivalent5',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_subject2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_subject3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_subject4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_subject5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='grade2',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='grade3',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='grade4',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='grade5',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='major_was_chosen',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='semester_taken1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='semester_taken2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='semester_taken3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='semester_taken4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='semester_taken5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='transfer_Institution',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='transfer_Institution2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='transfer_Institution3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='transfer_Institution4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='transfer_Institution5',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]