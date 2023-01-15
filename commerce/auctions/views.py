from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Group, AuctionListing, UserComments, Bidding

from .models import User


def index(request):
    groups = Group.objects.all()
    return render(request, "auctions/index.html", {
        "live_listings": tuple(AuctionListing.objects.filter(status=True)),
        "groups": groups
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """Registration for new users"""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_listing(request):
    """Create new listing"""
    if request.method == "POST":
        temp = request.POST["initial_price"]
        new_bid = Bidding(bid_amount=float(temp), bidder=request.user)
        new_bid.save()
        listing = AuctionListing(
            seller=request.user,
            listing_name = request.POST["listing_name"],
            image_representation = request.POST["image_representation"],
            initial_price = new_bid,
            product_description = request.POST["product_description"],
            group = Group.objects.get(group=request.POST["group"])
        )

        listing.save()
        return HttpResponseRedirect(reverse(index))
    else:
        groups = Group.objects.all()
        return render(request, "auctions/new_listing.html", {
            "groups": groups
        })


def delete_post(request, id):
    retrieve_listing = AuctionListing.objects.get(pk=id)
    retrieve_listing.status = False
    retrieve_listing.save()

    return render(request, "auctions/get_listing.html", {
        "retrieve_listing": retrieve_listing,
        "watchlist_confirmation": request.user in retrieve_listing.watchlist.all(),
        "collection_of_comments": UserComments.objects.filter(post=retrieve_listing),
        "seller_verification": retrieve_listing.seller.username == request.user.username,
        "reverse": True
    })


def group_search(request):
    if request.method == "POST":
        groups = Group.objects.all()
        group = Group.objects.get(group=request.POST["group"])
        return render(request, "auctions/index.html", {
            "live_listings": AuctionListing.objects.filter(status=True, group=group),
            "groups": groups
        })


def get_listing(request, id):
    retrieve_listing = AuctionListing.objects.get(pk=id)
    return render(request, "auctions/get_listing.html", {
        "retrieve_listing": retrieve_listing,
        "watchlist_confirmation": request.user in retrieve_listing.watchlist.all(),
        "collection_of_comments": UserComments.objects.filter(post=retrieve_listing),
        "seller_verification": retrieve_listing.seller.username == request.user.username
    })


def rm_watchlist(request, id):
    listing_object = AuctionListing.objects.get(pk=id)
    listing_object.watchlist.remove(request.user)
    return HttpResponseRedirect(reverse("get_listing", args=(id, )))


def add_watchlist(request, id):
    listing_object = AuctionListing.objects.get(pk=id)
    listing_object.watchlist.add(request.user)
    return HttpResponseRedirect(reverse("get_listing", args=(id, )))


def my_watchlist(request):
    end_user = request.user
    return render(request, "auctions/my_watchlist.html", {
        "retrieve_listing": end_user.watchlist.all()
    })


def user_comments(request, id):
    make_comment = UserComments(
        comment = request.POST["comment"],
        post = AuctionListing.objects.get(pk=id),
        seller = request.user
    )

    make_comment.save()

    return HttpResponseRedirect(reverse("get_listing", args=(id, )))


def bid(request, id):
    listing_object = AuctionListing.objects.get(pk=id)
    if float(request.POST["bid_placement"]) < float(listing_object.initial_price.bid_amount):

        return render(request, "auctions/get_listing.html", {
            "status_update": "Bid amount needs to be more than the initial price",
            "working_status": False,
            "collection_of_comments": UserComments.objects.filter(post=AuctionListing.objects.get(pk=id)),
            "seller_verification": listing_object.seller.username == request.user.username,
            "retrieve_listing": listing_object
        })

    else:
        users_bid = Bidding(bid_amount=request.POST["bid_placement"], bidder=request.user)
        users_bid.save()

        listing_object.initial_price = users_bid
        listing_object.save()

        return render(request, "auctions/get_listing.html", {
            "status_update": "Bid submitted!",
            "working_status": True,
            "collection_of_comments": UserComments.objects.filter(post=AuctionListing.objects.get(pk=id)),
            "seller_verification": listing_object.seller.username == request.user.username,
            "retrieve_listing": listing_object
        })
