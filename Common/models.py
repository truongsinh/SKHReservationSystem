from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
import Common.views

# Create your models here.
class Community(models.Model):
	address = models.CharField(max_length = 127)
	def link(self):
		return reverse(Common.views.community_detail, args=[self.id])
	def __unicode__(self):
		return self.address

class Apartment(models.Model):
	community = models.ForeignKey(Community)
	address = models.CharField(max_length = 127)
	note = models.TextField()
	def __unicode__(self):
		return self.address

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	apartment = models.ForeignKey(Apartment)
	plate_no = models.CharField(max_length = 127)
	def __unicode__(self):
		return self.plate_no
