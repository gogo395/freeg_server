# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151005_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='co_ordinates',
            field=geoposition.fields.GeopositionField(default=b'19.101985614850385, 72.88626194000244', max_length=42, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='outlet',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(default=b'POINT(1.232433 1.2323232)', editable=False, blank=True, srid=4326, null=True, verbose_name=b'Point'),
            preserve_default=True,
        ),
    ]
