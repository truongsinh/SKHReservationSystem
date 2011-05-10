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

class Sauna_queue(models.Model):
	user = models.ForeignKey(Profile, null=True)
	community = models.ForeignKey(Community, null=True)
	register_date = models.DateField(#'Registered Date',
									 auto_now_add=True)
	decision_date = models.DateField(#'Decided Date',
									 blank=True, null=True)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return u'%s - %s' % (self.user, self.community)

class Sauna_transaction(models.Model):
	sauna_queue = models.OneToOneField(Sauna_queue,
										 limit_choices_to = {'decision_date': None}
										 )
	sauna_slot = models.ForeignKey(Time_slot,
								#	 limit_choices_to = {'free': True}
									 )
	start_date = models.DateField('Start Date', auto_now_add=True)
	end_date = models.DateField('End Date', blank=True, null=True)
	note = models.TextField(blank=True)

	def __unicode__(self):
		return u'%s - %s' % (self.sauna_slot, self.sauna_queue)
