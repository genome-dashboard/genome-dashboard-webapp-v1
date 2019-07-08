"""
gdash.dalliance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


# Test embedded apps (dalliance, jbrowse, igb, jsmol, nglviewer, GIVE, etc.).
app_name = 'embedded'   # Namespace the app urls.

# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.
urlpatterns = [
     url(r'^$', views.index, name='index'),
     # url(r'^dalliance/$', TemplateView.as_view(template_name="dalliance.html")),
     url(r'^dalliance/$', views.DallianceView.as_view(), name='dalliance'),
     # url(r'^give/$', TemplateView.as_view(template_name="give.html")),
     url(r'^give/$', views.GiveView.as_view(), name='give'),
     # These pages not yet created...
     # url(r'^jbrowse/', include('jbrowse.urls')),  # Test jbrowse embed.
     # url(r'^igb/', include('igb.urls')),  # Test igb embed.
     # url(r'^jsmol/', include('jsmol.urls')),  # Test jsmol embed.
     # url(r'^nglviewer/', include('nglviewer.urls')),  # Test nglviewer embed.
]
