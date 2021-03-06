# -*- coding: utf-8 -*-

"""django_reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include

from tmex import views

urlpatterns = [
    url(r'^$', views.frontPage, name="frontpage"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signout/$', views.signout, name="signout"),

    url(r'^about/$', views.about, name="about"),
    url(r'^start/$', views.start, name="start"),
    url(r'^attorney/$', views.attorney, name="attorney"),
    url(r'^help/$', views.help, name="help"),
    url(r'^price/$', views.price, name="price"),
    url(r'^restore/$', views.restore, name="restore"),
]
