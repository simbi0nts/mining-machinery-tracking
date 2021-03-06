# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator
from django.db import models


@python_2_unicode_compatible
class BrandCharacteristics(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=50, unique=True)
    max_carrying_capacity = models.IntegerField(default=0,
                                                validators=[MinValueValidator(1)])

    def __str__(self):
        return unicode(self.brand_name)


@python_2_unicode_compatible
class CurrentActiveMachines(models.Model):
    machine_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    brand_name = models.ForeignKey(BrandCharacteristics,
                                   null=False,
                                   on_delete=models.CASCADE,
                                   related_name='overload_value')
    current_carrying_load = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return unicode(self.machine_id)
