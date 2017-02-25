"""bookexplorer URL Configuration

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
from django.views.generic import TemplateView
from . import views

app_name = 'site'

urlpatterns = [
    # ex: /site/
    #url(r'^$', TemplateView.as_view(template_name='site/index.html')),
    # url(r'^list/$', views.list, name='list'),
    # url(r'^(?P<book1>[0-9]+)/(?P<book2>[0-9]+)/(?P<pos>[0-9]+)/compareT/$', views.compareT, name='compareT'),
    # url(r'^(?P<book>[0-9]+)/analyze/$', views.analyze, name='analyze'),
    # url(r'^(?P<book1>[0-9]+)/(?P<book2>[0-9]+)/(?P<pos>[0-9]+)/compare/$', views.compare, name='compare'),

    url(r'^list/$', views.list, name='list'),
    url(r'^(?P<pos>[0-9]+)/pol/$', views.polarity, name='polarity'),
    url(r'^(?P<pos>[0-9]+)/subj/$', views.subjectivity, name='subjectivity'),
    url(r'^(?P<pos>[0-9]+)/words/$', views.words, name='words'),
    url(r'^similarity/$', views.similarity, name='similarity'),
    url(r'^condense/$', views.condense, name='condense'),


]
