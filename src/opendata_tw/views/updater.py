from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django_q.tasks import async_task
from opendata_tw import utils


@login_required()
def update_schema(
    request,
):
    async_task(
        utils.update_schema(),
    )
    return redirect(
        'operate_activity',
    )
