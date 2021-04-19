# Generated by Django 3.2 on 2021-04-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeanProject', '0009_alter_degreeauditamendmentrequest_course_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num1B',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num2',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num2B',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num3',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num4',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_num5',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number1',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number2',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number3',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number4',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number5',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='atu_course_number6',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_num',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_num2',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_num3',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_num4',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_num5',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]