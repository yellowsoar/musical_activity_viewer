from django.core.management.base import BaseCommand
from opendata_tw import utils


class Command(BaseCommand):
    help = 'Update musical activities and shows from opendata TW'

    def handle(
        self,
        *args,
        **options,
    ):
        self.update_data(
            self,
            *args,
            **options,
        )
        return

    def update_data(
        self,
        *args,
        **options,
    ):
        utils.retrieve_data()
        return
