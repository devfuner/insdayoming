from django.conf.urls import url
from instagram.views import index, upload, detail, update, remove, like

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^upload/', upload, name='upload'),
    url(r'^detail/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', update, name='update'),
    url(r'^remove/(?P<pk>[0-9]+)/$', remove, name='remove'),
    url(r'^like/', like, name='like'),
]
