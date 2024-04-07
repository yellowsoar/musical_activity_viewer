import django_filters
from django_filters import rest_framework as drf_filters

from django_q import models


class DjangoQScheduleFilter(django_filters.FilterSet):

    class Meta:
        fields = '__all__'
        # filter_overrides = activity_filter_overrides
        model = models.Schedule


class DjangoQScheduleDRFFilter(drf_filters.FilterSet):

    class Meta:
        fields = '__all__'
        # filter_overrides = activity_filter_overrides
        model = models.Schedule
