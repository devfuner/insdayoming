from django.conf.urls import url
from community.views import write, list, view

urlpatterns = [
    url(r'^write/', write, name='write'),
    url(r'^list/', list, name='list'),
    url(r'^view/(?P<num>[0-9]+)/$', view),
]
