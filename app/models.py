from django.contrib.auth.models import User
from django.contrib.gis.geos.point import Point
from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.gis.db import models as gis_models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(BaseModel):
    name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=25)
    contact = models.CharField(max_length=25,null=True)
    app_id = models.CharField(max_length=250, blank=True, null=True)
    app_version = models.CharField(max_length=10, blank=True, null=True)
    device_id = models.CharField(max_length=300, blank=True, null=True)
    def __unicode__(self):
        return self.user.email


class Location(BaseModel):
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    class Meta:
        unique_together = ('city', 'area',)

    def __unicode__(self):
        return self.area+", "+self.city

class Category(BaseModel):
    name=models.CharField(max_length=50,unique=True)
    is_active=models.BooleanField(is_active=False);
    display_order=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name


class Outlet(BaseModel):
    full_name=models.CharField(max_length=500)
    nick_name=models.CharField(max_length=100)
    cat =models.ForeignKey(Category,null=True,blank=False)
    brief=models.TextField()
    recommended_for=models.TextField()
    logo=models.CharField(max_length=100,null=True,blank=True)
    outer_image=models.CharField(max_length=100,null=True,blank=True)
    phone_no_primary=models.CharField(max_length=100)
    phone_no_secondary=models.CharField(max_length=100,null=True,blank=True)
    co_ordinates=GeopositionField(blank=True, default='19.101985614850385, 72.88626194000244')
    position=gis_models.PointField(null=True, blank=True,editable=False, srid=4326, verbose_name="Point",default='POINT(1.232433 1.2323232)')

    full_address=models.TextField()
    landmark=models.CharField(max_length=100,null=True,blank=True)
    location=models.ForeignKey(Location)
    cost_for_two=models.CharField(max_length=100,null=True,blank=True)
    price_for_one_coffee_mug=models.CharField(max_length=100,null=True,blank=True)
    rating=models.FloatField(default=0)
    no_of_tables=models.IntegerField(default=0)
    total_seating_capacity=models.IntegerField(default=0)
    # wifi = models.ManyToManyField(Wifi_Details)

    wifI_ssid=models.CharField(max_length=500,default="")
    free_wifi_time=models.IntegerField(default=0,help_text='Minutes') #(minutes)
    quoted_speed = models.FloatField(help_text="Mbps",default=0) #(mbps)
    avg_realized_speed = models.FloatField(help_text="Mbps",default=0)#(mbps)
    wiFi_performance = models.FloatField(help_text="%",default=0)#(%)
    wiFi_login_method=models.TextField(default="")
    wiFi_provider=models.CharField(max_length=500,default="")
    wiFi_purchase=models.CharField(max_length=500,help_text='after free time',default="") #()
    wiFi_purchase_process=models.TextField(default="")
    ipass_enabled=models.BooleanField(default=False)
    boingo_enabled=models.BooleanField(default=False)
    wiFi_captive_portal_provider=models.CharField(max_length=500,default="")
    wiFi_login_steps=models.TextField(default="")

    # def __unicode__(self):
    #     return self.wifI_ssid+", "+self.wiFi_provider
    def __unicode__(self):
        return self.nick_name+", "+str(self.location)

    def save(self, *args, **kwargs):
        self.position = 'POINT('+str(self.co_ordinates.latitude)+" "+str(self.co_ordinates.longitude)+")"
        print self.position.json
        print self.co_ordinates
        super(Outlet, self).save(*args, **kwargs)