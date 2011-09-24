from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'events/', 'meetit.views.events', name='events'),
    url(r'journeys/', 'meetit.views.journeys', name='journeys'),
    url(r'download/cal/(?P<filename>.*)/$', 'meetit.views.download', name='download'),
    url(r'^$', 'meetit.views.signup', name='signup'),

    # url(r'^admin/', include(admin.site.urls)),
)


if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r'%s(?P<path>.*)/$' % settings.MEDIA_URL[1:], 'static.serve', {
            "document_root": settings.MEDIA_ROOT,
        })
    )

