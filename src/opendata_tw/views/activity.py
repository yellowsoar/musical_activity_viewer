from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import (
    redirect,
    render,
)
from django_filters import rest_framework as drf_filters
from opendata_tw import (
    filters,
    forms,
    models,
    serializers,
)
from rest_framework import generics


def activity_operation(request):
    filter_obj = filters.MusicalActivityFilter(
        request.GET,
        queryset=models.MusicalActivity.objects.all().order_by(
            '-time_created',
        ),
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
        'operation.html',
        {
            'filter': filter_obj,
            'page_obj': pagered_queryset,
        },
    )


@login_required()
def update_activity(
    request,
    pk,
):
    activity = models.MusicalActivity.objects.get(
        id=pk,
    )
    if request.method == 'POST':
        form = forms.MusicalActivityForm(
            request.POST,
            instance=activity,
        )
        if form.is_valid():
            form.save()
        return redirect('/')
    form = forms.MusicalActivityForm(
        instance=activity,
    )
    context = {
        'form': form,
    }
    return render(
        request,
        'update.html',
        context,
    )


@login_required()
def delete_activity(
    request,
    pk,
):
    activity = models.MusicalActivity.objects.get(
        id=pk,
    )
    form = forms.MusicalActivityForm(
        instance=activity,
    )
    if request.method == "POST":
        activity.delete()
        return redirect(
            'operate_activity',
        )
    context = {
        'form': form,
    }
    return render(
        request,
        'delete.html',
        context,
    )


class DRFActivityList(generics.ListAPIView):
    queryset = models.MusicalActivity.objects.all()
    serializer_class = serializers.MusicalActivitySerializer
    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_class = filters.MusicalActivityDRFFilter
    filterset_fields = '__all__'
