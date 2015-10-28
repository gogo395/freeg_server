# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151005_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='outlet',
            name='wifi',
        ),
        migrations.DeleteModel(
            name='Wifi_Details',
        ),
        migrations.AddField(
            model_name='outlet',
            name='avg_realized_speed',
            field=models.FloatField(default=0, help_text=b'Mbps'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='boingo_enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='cat',
            field=models.ForeignKey(to='app.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='free_wifi_time',
            field=models.IntegerField(default=0, help_text=b'Minutes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='ipass_enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='quoted_speed',
            field=models.FloatField(default=0, help_text=b'Mbps'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_captive_portal_provider',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_login_method',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_login_steps',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_performance',
            field=models.FloatField(default=0, help_text=b'%'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_provider',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_purchase',
            field=models.CharField(default=b'', help_text=b'after free time', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wiFi_purchase_process',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outlet',
            name='wifI_ssid',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
