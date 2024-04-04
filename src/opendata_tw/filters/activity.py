import django_filters
from django import forms as dj_forms
from django.db import models as django_models
from django_filters import rest_framework as drf_filters

from opendata_tw import models

activity_fields = {
    'additional_remark': ['icontains'],
    'category_code__category_name': ['icontains'],
    'click_through_rate': ['gt', 'lt'],
    'description_content': ['icontains'],
    'discount_info': ['icontains'],
    'flyer_source': ['icontains'],
    'id': ['icontains'],
    'publish_version': ['icontains'],
    'time_created': ['gt', 'lt'],
    'time_end': ['gt', 'lt'],
    'time_modified': ['gt', 'lt'],
    'time_start': ['gt', 'lt'],
    'title': ['icontains'],
    'unit_assist__unit_name': ['icontains'],
    'unit_host__unit_name': ['icontains'],
    'unit_other__unit_name': ['icontains'],
    'unit_perform__unit_name': ['icontains'],
    'unit_sponsor__unit_name': ['icontains'],
    'url_flyer': ['icontains'],
    'url_image': ['icontains'],
    'url_ticket': ['icontains'],
}

activity_filter_overrides = {
    django_models.DateTimeField: {
        'filter_class': django_filters.DateTimeFilter,
        'extra': lambda f: {
            'widget': dj_forms.DateTimeInput,
        },
    },
}


class MusicalActivityFilter(django_filters.FilterSet):

    class Meta:
        fields = activity_fields
        filter_overrides = activity_filter_overrides
        model = models.MusicalActivity


class MusicalActivityDRFFilter(drf_filters.FilterSet):

    class Meta:
        fields = activity_fields
        filter_overrides = activity_filter_overrides
        model = models.MusicalActivity
