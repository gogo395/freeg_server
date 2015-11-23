# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_suggestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('rating', models.FloatField()),
                ('review', models.TextField(default=b'', null=True, blank=True)),
                ('outlet', models.ForeignKey(to='app.Outlet')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
