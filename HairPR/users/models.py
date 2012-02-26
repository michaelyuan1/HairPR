from django.db import models
from django import forms
from django.core.validators import validate_email

class User(models.Model):
	email = models.CharField(max_length=200, validators=[validate_email])

	def __unicode__(self):
		return self.email