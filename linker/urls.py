from django.conf.urls import patterns, url
from views import ListAll

urlpatterns = patterns('linker.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^list_all/$', ListAll.as_view()),
)
