# Generated by Django 4.1.2 on 2022-11-05 21:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bids_comments_auctionlisting_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='watchlist',
            field=models.ManyToManyField(null=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
