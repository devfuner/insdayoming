from django.conf.urls import url
from instagram.views import index, upload, detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^upload/', upload, name='upload'),
    url(r'^detail/(?P<pk>[0-9]+)/$', detail, name='detail'),
]
