# Generated by Django 4.1.2 on 2022-12-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_donation_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='comments',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
