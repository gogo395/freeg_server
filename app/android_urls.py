__author__ = 'anuragmeena'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from app import resources
from app import views

urlpatterns = patterns('',
    # Examples:
    url(r'^v1/get_settings$', views.get_settings, name='get_settings'),

)
