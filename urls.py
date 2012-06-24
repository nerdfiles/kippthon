from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^kippt/lists/$', 'views.lists'),
  url(r'^kippt/lists/(?P<limit>\d+)/$', 'views.lists'),
  url(r'^kippt/search/(?P<q>[A-Za-z\+]*)/$', 'views.search'),
  url(r'^kippt/search/(?P<q>[A-Za-z\+]*)/(?P<limit>\d+)/$', 'views.search'),
  url(r'^dashboard/', include(admin.site.urls)),
  url(r'^', include('cms.urls')),
)

if settings.DEBUG:
  urlpatterns = patterns('',
    url(r'^_assets/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
  ) + urlpatterns

