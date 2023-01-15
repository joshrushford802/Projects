from django.contrib import admin
from .models import User, Group, AuctionListing, UserComments, Bidding

# Register your models here.
class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("seller", "listing_name", "product_description", "initial_price", "status")

class GroupAdmin(admin.ModelAdmin):
    list_display = ["group"]

admin.site.register(User)
admin.site.register(Group, GroupAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(UserComments)
admin.site.register(Bidding)