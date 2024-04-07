from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

from opendata_tw import config


def save_unit(
    activity_instance: str,
    unit_table: Dict,
):
    for (
        the_field,
        the_model,
    ) in config.field_model_mapping.items():
        if the_field not in unit_table:
            continue
        if not unit_table[the_field]:
            continue
        for single_unit in unit_table[the_field]:
            if not single_unit:
                continue
            (
                instance_unit,
                created,
            ) = the_model.objects.get_or_create(
                unit_name=unit_table[the_field],
            )
            instance_through = config.field_through_model_mapping[
                the_field
            ].objects.create(
                musical_activity=activity_instance,
                unit_id=instance_unit,
            )
