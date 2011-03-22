from django.conf.urls.defaults import *

urlpatterns = patterns('fb_realtime.views',
    url(r'^fb_callback$',
        'callback_handler',
        name='fb_callback'),
)
