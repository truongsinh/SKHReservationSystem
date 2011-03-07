from Common.models import *
from django.core.urlresolvers import reverse
import datetime
# Create your models here.
# Each object has two instances which will be created later
class Area(models.Model):
	name = models.CharField (max_length=127)
	community = models.ForeignKey(Community)
	need_rental_agreement = models.BooleanField()
	user_in_charge = models.ManyToManyField(Profile,
											limit_choices_to = {'is_staff': True}
											)
	note = models.TextField(blank=True)
	class Meta:
		unique_together = (
			("name", "community"),
		)
	def __unicode__(self):
		return u'%s - %s' % (self.name, self.community)

class Type(models.Model):
	name = models.CharField(max_length=127)
	price_per_month = models.DecimalField(max_digits=5, decimal_places=2)
	note = models.CharField(max_length=127)
	def __unicode__(self):
		return self.name

class Slot(models.Model):
	name = models.CharField(max_length=127)
	parking_area = models.ForeignKey(Area)
	parking_type = models.ForeignKey(Type)
	note = models.TextField(blank=True)
	def is_free(self):
		obj = self.transaction_set.exclude(end_date__lt = datetime.date.today())
		if obj.count() > 0:
			return False
		else:
			return True
	#is_free.short_description = 'Is free?'
	free = models.BooleanField(editable=False)
	class Meta:
		unique_together = (
			("name", "parking_area"),
		)
	def __unicode__(self):
		return u'%s - %s' % (self.name, self.parking_area)
	def save(self, *args, **kwargs):
		if self.id is None:
			super(Slot, self).save(*args, **kwargs)
		if self.is_free() != self.free:
			self.free = not self.free
			super(Slot, self).save(*args, **kwargs)


class Queue(models.Model):
	user = models.ForeignKey(Profile, null=True)
	community = models.ForeignKey(Community, null=True)
	register_date = models.DateField(#'Registered Date',
									 auto_now_add=True)
	decision_date = models.DateField(#'Decided Date',
									 blank=True, null=True)
	note = models.TextField(blank=True)
	class Meta:
		unique_together = (
			("user", "community"),
		)
	def __unicode__(self):
		return u'%s - %s' % (self.user, self.community)
	def link(self):
		return reverse('Parking.views.queue_detail', args=[self.id])
	def get_status(self):
		if self.decision_date is None:
			return None
		elif self.transaction.count() > 0:
			return True
		else:
			return False
	get_status.boolean = True

class Transaction(models.Model):
	parking_queue = models.OneToOneField(Queue,
										 limit_choices_to = {'decision_date': None}
										 )
	parking_slot = models.ForeignKey(Slot,
									 limit_choices_to = {'free': True}
									 )
	start_date = models.DateField('Start Date', auto_now_add=True)
	end_date = models.DateField('End Date', blank=True, null=True)
	paid = models.BooleanField()
	note = models.TextField(blank=True)
	def __unicode__(self):
		return u'%s - %s' % (self.parking_slot, self.parking_queue)
	def is_current(self):
		return self.end_date is None or self.end_date >= datetime.date.today()
	is_current.boolean = True
	def slot_name(self):
		return self.parking_slot.name
	def link(self):
		return reverse('Parking.views.reservation_detail', args=[self.id])
	def community_name (self):
		return self.parking_queue.community.address
	def user_name (self):
		return self.parking_queue.user.last_name
	def save(self, *args, **kwargs):
		self.parking_queue.decision_date = datetime.date.today()
		self.parking_queue.save()
		super(Transaction, self).save(*args, **kwargs)