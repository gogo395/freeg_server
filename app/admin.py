from django.contrib import admin
from app.models import Outlet, Location, UserProfile

class OutletAdmin(admin.ModelAdmin):
    list_display = ('full_name','category','phone_no_primary',)
    list_filter = ('category','location')

admin.site.register(Outlet,OutletAdmin)
admin.site.register(Location)
admin.site.register(UserProfile)