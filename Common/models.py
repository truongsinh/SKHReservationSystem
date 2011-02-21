from django.db import models

# Create your models here.
class Community(models.Model):
	address = models.CharField(max_length = 127)

class Apartment(models.Model):
	community = models.ForeignKey(Community)
	address = models.CharField(max_length = 127)
	note = models.TextField()

class Profile(models.Model):
	apartment = models.ForeignKey(Apartment)
	plate_no = models.CharField(max_length = 127)