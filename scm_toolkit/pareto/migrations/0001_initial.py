# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abc_multi_loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('Item_id', models.CharField(max_length=15)),
                ('item_desc', models.CharField(max_length=80)),
                ('loc_id', models.CharField(max_length=15)),
                ('loc_desc', models.CharField(max_length=50)),
                ('loc_type', models.CharField(max_length=20)),
                ('sales', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
