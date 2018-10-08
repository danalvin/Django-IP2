from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.all_images,name='Instagram'),
    url(r'^what_profile/(?P<profile_id>\d+)', views.my_profile, name='profile'),
    url(r'^explore_more/', views.explore, name='my_explore'),
    url(r'^new/image$', views.new_image, name='new_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)