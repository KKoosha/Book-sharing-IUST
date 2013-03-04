from django.db import models
from django.contrib.auth.models import User
 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()

from django import forms
from django.core import validators
from django.contrib.auth.models import User
 

