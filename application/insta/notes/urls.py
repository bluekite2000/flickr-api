from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from notes.views import *



urlpatterns = patterns('notes.views',
    url(r'^$', 'index', name="index"),
      url(r'^flickr-callback/$',  'flickr_callback', name="flickr_callback"),


)

