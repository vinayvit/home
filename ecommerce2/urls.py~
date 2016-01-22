from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from dashing.utils import router
from registration.backends.default.views import RegistrationView


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
    url(r'^history/$', 'products.views.post_history', name='post_history'),
    url(r'^history/add/(?P<pk>[0-9]+)/$', 'products.views.post_detail_history', name='post_detail_history'),
    url(r'^historyS/$', 'products.views.service_history', name='service_history'),
    url(r'^servicelist/$', 'products.views.servicelist', name='servicelist'),    
    url(r'^history/service/(?P<pk>[0-9]+)/$', 'products.views.service_detail_history', name='service_detail_history'),
    url(r'^service/(?P<pk>[0-9]+)/$', 'products.views.service_detail_home', name='service_detail_home'),
    #service
    url(r'^historyS/$', 'products.views.service_history', name='service_history'),
 # Admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^profile/', include('user_profile.urls')),
    # Django JET URLS
    url(r'^jet/', include('jet.urls', 'jet')), 
    url(r'^tour/$', 'ecommerce2.views.tour', name='tour'),
    url(r'^dashboard/', include('dashboard.urls')),
   
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
