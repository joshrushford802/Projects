# Generated by Django 4.1.2 on 2022-12-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_subscribed_emails_emaillist_subscribed_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('title', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]
