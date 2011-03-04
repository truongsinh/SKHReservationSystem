from Common.models import *
from django.core.urlresolvers import reverse
import datetime
# Create your models here.
# Each object has two instances which will be created later
class Area(models.Model):
	community = models.ForeignKey(Community)
	need_rental_agreement = models.BooleanField()
	user_in_charge = models.ManyToManyField(Profile)
	note = models.TextField()
	def __unicode__(self):
		return self.note

class Type(models.Model):
	price_per_month = models.DecimalField(max_digits=5, decimal_places=2)
	note = models.CharField(max_length=127)
	def __unicode__(self):
		return self.note

class Slot(models.Model):
	name = models.CharField (max_length=127)
	parking_area = models.ForeignKey(Area)
	parking_type = models.ForeignKey(Type)
	note = models.TextField(max_length=127)
	def is_free(self):
		# Link to transaction ex: return Transaction.end_date ...
		return True
	is_free.short_description = 'Is free?'
	def __unicode__(self):
		return "%d" % self.id

class Queue(models.Model):
	user = models.ForeignKey(Profile, null=True)
	community = models.ForeignKey(Community, null=True)
	register_date = models.DateField('Registered Date', auto_now_add=True)
	decision_date = models.DateField('Decided Date', blank=True, null=True)
	note_queue = models.TextField(max_length=127)
	def __unicode__(self):
		return self.user.plate_no
	def link(self):
		return reverse('Parking.views.queue_detail', args=[self.id])
	class Meta:
		permissions = (
			("view_queue_full", "Can see queue full"),
			("view_queue_limited", "Can see queue limited"),
		)

class Transaction(models.Model):
	parking_queue = models.OneToOneField(Queue)
	parking_slot = models.ForeignKey(Slot)
	start_date = models.DateField('Start Date', auto_now_add=True)
	end_date = models.DateField('End Date', blank=True, null=True)
	paid = models.BooleanField()
	note_transaction = models.TextField(max_length=127)
	def is_history(self):
		return self.end_date is not None and self.end_date < datetime.date.today()
	def is_current(self):
		return not self.is_history()
	def __unicode__(self):
		return self.parking_queue.user.plate_no
	def link(self):
		return reverse('Parking.views.reservation_detail', args=[self.id])