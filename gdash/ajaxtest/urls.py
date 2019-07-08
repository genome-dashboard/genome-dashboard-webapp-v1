from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]
