# Generated by Django 4.1.2 on 2022-12-12 14:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_rename_collected_a_sample_yes_invasivereport_did_you_collect_a_sample_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invasivereport',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=200, null=True, region='US'),
        ),
        migrations.AlterField(
            model_name='invasivereport',
            name='when_they_found_it',
            field=models.DateField(blank=True, null=True),
        ),
    ]
