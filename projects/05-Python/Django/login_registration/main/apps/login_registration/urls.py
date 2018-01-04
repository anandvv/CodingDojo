from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    # url(r'^(?P<user_id>\d+)$', views.show),
    # url(r'^(?P<user_id>\d+)/delete$', views.delete),
    # url(r'^new$', views.new),
    # url(r'^create$', views.create),
    # url(r'^(?P<user_id>\d+)/edit$', views.edit)
]
