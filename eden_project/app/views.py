from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages

from .models import EmailList, NewsArticle, InvasiveReport, Donation


def index(request):
    articles = NewsArticle.objects.all().order_by("id").reverse()
    page = request.GET.get('page')
    paginator = Paginator(articles, 3).get_page(page)

    return render(request, "index.html", {
        "paginator": paginator
    })

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def what_is_an_invasive(request):
    return render(request, "invasive_species/what_is_an_invasive.html")

def about_milfoil(request):
    return render(request, "invasive_species/about_milfoil.html")

def milfoil_control_efforts(request):
    return render(request, "invasive_species/milfoil_control_efforts.html")

def other_invasive_species(request):
    return render(request, "invasive_species/other_invasive_species.html")

def greeter_and_vip_programs(request):
    return render(request, "invasive_species/greeter_and_vip_programs.html")

def health_overview(request):
    return render(request, "lake_health/health_overview.html")

def sampling_and_monitoring_programs(request):
    return render(request, "lake_health/sampling_and_monitoring_programs.html")

def shoreline_health(request):
    return render(request, "lake_health/shoreline_health.html")

def lake_data_and_maps(request):
    return render(request, "lake_health/lake_data_and_maps.html")

def plant_surveys(request):
    return render(request, "lake_health/plant_surveys.html")

def overview(request):
    return render(request, "enjoying_the_lake/overview.html")

def boating_on_lake_eden(request):
    return render(request, "enjoying_the_lake/boating_on_lake_eden.html")

def public_fishing_and_boat_access(request):
    return render(request, "enjoying_the_lake/public_fishing_and_boat_access.html")

def greeter_program(request):
    return render(request, "enjoying_the_lake/greeter_program.html")

def why_become_a_member(request):
    return render(request, "how_to_help/why_become_a_member.html")

def donate(request):
    return render(request, "how_to_help/donate.html")

def make_donation(request):
    if request.method == "POST":
        project_specification = request.POST['project_specification']
        in_honor_of = request.POST['in_honor_of']
        comments = request.POST['comments']
        new_donation = Donation(project_specification=project_specification, in_honor_of=in_honor_of, comments=comments)
        new_donation.save()

        return HttpResponseRedirect(reverse(index))

def volunteer_opportunities(request):
    return render(request, "how_to_help/volunteer_opportunities.html")

def join_email_list(request):
    return render(request, "how_to_help/join_email_list.html")

def register_email(request):
    if request.method == "POST":

        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_subscriber = EmailList(subscribed_email=email, first_name=first_name, last_name=last_name)
        new_subscriber.save()

        messages.info(request, 'temp')
        return HttpResponseRedirect(reverse(index))

def report_invasives(request):
    return render(request, "how_to_help/report_invasives.html")

def create_invasive_report(request):
    if request.method == "POST":
        what_did_you_find = request.POST['what_did_you_find']
        where_did_you_find_it = request.POST['where_did_you_find_it']

        if request.POST['when_did_you_find_it']:
            when_did_you_find_it = request.POST['when_did_you_find_it']
        else:
            when_did_you_find_it = "0001-01-01"

        under_water_or_floating = request.POST['flexRadioDefault']
        did_you_collect_a_sample = request.POST['exampleRadios']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        comments = request.POST['comments']
        new_report = InvasiveReport(what_they_found=what_did_you_find, where_they_found_it=where_did_you_find_it, when_they_found_it=when_did_you_find_it, under_water_or_floating=under_water_or_floating, did_you_collect_a_sample=did_you_collect_a_sample, name=name, phone_number=phone_number, email=email, comments=comments)
        new_report.save()

        messages.info(request, 'temp')
        return HttpResponseRedirect(reverse(index))

def who_we_are(request):
    return render(request, "about/who_we_are.html")

def contact_us(request):
    return render(request, "about/contact_us.html")

def history_of_the_lake(request):
    return render(request, "about/history_of_the_lake.html")

def mission_and_bylaws(request):
    return render(request, "about/mission_and_bylaws.html")

def meeting_minutes(request):
    return render(request, "about/meeting_minutes.html")

def plans_and_annual_reports(request):
    return render(request, "about/plans_and_annual_reports.html")

def news_and_events(request):
    articles = NewsArticle.objects.all().order_by("id").reverse()
    page = request.GET.get('page')
    paginator = Paginator(articles, 8).get_page(page)

    return render(request, "news_and_events.html", {
        "paginator": paginator
    })

def article(request, article_id):
    articles = NewsArticle.objects.all().order_by("id").reverse()
    extra = NewsArticle.objects.get(title=article_id)

    return render(request, "article.html", {
        "extra": extra,
        "articles": articles
    })