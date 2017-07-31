from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from timezone_field import TimeZoneField
from taggit.managers import TaggableManager

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    company = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=15)
    skype = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=50, blank=True)
    birthDate = models.DateField(null=True)
    timezone = TimeZoneField(null=True)
    tags = TaggableManager()
    avatar = models.ImageField(upload_to='/media/images/')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()