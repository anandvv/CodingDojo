from django.conf.urls import url
  from . import views           # This line is new!
  urlpatterns = [
    url(r'^$', views.index)     # This line has changed! Look for empty string after stripping out the '/'
  ]