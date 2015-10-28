__author__ = 'anuragmeena'
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource
from tastypie.contrib.gis.resources import ModelResource as GeoModelResource
from app.models import *
from tastypie import fields
from django.contrib.auth.models import User


class UserResource(ModelResource):

    class Meta:
        queryset = UserProfile.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = "user"
        include_resource_uri = False
        authentication=Authentication()
        authorization = Authorization()
        # fields=['email','username',]
        # filtering = {
        #     'id' : ALL,
        #     'email' :ALL,
        #     'username' :ALL
        # }


class LocationResource(ModelResource):

    class Meta:
        queryset = Location.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = "location"
        include_resource_uri = False
        authentication=Authentication()
        authorization = Authorization()
        # fields=['city','username',]
        # filtering = {
        #     'id' : ALL,
        #     'email' :ALL,
        #     'username' :ALL
        # }


class OutletResource(ModelResource):

    class Meta:
        queryset = Outlet.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = "outlet"
        include_resource_uri = False
        authentication=Authentication()
        authorization = Authorization()
        # fields=['email','username',]
        excludes=['created_at','modified_at']
        filtering = {
            'id':ALL,
            'cat' : ALL,
        #     'email' :ALL,
        #     'username' :ALL
        }

