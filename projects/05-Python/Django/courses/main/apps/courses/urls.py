from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),     # This line has changed!
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<course_id>\d+)/delete$', views.delete),
]
