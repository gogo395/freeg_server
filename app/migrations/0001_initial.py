# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=500)),
                ('nick_name', models.CharField(max_length=100)),
                ('category', models.IntegerField(choices=[(0, b'Cafes'), (1, b'Restaurants'), (2, b'Salons & Spas'), (3, b'Fitness'), (4, b'Entertainment'), (5, b'Hotels'), (6, b'Others')])),
                ('brief', models.TextField()),
                ('recommended_for', models.TextField()),
                ('logo', models.CharField(max_length=100, null=True, blank=True)),
                ('outer_image', models.CharField(max_length=100, null=True, blank=True)),
                ('phone_no_primary', models.CharField(max_length=100)),
                ('phone_no_secondary', models.CharField(max_length=100, null=True, blank=True)),
                ('co_ordinates', geoposition.fields.GeopositionField(default=b'19.101985614850385, 72.88626194000244', max_length=42, blank=True)),
                ('full_address', models.TextField()),
                ('landmark', models.CharField(max_length=100, null=True, blank=True)),
                ('cost_for_two', models.CharField(max_length=100, null=True, blank=True)),
                ('price_for_one_coffee_mug', models.CharField(max_length=100, null=True, blank=True)),
                ('rating', models.FloatField(default=0)),
                ('no_of_tables', models.IntegerField(default=0)),
                ('total_seating_capacity', models.IntegerField(default=0)),
                ('location', models.ForeignKey(to='app.Location')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=25, null=True)),
                ('app_id', models.CharField(max_length=250, null=True, blank=True)),
                ('app_version', models.CharField(max_length=10, null=True, blank=True)),
                ('device_id', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wifi_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('wifI_ssid', models.CharField(max_length=500)),
                ('free_wifi_time', models.IntegerField(default=0, help_text=b'Minutes')),
                ('quoted_speed', models.FloatField(help_text=b'Mbps')),
                ('avg_realized_speed', models.FloatField(help_text=b'Mbps')),
                ('wiFi_performance', models.FloatField(help_text=b'%')),
                ('wiFi_login_method', models.TextField()),
                ('wiFi_provider', models.CharField(max_length=500)),
                ('wiFi_purchase', models.CharField(help_text=b'after free time', max_length=500)),
                ('wiFi_purchase_process', models.TextField()),
                ('ipass_enabled', models.BooleanField(default=False)),
                ('boingo_enabled', models.BooleanField(default=False)),
                ('wiFi_captive_portal_provider', models.CharField(max_length=500)),
                ('wiFi_login_steps', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='outlet',
            name='wifi',
            field=models.ManyToManyField(to='app.Wifi_Details'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('city', 'area')]),
        ),
    ]
