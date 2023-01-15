# Generated by Django 4.1.2 on 2022-11-07 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_usercomments_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.FloatField()),
                ('bidder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='initial_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initial_price', to='auctions.bidding'),
        ),
    ]
