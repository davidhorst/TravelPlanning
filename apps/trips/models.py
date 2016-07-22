from __future__ import unicode_literals

from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User

import datetime

class Trip(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Traveler(models.Model):
	Traveler_id = models.ForeignKey(User)
	Trip_id = models.ForeignKey(Trip)

def clean_date(date, checkdate=datetime.date.today()):

    if not isinstance(date, datetime.date):
    	date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
  

    if date < checkdate:
        raise ValidationError("You cannot travel into the past. because rules")
        
    return date