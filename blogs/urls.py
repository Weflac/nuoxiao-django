# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'garden/', views.garden),
    path(r'garden/<str:num>/', views.detail),
    path(r'theme/', views.theme),
    path(r'page<int:num>/', views.detail),
    path(r'(page-(\d+)/)?/', views.detail),
    path(r'(\d+)/?/', views.detail),

    path(r'adduser/', views.add_user),
    path(r'addgarden/', views.add_garden),
    path(r'addblogs/', views.add_blogs),
    path(r'updateblogs/', views.update_blogs),
]

