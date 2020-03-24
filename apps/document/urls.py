"""MeraKhata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from document import views

app_name = 'document'

urlpatterns = [
    url(r'^primary/$', views.DocumentList.as_view(), name='list'),
    url(r'^single/(?P<pk>[^/.]+)/', views.DocumentDetail.as_view(), name='item'),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[^/.]+)/', views.UserDetail.as_view()),
]