from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^reservation/parking', include('SKHReseravationSystem.foo.urls')),
    # (r'^reservation/parking/community', include('SKHReseravationSystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^reservation/parking/', include('SKHReseravationSystem.Parking.url')),
    (r'^reservation/profile/', include('SKHReseravationSystem.Common.url')),
    (r'^reservation/update/', include('SKHReseravationSystem.Update.url')),
    (r'^reservation/admin/', include(admin.site.urls)),
)
