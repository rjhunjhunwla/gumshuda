from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^upload$', views.upload, name='upload'),
    url(r'^$', 'sighting.views.login'),
    url(r'home/$', 'sighting.views.home'),
    url(r'logout/$', 'sighting.views.logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)