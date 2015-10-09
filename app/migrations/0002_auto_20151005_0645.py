# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlet',
            name='co_ordinates',
        ),
        migrations.AddField(
            model_name='outlet',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(default=b'POINT(1.232433 1.2323232)', srid=4326, verbose_name=b'Point'),
            preserve_default=True,
        ),
    ]
