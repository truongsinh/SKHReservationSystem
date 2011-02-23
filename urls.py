from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import Update

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:

    (r'^reservation/community/$', 'Common.views.community_list', "community_list"),
	url(r'^reservation/community/(?P<community_id>\d+)/$', 'Common.views.community_detail', name = "community_detail"),
    url(r'^reservation/profile/(?P<user_id>\d+)/$', 'Common.views.profile', name = "profile"),


    (r'^reservation/community/(?P<community_id>\d+)/parking$', 'Parking.views.index'),

    (r'^reservation/community/(?P<community_id>\d+)/parking/queue/$', 'Parking.views.queue_list'),
    url(r'^reservation/parking/queue/add/$', 'Parking.views.queue_add', name='queue_add'), #POST
    url(r'^reservation/parking/queue/(?P<queue_id>\d+)/$', 'Parking.views.queue_detail', name='queue_detail'),

    (r'^reservation/community/(?P<community_id>\d+)/parking/reservation/$', 'Parking.views.reservation_list'),
    url(r'^reservation/parking/reservation/add/$', 'Parking.views.reservation_add', name='reservation_add'), #POST
    url(r'^reservation/parking/reservation/(?P<transaction_id>\d+)/$', 'Parking.views.reservation_detail', name='reservation_detail'),


	#url(r'^Area/(?P<Area_id>\d+)/$', ''),


    (r'^reservation/parking/', include('SKHReseravationSystem.Parking.urls')),
    (r'^reservation/update/$', 'Update.views.update'),
    (r'^reservation/admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^reservation/admin/', include(admin.site.urls)),
)
