from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Community(models.Model):
	address = models.CharField(max_length=100)

class Area(models.Model):
	community = models.ForeignKey (Community)
	need_rental_agreement = models. BooleanField()
	user_in_charge = models. CharField(max_length=100)
	note = models.TextField()

class Type(models.Model):
	parking_area = models.ForeignKey(Area)
	price_per_month = models.DecimalField(max_digits=5, decimal_places=2)
	note = models.CharField(max_length=500)

class Slot(models.Model):
	parking_area = models.ForeignKey(Area)
	parking_type = models.ForeignKey(Type)
	note = models.TextField(max_length=500)
	def is_free(self):
		return True

class Queue(models.Model):
	user = models.ForeignKey(User)
	community = models.ForeignKey(Community)
	register_date = models.DateField('Registered Date')
	decision_date = models.DateField('Decided Date')
	decision = models.NullBooleanField()
	note = models.TextField(max_length=500)

class Transaction(models.Model):
	parking_slot = models.ForeignKey(Slot)
	parking_queue = models.ForeignKey(Queue)
	start_date = models.DateField('Start Date')
	end_date = models.DateField('End Date')
	paid = models.BooleanField()
	note = models.TextField(max_length=500)
	def is_history(self):
		return True
