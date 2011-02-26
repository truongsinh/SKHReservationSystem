from Common.models import *
from django.core.urlresolvers import reverse
import Parking.views
import datetime
# Create your models here.
# Each object has two instances which will be created later
class Area(models.Model):
	community = models.ForeignKey(Community)
	need_rental_agreement = models.BooleanField()
	user_in_charge = models.ManyToManyField(User)
	note = models.TextField()
	def __unicode__(self):
		return self.note

class Type(models.Model):
	price_per_month = models.DecimalField(max_digits=5, decimal_places=2)
	note = models.CharField(max_length=127)
	def __unicode__(self):
		return self.note

class Slot(models.Model):
	parking_area = models.ForeignKey(Area)
	parking_type = models.ForeignKey(Type)
	note = models.TextField(max_length=127)
	def is_free(self):
		# Link to transaction ex: return Transaction.end_date ...
		return True
	def __unicode__(self):
		return self.note

class Queue(models.Model):
	user = models.ForeignKey(User)
	community = models.ForeignKey(Community)
	register_date = models.DateField('Registered Date', auto_now_add=True)
	decision_date = models.DateField('Decided Date', blank=True, null=True)
	decision = models.NullBooleanField()
	note = models.TextField(max_length=127)
	def __unicode__(self):
		return self.community
	def link(self):
		return reverse(Parking.views.queue_detail, args=[self.id])

class Transaction(models.Model):
	parking_slot = models.ForeignKey(Slot)
	parking_queue = models.ForeignKey(Queue)
	start_date = models.DateField('Start Date', auto_now_add=True)
	end_date = models.DateField('End Date', blank=True, null=True)
	paid = models.BooleanField()
	note = models.TextField(max_length=127)
	def is_history(self):
		return self.end_date is not None
	def __unicode__(self):
		return self.parking_slot
