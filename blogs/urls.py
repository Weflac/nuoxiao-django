# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='home'),
    path(r'index', views.index, name='index'),
    path(r'garden/', views.garden, name='garden'),
    path(r'garden/list-<int:type>/', views.garden_list, name='gardenlist'),
    path(r'garden/<int:id>/', views.detail, name='detail'),
    path(r'theme/', views.theme, name='theme'),
    path(r'404/', views.notfound, name='notfound' ),

    path(r'adduser/', views.add_user),
    path(r'addgarden/', views.add_garden),
    path(r'addblogs/', views.add_blogs),
    path(r'updateblogs/', views.update_blogs),
]

