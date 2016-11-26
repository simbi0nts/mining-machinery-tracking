# -*- coding: utf-8 -*-

from django import forms
from .models import CurrentActiveMachines

class BrandForm(forms.ModelForm):

    class Meta:
        model = CurrentActiveMachines
        fields = ['brand_name']

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        self.fields['brand_name'].label = 'Модель'