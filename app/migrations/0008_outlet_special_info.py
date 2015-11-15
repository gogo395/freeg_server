# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151108_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='special_info',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
