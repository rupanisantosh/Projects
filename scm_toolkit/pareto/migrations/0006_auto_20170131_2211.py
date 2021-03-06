# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 16:41
from __future__ import unicode_literals

import cuser.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pareto', '0005_auto_20170131_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc_multi_loc',
            name='creator',
            field=cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_mymodels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abc_multi_loc',
            name='last_editor',
            field=cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_edited_mymodels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='abc_multi_loc',
            name='user_id',
            field=models.CharField(default=1, editable=False, max_length=15),
        ),
    ]
