from Common.models import *
from django.core.urlresolvers import reverse
import datetime

class Sauna(models.Model):
	name = models.CharField (max_length=127)
	community = models.ForeignKey(Community)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.name
	
class Time_slot(models.Model):
	name = models.CharField (max_length=127)
	sauna = models.ForeignKey(Sauna)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.name
	#This model need modification to bind certain user on it
	#Similar to Parking_Slot model