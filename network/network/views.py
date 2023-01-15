import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Follow, User, Like, Post
from django.core.paginator import Paginator
def index(request):
    culmination_of_posts = Post.objects.all().order_by("id").reverse()
    thumb_ups = Like.objects.all()
    like_array = []
    num_pg = request.GET.get('page')
    pg_num = Paginator(culmination_of_posts, 10).get_page(num_pg)
    try:
        for _ in thumb_ups:
            if _.dweller.id == request.user.id:
                like_array.append(_.pid.id)
    except:
        like_array = []
    return render(request, "network/index.html", {
        "culmination_of_posts": culmination_of_posts,
        "pg_posts": pg_num,
        "like_array": like_array
    })
def subscribed(request):
    subbed_to = Follow.objects.filter(dweller=User.objects.get(pk=request.user.id))
    culmination_of_posts = Post.objects.all().order_by('id').reverse()
    subArray = []
    for article in culmination_of_posts:
        for subbed in subbed_to:
            if subbed.sub == article.maker:
                subArray.append(article)
    pg_num = request.GET.get('page')
    num_pg = Paginator(subArray, 10).get_page(pg_num)
    return render(request, "network/following.html", {
        "num_pg": num_pg
    })
def make_adjustments(request, p):
    if request.method == "POST":
        f = json.loads(request.body)
        adj = Post.objects.get(pk=p)
        adj.material = f["material"]
        adj.save()
        return JsonResponse({"data": f["material"]})
def make_post(request):
    if request.method == "POST":
        material = request.POST['material']
        dweller = User.objects.get(pk=request.user.id)
        article = Post(maker=dweller, material=material)
        article.save()
        return HttpResponseRedirect(reverse(index))
def sign_up(request):
    if request.method == "POST":
        usr_nm = request.POST["usr_nm"]
        email_address = request.POST["email_address"]
        passw = request.POST["passw"]
        authenticate = request.POST["authenticate"]
        if passw != authenticate:
            return render(request, "network/register.html", {
                "alert": "You entered an incorrect password. Please try again."
            })
        try:
            dweller = User.objects.create_user(usr_nm, email_address, passw)
            dweller.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "alert": "Invalid username. Please try a different one."
            })
        login(request, dweller)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
def increment_vote(request, p):
    article = Post.objects.get(pk=p)
    dweller = User.objects.get(pk=request.user.id)
    thumbs_up = Like(pid=article, dweller=dweller)
    thumbs_up.save()
    return JsonResponse({"message": "Liked"})
def unsubscribe(request):
    sub = request.POST['sub']
    now_dweller = User.objects.get(pk=request.user.id)
    subDt = User.objects.get(username=sub)
    store = Follow.objects.get(dweller=now_dweller, sub=subDt)
    store.delete()
    user_id = subDt.id
    return HttpResponseRedirect(reverse(account, kwargs={'user_id': user_id}))
def logged(request):
    if request.method == "POST":
        usr_nm = request.POST["usr_nm"]
        passw = request.POST["passw"]
        dweller_authentication = authenticate(request, username=usr_nm, password=passw)
        if dweller_authentication is not None:
            login(request, dweller_authentication)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "alert": "Incorrect credentials."
            })
    else:
        return render(request, "network/login.html")
def subscribe(request):
    sub = request.POST["sub"]
    now_dweller = User.objects.get(pk=request.user.id)
    subDt = User.objects.get(username=sub)
    store = Follow(dweller=now_dweller, sub=subDt)
    store.save()
    user_id = subDt.id
    return HttpResponseRedirect(reverse(account, kwargs={'user_id': user_id}))
def out_logged(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
def void_vote(request, p):
    article = Post.objects.get(pk=p)
    dweller = User.objects.get(pk=request.user.id)
    thumbs_up = Like.objects.filter(dweller=dweller, pid=article)
    thumbs_up.delete()
    return JsonResponse({"message": "Voided like"})
def account(request, user_id):
    dweller = User.objects.get(pk=user_id)
    find_dweller = User.objects.get(pk=request.user.id)
    culmination_of_posts = Post.objects.filter(maker=dweller).order_by("id").reverse()
    te = Like.objects.filter(dweller=dweller)
    subbed = Follow.objects.filter(dweller=dweller)
    subs = Follow.objects.filter(sub=dweller)
    try:
        sub_or_not = subs.filter(dweller=find_dweller)
        if len(sub_or_not) == 0:
            confirmed_sub = False
        else:
            confirmed_sub = True
    except:
        confirmed_sub = False
    pg_num = request.GET.get('page')
    num_pg = Paginator(culmination_of_posts, 10).get_page(pg_num)
    return render(request, "network/profile.html", {
        "culmination_of_posts": culmination_of_posts,
        "dweller_account": dweller,
        "num_pg": num_pg,
        "username": dweller.username,
        "confirmed_sub": confirmed_sub,
        "subbed": subbed,
        "te": te,
        "subs": subs
    })