# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 04:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pareto', '0012_abc_multi_loc_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abc_multi_loc',
            name='user_id',
        ),
    ]
