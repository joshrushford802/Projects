
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user_login", views.logged, name="logged"),
    path("unsubscribe", views.unsubscribe, name="unsubscribe"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("subscribed", views.subscribed, name="subscribed"),
    path("user_logout", views.out_logged, name="out_logged"),
    path("void_vote/<int:p>", views.void_vote, name="void_vote"),
    path("increment_vote/<int:p>", views.increment_vote, name="increment_vote"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("make_post", views.make_post, name="make_post"),
    path("account/<int:user_id>", views.account, name="account"),
    path("make_adjustments/<int:p>", views.make_adjustments, name="make_adjustments")
]
