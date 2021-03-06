# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import BrandForm, NewMachineForm, NewBrandForm
from .models import CurrentActiveMachines, BrandCharacteristics
from django.db.models import F
from django.shortcuts import render
from jinja2 import Environment, PackageLoader

HUNDRED_PERCENT = 100
env = Environment(loader=PackageLoader('TrackingApp', 'templates'))


def create_filter_for_all_objects():

    # TODO: Maybe there is more correct way to define this function in code
    # Adding select option for choosing all active machines from DB
    BrandCharacteristics.objects.get_or_create(
        brand_id=0,
        brand_name="Все",
        max_carrying_capacity=1,
    )


def index(request):

    create_filter_for_all_objects()
    template = env.get_template('TrackingApp/index.html')
    query_results = CurrentActiveMachines.objects.select_related().\
        annotate(overload_value=F('current_carrying_load') * HUNDRED_PERCENT /
                                F('brand_name__max_carrying_capacity') - HUNDRED_PERCENT).order_by('machine_id')
    brand_form = BrandForm()
    if request.method == 'POST':
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            brand_name = brand_form.cleaned_data['brand_name']
            if brand_name.brand_id:
                query_results = query_results.filter(brand_name=brand_name)
    context = {
        'query_results': query_results,
        'brand_form': brand_form,
    }
    return HttpResponse(template.render(context))


def insert_new_machine(request):

    if request.method == 'POST':
        new_machine_form = NewMachineForm(request.POST)
        if new_machine_form.is_valid():
            machine_id = new_machine_form.cleaned_data['machine_id']
            brand_name = new_machine_form.cleaned_data['brand_name']
            current_carrying_load = new_machine_form.cleaned_data['current_carrying_load']
            query = CurrentActiveMachines.objects.create(
                machine_id=machine_id,
                brand_name=brand_name,
                current_carrying_load=current_carrying_load, )
            query.save()
            return HttpResponseRedirect('/')
    else:
        new_machine_form = NewMachineForm()
    return render(request, 'TrackingApp/add_new_machine.html', {'new_machine_form': new_machine_form, })


def insert_new_brand(request):

    if request.method == 'POST':
        new_brand_form = NewBrandForm(request.POST)
        if new_brand_form.is_valid():
            brand_name = new_brand_form.cleaned_data['brand_name']
            max_carrying_capacity = new_brand_form.cleaned_data['max_carrying_capacity']
            query = BrandCharacteristics.objects.create(
                brand_name=brand_name,
                max_carrying_capacity=max_carrying_capacity, )
            query.save()
            return HttpResponseRedirect('/')
    else:
        new_brand_form = NewBrandForm()
    return render(request, 'TrackingApp/add_new_brand.html', {'new_brand_form': new_brand_form,})


