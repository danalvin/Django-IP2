from . import views
from django.conf.urls import url
from django.conf import settings

urlpatterns=[
    url('^$', views.home,name='Instagram')
]
