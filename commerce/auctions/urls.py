from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("group_search", views.group_search, name="group_search"),
    path("listing_view/<int:id>", views.get_listing, name="get_listing"),
    path("remove_from_watchlist/<int:id>", views.rm_watchlist, name="rm_watchlist"),
    path("add_to_watchlist/<int:id>", views.add_watchlist, name="add_watchlist"),
    path("my_watchlist", views.my_watchlist, name="my_watchlist"),
    path("user_comments/<int:id>", views.user_comments, name="user_comments"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post")
]
