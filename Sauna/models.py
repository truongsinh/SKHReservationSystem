from Common.models import *
from django.core.urlresolvers import reverse
import datetime

class Sauna(models.Model):
	name = models.CharField (max_length=127)
	community = models.ForeignKey(Community)
	note = models.TextField(blank=True)
	class Meta:
		unique_together = (
			("name", "community"),
		)
	def __unicode__(self):
		return u'%s - %s' % (self.name, self.community)

	
class Time_slot(models.Model):
	name = models.CharField (max_length=127)
	sauna = models.ForeignKey(Sauna)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.name
	def is_free(self):
		obj = self.sauna_transaction_set.exclude(end_date__lt = datetime.date.today())
		if obj.count() > 0:
			return False
		else:
			return True
	#is_free.short_description = 'Is free?'
	free = models.BooleanField(editable=False)
	class Meta:
		unique_together = (
			("name", "sauna"),
		)

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
	class Meta:
		unique_together = (
			("user", "community"),
		)
	def get_status(self):
		if self.decision_date is None:
			return None
		elif self.sauna_transaction.count() > 0:
			return True
		else:
			return False
	get_status.boolean = True
	def link(self):
		return reverse('Sauna.views.queue_detail', args=[self.id])

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
	def is_current(self):
		return self.end_date is None or self.end_date >= datetime.date.today()
	is_current.boolean = True
	def slot_name(self):
		return self.sauna_slot.name
	def community_name (self):
		return self.sauna_queue.community.address
	def user_name (self):
		return self.sauna_queue.user.last_name
	def save(self, *args, **kwargs):
		self.sauna_queue.decision_date = datetime.date.today()
		self.sauna_queue.save()
		super(Sauna_transaction, self).save(*args, **kwargs)
	def link(self):
		return reverse('Sauna.views.reservation_detail', args=[self.id])