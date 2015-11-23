from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from app import resources
from app import views

v1_api = Api(api_name='v1')

v1_api.register(resources.OutletResource())
v1_api.register(resources.UserResource())
v1_api.register(resources.LocationResource())
v1_api.register(resources.CatResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freeG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/add_hotspot', views.add_hotspot, name='add_hotspot'),
    url(r'^api/v1/get_settings$', views.get_settings, name='get_settings'),
    (r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
