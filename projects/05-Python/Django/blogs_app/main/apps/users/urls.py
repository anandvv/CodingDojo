from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index, name='index'),     # This line has changed!
    url(r'^new$', views.new, name='new'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
]
