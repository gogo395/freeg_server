from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# from django.contrib.gis.geos import *
#     from django.contrib.gis.measure import D
#
#     distance = 2000
#     ref_location = Point(1.232433, 1.2323232)
#
#     res = yourmodel.objects.filter(location__distance_lte=(ref_location, D(m=distance))).distance(ref_location).order_by('distance')
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_settings(request):
    data={}
    data['FAQ']="Q1: alsdjf opajelkrjalnv ?\nAns:ajsofijwnbfvolknwkefnipn skdfj pwoenrpkwen . \nQ2:aoiwhefnw owihef woewmekrjgpiw n? \nAns: kajspfeiwgnb pwjepk nwpekwe mgpwkenbp."
    data=json.dumps(data)
    return HttpResponse(data, content_type='application/json')
