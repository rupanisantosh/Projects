# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pareto', '0009_remove_abc_multi_loc_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc_multi_loc',
            name='user_id',
            field=models.CharField(default=1, editable=False, max_length=15),
        ),
    ]
