"""
gdash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import include, url
from django.contrib import admin
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect

from . import views


app_name = 'gdash_root'   # Namespace the app urls.

# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Example.
    url(r'^simpleview/', include('simpleview.urls')),

    # Demo Apps.
    url(r'^polls/', include('polls.urls')),
    url(r'^ajaxtest/', include('ajaxtest.urls')),

    # Embed Tests.
    url(r'^embedded/', include('embedded.urls')),

    # Django Admin.
    url(r'^admin/', admin.site.urls),
]
