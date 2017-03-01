# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pareto', '0019_delete_abc_multi_loc'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc_multiloc_analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=15)),
                ('item_desc', models.CharField(blank=True, default=None, max_length=80)),
                ('loc_id', models.CharField(max_length=15)),
                ('loc_desc', models.CharField(blank=True, default=None, max_length=50)),
                ('loc_type', models.CharField(blank=True, default=None, max_length=20)),
                ('sales', models.FloatField(blank=True, default=None, null=True)),
                ('cum_sum', models.FloatField(blank=True, default=None, null=True)),
                ('ABC_Class', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('creator', models.CharField(default=None, max_length=20)),
                ('last_editor', models.CharField(default=None, max_length=20)),
            ],
        ),
    ]
