from django.contrib import admin

from .models import CurrentActiveMachines, BrandCharacteristics

# Register your models here.

admin.site.register(CurrentActiveMachines)
admin.site.register(BrandCharacteristics)