# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='is_considered',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
