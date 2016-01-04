from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^$', views.index),
    url(r'home/$', views.home),
    url(r'logout/$', views.logout),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)