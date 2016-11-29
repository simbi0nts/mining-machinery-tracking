from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_machine/$', views.insert_new_machine, name='insert_new_machine'),
    url(r'^new_brand/$', views.insert_new_brand, name='insert_new_brand'),
]
