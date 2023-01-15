from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('register_email', views.register_email, name="register_email"),
    path('privacy_policy', views.privacy_policy, name="privacy_policy"),
    path('what_is_an_invasive', views.what_is_an_invasive, name="what_is_an_invasive"),
    path('about_milfoil', views.about_milfoil, name="about_milfoil"),
    path('milfoil_control_efforts', views.milfoil_control_efforts, name="milfoil_control_efforts"),
    path('other_invasive_species', views.other_invasive_species, name="other_invasive_species"),
    path('greeter_and_vip_programs', views.greeter_and_vip_programs, name="greeter_and_vip_programs"),
    path('health_overview', views.health_overview, name="health_overview"),
    path('sampling_and_monitoring_programs', views.sampling_and_monitoring_programs, name="sampling_and_monitoring_programs"),
    path('shoreline_health', views.shoreline_health, name="shoreline_health"),
    path('lake_data_and_maps', views.lake_data_and_maps, name="lake_data_and_maps"),
    path('plant_surveys', views.plant_surveys, name="plant_surveys"),
    path('overview', views.overview, name="overview"),
    path('boating_on_lake_eden', views.boating_on_lake_eden, name="boating_on_lake_eden"),
    path('public_fishing_and_boat_access', views.public_fishing_and_boat_access, name="public_fishing_and_boat_access"),
    path('greeter_program', views.greeter_program, name="greeter_program"),
    path('why_become_a_member', views.why_become_a_member, name="why_become_a_member"),
    path('donate', views.donate, name="donate"),
    path('make_donation', views.make_donation, name="make_donation"),
    path('volunteer_opportunities', views.volunteer_opportunities, name="volunteer_opportunities"),
    path('join_email_list', views.join_email_list, name="join_email_list"),
    path('report_invasives', views.report_invasives, name="report_invasives"),
    path('create_invasive_report', views.create_invasive_report, name="create_invasive_report"),
    path('who_we_are', views.who_we_are, name="who_we_are"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('history_of_the_lake', views.history_of_the_lake, name="history_of_the_lake"),
    path('mission_and_bylaws', views.mission_and_bylaws, name="mission_and_bylaws"),
    path('meeting_minutes', views.meeting_minutes, name="meeting_minutes"),
    path('plans_and_annual_reports', views.plans_and_annual_reports, name="plans_and_annual_reports"),
    path('news_and_events', views.news_and_events, name="news_and_events"),
    path('<str:article_id>', views.article, name="article")
]