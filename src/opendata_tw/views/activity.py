from django.shortcuts import (
    redirect,
    render,
)
from django_filters import rest_framework as drf_filters
from opendata_tw import (
    filters,
    models,
)


def activity_operation(request):
    filter_obj = filters.MusicalActivityFilter(
        request.GET,
        queryset=models.MusicalActivity.objects.all().order_by(
            '-time_created',
        ),
    )

    return render(
        request,
        'operation.html',
        {
            'filter': filter_obj,
        },
    )
