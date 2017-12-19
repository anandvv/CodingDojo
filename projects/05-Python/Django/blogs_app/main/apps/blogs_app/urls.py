from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index, name='index'),     # This line has changed!
    url(r'^display$', views.display, name='display'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<blog_id>[-+]?[0-9]+)$', views.show, name='show'),
    url(r'^(?P<blog_id>[-+]?[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<blog_id>[-+]?[0-9]+)/delete$', views.delete, name='delete'),
]
