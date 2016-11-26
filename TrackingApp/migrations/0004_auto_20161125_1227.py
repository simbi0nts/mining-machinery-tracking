# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 09:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackingApp', '0003_currentactivemachines_overload_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentactivemachines',
            name='overload_value',
        ),
        migrations.AlterField(
            model_name='brandcharacteristics',
            name='max_carrying_capacity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='currentactivemachines',
            name='brand_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overload_value', to='TrackingApp.BrandCharacteristics'),
        ),
    ]