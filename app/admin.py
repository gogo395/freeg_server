from django.contrib import admin
from app.models import Outlet, Wifi_Details, Location, UserProfile

admin.site.register(Outlet)
admin.site.register(Location)
admin.site.register(Wifi_Details)
admin.site.register(UserProfile)