# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index),
    url(r'^garden$', views.garden),
    url(r'^theme$', views.theme),
    url(r'^(\d+)/?$', views.detail),
]

