'''from django.conf.urls.defaults import *

urlpatterns = patterns('Common.views',
    (r'^Common/$', 'index'),
	(r'^Common/(?P<Community_id>\d+)/$', 'community_detail'),
)
'''