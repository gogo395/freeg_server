# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151028_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='display_order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
