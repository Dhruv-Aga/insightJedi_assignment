"""InsightJedi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    url(r'^document/', include('document.urls', namespace='document')),
    # enable the admin interface
    url(r'^admin/', admin.site.urls),
]
