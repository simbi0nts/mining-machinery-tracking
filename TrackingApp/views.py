# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import BrandForm
from .models import CurrentActiveMachines, BrandCharacteristics
from django.db.models import F

HUNDRED_PERCENT = 100

def index(request):

    # TODO: Maybe there is more correct way to define this function in code
    # Adding select option for choosing all active machines from DB
    BrandCharacteristics.objects.get_or_create(
            brand_id=0,
            brand_name="Все",
            max_carrying_capacity=1,
        )

    query_results = CurrentActiveMachines.objects.\
        annotate(overload_value=F('current_carrying_load') * HUNDRED_PERCENT /
                                F('brand_name__max_carrying_capacity') - HUNDRED_PERCENT)
    template = loader.get_template('TrackingApp/index.html')
    form = BrandForm()
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data['brand_name']
            if brand_name.brand_id:
                query_results = query_results.filter(brand_name=brand_name)
    context = RequestContext(request, {
        'query_results': query_results,
        'form': form,
    })
    return HttpResponse(template.render(context))

