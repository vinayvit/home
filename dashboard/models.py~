from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from datetime import datetime
# Create your models here.

class Document(models.Model):
       user = models.ForeignKey(User, unique=False)
       docfile = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)
       firstname = models.CharField(max_length=200)
       lastname = models.CharField(max_length=200)
       address = models.CharField(max_length=500)

class Event(models.Model):
       user = models.ForeignKey(User, unique=False)
       snap = models.FileField(upload_to='event/%d/%m/%y',blank=True, null=True)
       eventtype = models.CharField(max_length=200,null=False)
       date_created = models.DateTimeField(default=timezone.now)
       date_event = models.DateTimeField(default=False)
       dresscode = models.BooleanField(default=False)
       duration = models.TimeField(blank=True, null=True)
       description= models.CharField(max_length=400)
       place = models.CharField(max_length=50)

       


      
