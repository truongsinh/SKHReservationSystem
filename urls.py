from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:

    (r'^reservation/community/$', 'Common.views.community_list', {'page': '1'}),
    (r'^reservation/community/page_(?P<page>\d+)$', 'Common.views.community_list'),
	(r'^reservation/community/(?P<community_id>\d+)/$', 'Common.views.community_detail'),

    (r'^reservation/community/(?P<community_id>\d+)/parking/$', 'Parking.views.index'),

    (r'^reservation/community/(?P<community_id>\d+)/parking/area/$', 'Parking.views.area_list', {'page': '1'}),
    (r'^reservation/community/(?P<community_id>\d+)/parking/area/page_(?P<page>\d+)$', 'Parking.views.area_list'),

    (r'^reservation/community/(?P<community_id>\d+)/parking/queue/$', 'Parking.views.queue_list', {'page': '1'}),
    (r'^reservation/community/(?P<community_id>\d+)/parking/queue/page_(?P<page>\d+)$', 'Parking.views.queue_list'),
	
    (r'^reservation/community/(?P<community_id>\d+)/parking/reservation/$', 'Parking.views.reservation_list', {'page': '1'}),
    (r'^reservation/community/(?P<community_id>\d+)/parking/reservation/page_(?P<page>\d+)$', 'Parking.views.reservation_list'),

    (r'^reservation/profile/(?P<user_id>\d+)/$', 'Common.views.profile'),


    (r'^reservation/parking/area/(?P<area_id>\d+)/$', 'Parking.views.area_detail'),

    (r'^reservation/parking/queue/add/$', 'Parking.views.queue_add'), #POST
    (r'^reservation/parking/queue/(?P<queue_id>\d+)/$', 'Parking.views.queue_detail'),

    (r'^reservation/parking/reservation/add/$', 'Parking.views.reservation_add'), #POST
    (r'^reservation/parking/reservation/(?P<transaction_id>\d+)/$', 'Parking.views.reservation_detail'),


	#url(r'^Area/(?P<Area_id>\d+)/$', ''),


    #(r'^reservation/parking/', include('SKHReseravationSystem.Parking.urls')),
    (r'^reservation/update/$', 'Update.views.update'),
    (r'^reservation/admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^reservation/admin/', include(admin.site.urls)),

	#(r'^', 'Common.views.PageNotFound'),
)
