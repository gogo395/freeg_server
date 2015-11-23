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
from app.models import Suggestions, Review, Outlet


@csrf_exempt
def get_settings(request):
    data={}
    data['FAQ']="Q1: alsdjf opajelkrjalnv ?\nAns:ajsofijwnbfvolknwkefnipn skdfj pwoenrpkwen . \nQ2:aoiwhefnw owihef woewmekrjgpiw n? \nAns: kajspfeiwgnb pwjepk nwpekwe mgpwkenbp."
    data=json.dumps(data)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def add_hotspot(request):
    name= request.POST.get('name')
    address= request.POST.get('address')
    city= request.POST.get('city')
    comments= request.POST.get('comments')
    if not Suggestions.objects.filter(name=name,city=city,address=address):
        Suggestions(name=name,city=city,address=address,comments=comments).save()
    return HttpResponse("done",content_type="application/json")


@csrf_exempt
def add_review(request):
    outlet_id = request.POST.get('outlet_id')
    rating = request.POST.get('rating')
    review = request.POST.get('reviews')
    outlet = Outlet.objects.get(pk=outlet_id)
    Review(outlet=outlet,rating=rating,review=review).save()
    return HttpResponse("done",content_type="application/json")
