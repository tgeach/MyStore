import datetime
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    name = models.CharField(max_length=250)
    user = models.ManyToManyField(User)

class Location(models.Model):
    name = models.CharField(max_length=250)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    province_state = models.CharField(max_length=80, blank=True, null=True)
    country = models.CharField(max_length=80, blank=True, null=True)
    zip_postal = models.CharField(max_length=10, blank=True, null=True)
    contact_phone = models.CharField(max_length=11, blank=True, null=True)

class Inventory(models.Model):
    name = models.CharField(max_length=250)
    unit = models.CharField(max_length=250)
    price_per_unit = models.FloatField()

class Order(models.Model):
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    quantity = models.IntegerField()


