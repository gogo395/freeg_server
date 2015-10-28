from django.contrib import admin
from app.models import Outlet, Location, UserProfile, Category


class OutletAdmin(admin.ModelAdmin):
    list_display = ('full_name','cat','phone_no_primary',)
    list_filter = ('cat','location')

admin.site.register(Outlet,OutletAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(UserProfile)