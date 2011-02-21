from django.db.models import *

# Create your models here.
class version(Model):
	major = PositiveSmallIntegerField()
	minor = PositiveSmallIntegerField()
	STATUS_CHOICE = (
		(0, 'dev'),
		(1, 'alpha'),
		(2, 'beta'),
		(3, 'rc'),
		(4, 'gold'),
	)
	status = PositiveSmallIntegerField(choices=STATUS_CHOICE)
	build = DateField()