# Generated by Django 4.1.2 on 2022-12-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_emaillist_subscribed_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
