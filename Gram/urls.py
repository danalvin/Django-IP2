from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.all_images,name='Instagram')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)