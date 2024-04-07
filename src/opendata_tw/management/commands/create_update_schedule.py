from django.core.management.base import BaseCommand
from opendata_tw import utils


class Command(BaseCommand):
    help = 'Update musical activities and shows from opendata TW'

    def add_arguments(
        self,
        parser,
    ):
        parser.add_argument(
            "cron_expression",
        )

    def handle(
        self,
        *args,
        **options,
    ):
        self.create_update_schedule(
            self,
            *args,
            **options,
        )
        return

    def create_update_schedule(
        self,
        *args,
        **options,
    ):
        utils.create_update_schedule(
            options['cron_expression'],
        )
        return
