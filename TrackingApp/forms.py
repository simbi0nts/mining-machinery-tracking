# -*- coding: utf-8 -*-

from django import forms
from .models import CurrentActiveMachines, BrandCharacteristics
from django.utils.safestring import mark_safe


class BrandForm(forms.ModelForm):

    class Meta:
        model = CurrentActiveMachines
        fields = ['brand_name']

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        self.fields['brand_name'] = forms.ModelChoiceField(
            queryset=BrandCharacteristics.objects.all().order_by('brand_id'),
            label='Модель',
            empty_label=None
        )


class NewMachineForm(forms.ModelForm):

    class Meta:
        model = CurrentActiveMachines
        fields = ['machine_id', 'brand_name', 'current_carrying_load']

    def __init__(self, *args, **kwargs):
        super(NewMachineForm, self).__init__(*args, **kwargs)
        self.fields['brand_name'] = forms.ModelChoiceField(
            queryset=BrandCharacteristics.objects.exclude(brand_id=0)
        )
        self.fields['machine_id'].label = mark_safe('<br /><br />Номер машины')
        self.fields['machine_id'].empty_label = None
        self.fields['brand_name'].label = mark_safe('<br /><br /><br />Название модели')
        self.fields['brand_name'].empty_label = None

        self.fields['current_carrying_load'].label = mark_safe('<br /><br /><br />Текущий перевозимый вес')
        self.fields['current_carrying_load'].empty_label = None


class NewBrandForm(forms.ModelForm):

    class Meta:
        model = BrandCharacteristics
        fields = ['brand_name', 'max_carrying_capacity']

    def __init__(self, *args, **kwargs):
        super(NewBrandForm, self).__init__(*args, **kwargs)
        self.fields['brand_name'].label = mark_safe('<br /><br />Название модели')
        self.fields['brand_name'].empty_label = None
        self.fields['max_carrying_capacity'].label = mark_safe('<br /><br /><br />Максимальная загрузка')
        self.fields['max_carrying_capacity'].empty_label = None

