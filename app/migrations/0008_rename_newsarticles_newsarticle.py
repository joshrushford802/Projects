# Generated by Django 4.1.2 on 2022-12-08 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_newsarticles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsArticles',
            new_name='NewsArticle',
        ),
    ]