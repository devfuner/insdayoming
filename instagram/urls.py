from django.conf.urls import url
from instagram.views import upload

urlpatterns = [
    url(r'^upload/', upload, name='upload'),
]
