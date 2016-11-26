# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader

from .forms import BrandForm
from .models import CurrentActiveMachines

def index(request):

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data['brand_name']
            if brand_name.brand_id == 0:
                query_results = CurrentActiveMachines.objects.all()
            else:
                query_results = CurrentActiveMachines.objects.filter(brand_name=brand_name)
    else:
        form = BrandForm()
        query_results = CurrentActiveMachines.objects.all()
    template = loader.get_template('TrackingApp/index.html')
    context = RequestContext(request, {
        'query_results': query_results,
        'form': form,
    })
    return HttpResponse(template.render(context))