from django.core.checks import messages
from django.db import models

# Create your models here.
class Service(models.Model):
    fa_icon_calss = models.CharField(max_length=200)
    service_name = models.CharField(max_length=100)
    service_details = models.TextField()
    modal_id = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return str(self.service_name)

class Portfolio(models.Model):
    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    date = models.DateField()
    client = models.CharField(max_length=250)
    short_description = models.TextField()
    description = models.TextField()
    thumbnail_image = models.ImageField(upload_to='img/portfolio/')
    full_image = models.ImageField(upload_to='img/portfolio/')
    modal_id = models.CharField(max_length=250)
    def __str__(self):
        return str(self.project_name)

class About(models.Model):
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    eventDate = models.DateField(null=True, blank=True)
    event_title = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='img/about/', null=True, blank=True)
    event_details = models.TextField()
    def __str__(self):
        return str(self.event_title)

class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img/team/', blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkdin_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return str(self.role)

class Client(models.Model):
    name = models.CharField(max_length=100)
    client_logo = models.ImageField(upload_to='img/logo/')
    client_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return str(self.client_logo)

class Contact(models.Model):
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    messages = models.TextField()
    def __str__(self):
        return str(self.time)

class CompanySocialDetail(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(max_length=250)
    icon = models.CharField(max_length=150)
    def __str__(self):
        return str(self.name)