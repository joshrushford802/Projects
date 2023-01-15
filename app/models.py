from django.db import models
import datetime
from django.utils.html import format_html

class EmailList(models.Model):
    subscribed_email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return format_html("{} {}&emsp;subscribed with email:&emsp;{}", self.first_name, self.last_name, self.subscribed_email)
        elif self.first_name:
            return format_html("{} (last name withheld)&emsp;subscribed with email:&emsp;{}", self.first_name, self.subscribed_email)
        elif self.last_name:
            return format_html("(first name withheld) {}&emsp;subscribed with email:&emsp;{}", self.last_name, self.subscribed_email)
        else:
            return format_html("(first and last name withheld)&emsp;subscribed with email:&emsp;{}", self.subscribed_email)


class NewsArticle(models.Model):
    image = models.ImageField(upload_to="article_images", max_length=100, blank=True, null=True, editable=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=10000)

    def serialize(self):
        return {"timestamp": self.date.strftime("%b %d %Y")}


class InvasiveReport(models.Model):
    what_they_found = models.CharField(max_length=200, null=True)
    where_they_found_it = models.CharField(max_length=200, null=True)
    when_they_found_it = models.DateField(null=True)
    under_water_or_floating = models.CharField(max_length=11, null=True)
    did_you_collect_a_sample = models.CharField(max_length=3, null=True)
    name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    comments = models.CharField(max_length=200, null=True)

    def __str__(self):
        return format_html("Name:&emsp;{}<br>Phone number:&emsp;{}<br>Email:&emsp;{}<br>What they found:&emsp;{}<br>Location:&emsp;{}<br>When:&emsp;{}<br>Under water or floating:&emsp;{}<br>Sample collected:&emsp;{}<br>Comments:<br>&emsp;{}", self.name, self.phone_number, self.email, self.what_they_found, self.where_they_found_it, self.when_they_found_it, self.under_water_or_floating, self.did_you_collect_a_sample, self.comments)


class Donation(models.Model):
    project_specification = models.CharField(max_length=80, null=True)
    in_honor_of = models.CharField(max_length=100, null=True)
    comments = models.TextField(max_length=1000, null=True)

    def __str__(self):
        if self.project_specification and self.in_honor_of:
            return format_html("Donation recieved!<br>For project:&emsp;{}<br>In honor of:&emsp;{}<br>Comments:<br>&emsp;{}", self.project_specification, self.in_honor_of, self.comments)
        elif not self.project_specification and self.in_honor_of:
            return format_html("Donation recieved!<br>For project:&emsp;Undefined<br>In honor of:&emsp;{}<br>Comments:<br>&emsp;{}", self.in_honor_of, self.comments)
        elif self.project_specification and not self.in_honor_of:
            return format_html("Donation recieved!<br>For project:&emsp;{}<br>In honor of:&emsp;Undefined<br>Comments:<br>&emsp;{}", self.project_specification, self.comments)
        elif not self.project_specification and not self.in_honor_of:
            return format_html("Donation recieved!<br>For project:&emsp;Undefined<br>In honor of:&emsp;Undefined<br>Comments:<br>&emsp;{}", self.comments)