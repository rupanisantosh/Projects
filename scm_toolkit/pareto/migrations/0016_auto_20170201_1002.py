# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 04:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pareto', '0015_remove_abc_multi_loc_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abc_multi_loc',
            old_name='Item_id',
            new_name='item_id',
        ),
    ]
