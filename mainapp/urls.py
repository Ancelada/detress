from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='index'),
    url(r'^level/(?P<level>[0-9]+)/unit/(?P<unit_id>[0-9]+)/$', views.unit_page, name='unit_page'),
]