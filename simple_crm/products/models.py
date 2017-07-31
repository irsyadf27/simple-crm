from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, blank=True) 
    vendor = models.CharField(max_length=50, blank=True) 
    price_per = models.CharField(max_length=50, blank=True) 
    price = models.DecimalField(max_digits=8, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)
    yearly_price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = TaggableManager()
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Editions(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    perpetual = models.DecimalField(max_digits=8, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)
    yearly_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name