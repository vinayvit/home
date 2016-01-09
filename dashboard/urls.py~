from django.conf.urls import patterns, include, url

urlpatterns = patterns('dashboard.views',
    
    url(r'^edit/$', 'edit', name='edit'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', 'profile_edit', name='profile_edit'),
    url(r'^event/$', 'event', name='event'),
    url(r'^eventu/$', 'devent', name='devent'),
    url(r'^detail/$', 'devent_detail', name='devent_detail'),
    url(r'^event/(?P<pk>[0-9]+)/$', 'event_detail', name='event_detail'),
    url(r'^detail/(?P<pk>[0-9]+)/$', 'uevent_detail', name='uevent_detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', 'devent_edit', name='devent_edit'),

)
