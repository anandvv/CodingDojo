"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.time_display import views as time_displayViews
from apps.random_word import views as random_wordViews
from apps.survey_form import views as survey_formViews
from apps.session_words import views as session_wordsViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time_display/$', time_displayViews.index),
    url(r'^random_word/$', random_wordViews.index),
    url(r'^survey_form/$', survey_formViews.index),
    url(r'^survey_form/create', survey_formViews.create),
    url(r'^session_words/$', session_wordsViews.index),
    url(r'^session_words/process', session_wordsViews.process),
    url(r'^session_words/clear', session_wordsViews.clear)
]

