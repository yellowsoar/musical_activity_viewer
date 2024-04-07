from django_q.tasks import schedule


def create_update_schedule(
    cron_expression,
):
    schedule(
        'django.core.management.call_command',
        'update_data',
        schedule_type='C',
        cron=str(cron_expression),
    ),

    pass
