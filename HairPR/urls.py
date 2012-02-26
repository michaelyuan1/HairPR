from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   
    url(r'^$', 'users.views.home'),
	url(r'^submitEmail/$', 'users.views.submitEmail'),
    # url(r'^HairPR/', include('HairPR.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	
)
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
		#(r'^static/(P.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
)