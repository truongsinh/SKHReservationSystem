from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Community(models.Model):
	address = models.CharField(max_length = 127)

class Apartment(models.Model):
	community = models.ForeignKey(Community)
	address = models.CharField(max_length = 127)
	note = models.TextField()

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	apartment = models.ForeignKey(Apartment)
	plate_no = models.CharField(max_length = 127)