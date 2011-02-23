from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import Update

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^reservation/parking', include('SKHReseravationSystem.foo.urls')),
    # (r'^reservation/parking/community', include('SKHReseravationSystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^reservation/community/$', 'Common.views.community_list'),
	url(r'^reservation/community/(?P<community_id>\d+)/$', 'Common.views.community_detail', name = "community_detail"),
    #(r'^reservation/parking/', include('SKHReseravationSystem.Parking.urls')),
    #(r'^reservation/profile/', include('SKHReseravationSystem.Common.urls')),
    (r'^reservation/update/$', 'Update.views.update'),
    #(r'^reservation/admin/', include(admin.site.urls)),
)
