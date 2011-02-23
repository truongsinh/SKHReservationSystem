from django.conf.urls.defaults import *
from Update.views import *

urlpatterns = patterns('',
    (r'^$', update),
)
