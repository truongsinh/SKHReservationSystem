from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Community(models.Model):
	address = models.CharField(max_length = 127)
	city = models.CharField (max_length = 127)
	postal_code = models.CharField (max_length = 127)
	note = models.TextField(blank=True)
	def link(self):
		return reverse('Common.views.community_detail', args=[self.id])
	class Meta:
		verbose_name_plural = "communities"
		ordering = ['city', 'address']
	def __unicode__(self):
		return u'%s %s %s' % (self.city, self.address, self.postal_code, )
	
class Apartment(models.Model):
	community = models.ForeignKey(Community)
	address = models.CharField(max_length = 127)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return u'%s - %s' % (self.address, self.community, )

class Profile(User):
	#user = models.OneToOneField(User, primary_key=True)
	apartment = models.ForeignKey(Apartment, null=True)
	plate_no = models.CharField(max_length = 127, blank=True)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return u'%s (%s)' % (self.get_full_name(), self.username, )
