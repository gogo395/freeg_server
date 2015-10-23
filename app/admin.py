from django.contrib import admin
from app.models import Outlet, Wifi_Details, Location, UserProfile

class OutletAdmin(admin.ModelAdmin):
    list_display = ('full_name','category','phone_no_primary',)
    list_filter = ('category','location','wifi')

admin.site.register(Outlet)
admin.site.register(Location)
admin.site.register(Wifi_Details)
admin.site.register(UserProfile)