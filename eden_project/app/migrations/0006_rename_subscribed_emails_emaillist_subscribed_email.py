# Generated by Django 4.1.2 on 2022-12-06 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_emaillist_first_name_emaillist_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emaillist',
            old_name='subscribed_emails',
            new_name='subscribed_email',
        ),
    ]