from django.contrib import admin
from .models import EmailList, NewsArticle, InvasiveReport, Donation

admin.site.register(EmailList)
admin.site.register(NewsArticle)
admin.site.register(InvasiveReport)
admin.site.register(Donation)