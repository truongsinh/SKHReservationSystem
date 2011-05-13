from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'Common.views.home'),#
    (r'^reservation/$', 'Common.views.index'),#
    (r'^reservation/community/$', 'Common.views.community_list',),#+
	(r'^reservation/community/(?P<community_id>\d+)/$', 'Common.views.community_detail'),#+
	(r'^reservation/community/(?P<community_id>\d+)/$', 'Common.views.reserved'),#+

    #(r'^reservation/community/(?P<community_id>\d+)/parking/$', 'Parking.views.index'),#

    #(r'^reservation/areas/$', 'Common.views.area_list'),
    #(r'^reservation/community/(?P<community_id>\d+)/area/page_(?P<page>\d+)$', 'Parking.views.area_list'),
	#(r'^reservation/community/(?P<community_id>\d+)/area/(?P<area_id>\d+)/$', 'Parking.views.area_detail'), #+
	#(r'^reservation/community/area/(?P<area_id>\d+)/$', 'Parking.views.area_detail'),

    (r'^reservation/queue/$', 'Common.views.queue_list',),
	(r'^reservation/queue/(?P<queue_id>\d+)/$', 'Common.views.queue_detail'),

    (r'^reservation/community/(?P<community_id>\d+)/parking/reservation/$', 'Parking.views.reservation_list',),
    (r'^reservation/community/(?P<community_id>\d+)/parking/reservation/page_(?P<page>\d+)$', 'Parking.views.reservation_list'),
    (r'^reservation/parking/reservation/(?P<transaction_id>\d+)/$', 'Parking.views.reservation_detail'),


	#url(r'^Area/(?P<Area_id>\d+)/$', ''),
    (r'^reservation/accounts/$', 'Common.views.account_list'),
    (r'^reservation/profile/$', 'Common.views.profile'),
	(r'^reservation/permissions_warning/$', 'Common.views.permissions_warning'),
	(r'^reservation/reserved/$', 'Common.views.reserved'),
	(r'^reservation/login/$', 'django.contrib.auth.views.login', {'template_name': 'Common/login.html'}),
	(r'^reservation/password/$', 'django.contrib.auth.views.password_change', {'template_name': 'Common/password.html'}),
	(r'^reservation/password/changed/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'Common/password_changed.html'}),
	(r'^reservation/logout/$', 'Common.views.logout'),

	(r'^reservation/admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^reservation/admin/', include(admin.site.urls)),
	(r'^reservation/update/$', 'Update.views.update'),
)
urlpatterns += staticfiles_urlpatterns()