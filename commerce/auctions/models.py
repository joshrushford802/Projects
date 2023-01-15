from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Group(models.Model):
    group = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.group}"


class Bidding(models.Model):
    bid_amount = models.FloatField()
    bidder = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="bidder")

    def __str__(self):
        return f"{self.bid_amount}"


class AuctionListing(models.Model):
    listing_name = models.CharField(max_length=36)
    product_description = models.CharField(max_length=140)
    initial_price = models.ForeignKey(Bidding, null=True, on_delete=models.CASCADE, related_name="price")
    image_representation = models.CharField(max_length=700)
    status = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, null=True, related_name="watchlist")
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, related_name="group_name")
    seller = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="seller")


class UserComments(models.Model):
    comment = models.CharField(max_length=140)
    post = models.ForeignKey(AuctionListing, null=True, on_delete=models.CASCADE, related_name="post")
    seller = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="commenter")
