from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from dashing.utils import router
from registration.backends.default.views import RegistrationView
from django_messages.views import *
from dashboard.views import *
urlpatterns = [
    # Examples:
    url(r'^messages/', include('django_messages.urls')),
    #url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
 # MAIN:
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    url(r'^blank/$', 'ecommerce2.views.blank', name='blank'),  
    url(r'^faq/$', 'ecommerce2.views.faq', name='faq'),
    url(r'^services/$', 'ecommerce2.views.services', name='services'),
    url(r'^term/$', 'ecommerce2.views.term', name='term'),
    url(r'^gallery/$', 'ecommerce2.views.gallery', name='gallery'),
 # Dashboard:
    url(r'^dashboard/$', 'dashboard.views.dashboard', name='dashboard'),   
    url(r'^profiles/$', 'dashboard.views.profiles', name='profiles'),
    #url(r'^dashboard/', include(router.urls)),
 # Product:
     url(r'^$', 'products.views.home', name='home'),
    url(r'^products/', include('products.urls')),
    url(r'^producthistory/$', 'products.views.post_history', name='post_history'),
    url(r'^detail/product/(?P<pk>[0-9]+)/$', 'products.views.post_detail_history', name='post_detail_history'),
    url(r'^servicehistory/$', 'products.views.service_history', name='service_history'),
    url(r'^servicelist/$', 'products.views.servicelist', name='servicelist'),    
    url(r'^detail/service/(?P<pk>[0-9]+)/$', 'products.views.service_detail_history', name='service_detail_history'),
    url(r'^service/(?P<pk>[0-9]+)/$', 'products.views.service_detail_home', name='service_detail_home'),
    #service
    url(r'^servicehistory/$', 'products.views.service_history', name='service_history'),
 # Admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^profile/', include('user_profile.urls')),
    # Django JET URLS
    url(r'^jet/', include('jet.urls', 'jet')), 
    url(r'^tour/$', 'ecommerce2.views.tour', name='tour'),
    url(r'^dashboard/', include('dashboard.urls')),
 #events
    url(r'^events/$', 'dashboard.views.event', name='event'), 
    url(r'^event/(?P<pk>[0-9]+)/$', 'dashboard.views.event_detail', name='event_detail'),  
 #service
    url(r'^service/enquiry/$', 'django_messages.views.enquiry', name='enquiry'),
    url(r'^service/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'^service/(?P<pk>[0-9]+)/edit/$', 'products.views.post_edit_service', name='post_edit_service'),
    url(r'^offer/service/$', 'products.views.service', name='service'),
    url(r'^offer/service/(?P<pk>[0-9]+)/$', 'products.views.post_detail_service', name='post_detail_service'),
# event    
    url(r'^event/enquiry/$', 'django_messages.views.enquiry', name='enquiry'),
    url(r'^event/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'^eventhistory/$', 'dashboard.views.devent_detail', name='devent_detail'),
    url(r'^detail/event/(?P<pk>[0-9]+)/$', 'dashboard.views.uevent_detail', name='uevent_detail'),
    url(r'^event/edit/(?P<pk>[0-9]+)/$', 'dashboard.views.devent_edit', name='devent_edit'),
    url(r'^host/event/$', 'dashboard.views.devent', name='devent'),
    url(r'^host/event/(?P<pk>[0-9]+)/$', 'dashboard.views.event_detail', name='event_detail'),
    url(r'^event/detail/(?P<pk>[0-9]+)/$', 'dashboard.views.uevent_detail', name='uevent_detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
