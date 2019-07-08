"""
gdash.simpleview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url

from . import views


app_name = 'simpleview'   # Namespace the app urls.

# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.
urlpatterns = [
     url(r'^$', views.index, name='index'),
]
