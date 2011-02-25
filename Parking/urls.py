'''from django.conf.urls.defaults import *

urlpatterns = patterns('Parking.views',
    url(r'^$', 'reservation_list'),
	url(r'^(?P<transaction_id>\d+)/$', 'transaction_detail'),
	url(r'^Area/(?P<Area_id>\d+)/$', ''),
)
'''
