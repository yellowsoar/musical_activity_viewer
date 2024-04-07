from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django_filters import rest_framework as drf_filters
from django_q import models as djq_models
from mav_djangoq import (
    filters,
    models,
)
from rest_framework import generics

@login_required()
def django_q_schedule_list(request):
    filter_obj = filters.DjangoQScheduleFilter(
        request.GET,
        queryset=djq_models.Schedule.objects.all()
    )

    paginator = Paginator(
        filter_obj.qs,
        20,
    )
    page = request.GET.get(
        'page',
        1,
    )
    pagered_queryset = paginator.page(page)

    return render(
        request,
        'list.html',
        {
            'filter': filter_obj,
            'page_obj': pagered_queryset,
        },
    )
