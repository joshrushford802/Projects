# Generated by Django 4.1.2 on 2022-12-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_newsarticle_content_alter_newsarticle_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='content',
            field=models.CharField(max_length=4000),
        ),
    ]
