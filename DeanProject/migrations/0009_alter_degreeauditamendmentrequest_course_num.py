# Generated by Django 3.2 on 2021-04-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeanProject', '0008_alter_degreeauditamendmentrequest_atu_course_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degreeauditamendmentrequest',
            name='course_num',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=10, null=True),
        ),
    ]
