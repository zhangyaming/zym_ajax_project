from django.conf.urls import patterns, include, url
from ajax2 import views

urlpatterns = patterns('',
	url(r'^index/',views.index,name='home'),
	url(r'^add/',views.add,name='add'),
    url(r'^ajax_list/',views.ajax_list,name='ajax_list'),
    url(r'^ajax_dict/',views.ajax_dict,name='ajax_dict'),
)