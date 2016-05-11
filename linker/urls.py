from django.conf.urls import patterns, url

urlpatterns = patterns('linker.views',
    url(r'^list/$', 'list', name='list'),
)
