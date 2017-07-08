from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^oauth/vk/$', views.vk, name='vk'),
    url(r'^oauth/fb/$', views.fb, name='fb'),
    url(r'^oauth/gp/$', views.gp, name='gp'),
    url(r'^oauth/ya/$', views.ya, name='ya'),
]
