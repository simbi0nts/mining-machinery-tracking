# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackingApp', '0006_remove_currentactivemachines_overload_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandcharacteristics',
            name='brand_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
