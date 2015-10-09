from django.shortcuts import render

# Create your views here.

# from django.contrib.gis.geos import *
#     from django.contrib.gis.measure import D
#
#     distance = 2000
#     ref_location = Point(1.232433, 1.2323232)
#
#     res = yourmodel.objects.filter(location__distance_lte=(ref_location, D(m=distance))).distance(ref_location).order_by('distance')