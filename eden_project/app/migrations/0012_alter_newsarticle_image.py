# Generated by Django 4.1.2 on 2022-12-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_newsarticle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='image',
            field=models.ImageField(height_field='620px', upload_to='article_images', width_field='250px'),
        ),
    ]
