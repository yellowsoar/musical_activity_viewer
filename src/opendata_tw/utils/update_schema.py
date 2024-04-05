import copy
import json
import logging
import re
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

import requests
from benedict import benedict
from opendata_tw import serializers

logger_django_crud = logging.getLogger('django_crud')


def request_schema(
    request_url: str = "",
) -> Dict:
    """Request schema via requests package

    Parameters
    ----------
    request_url : str, optional
        The URL to the schema
    """
    data_raw = requests.get(
        (
            "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJOpenApi&category=1"
            if not request_url
            else request_url
        ),
    )
    data_json = json.loads(data_raw.text)
    return data_json


def gen_category_table(
    data_json: Dict,
) -> Dict:
    """Generate category table from dictionary

    Parameters
    ----------
    data_json : Dict
        The dictionary of all categories
    """
    data_schema = benedict(
        data_json,
        keypath_separator="..",
    )
    try:
        category_text = str(
            data_schema[
                "..".join(
                    [
                        'components',
                        'schemas',
                        'Activity',
                        'properties',
                        'category',
                        'description',
                    ],
                )
            ],
        )
    except:
        category_text = ""

    if category_text:
        category_text = re.sub(
            r'活動類別 ([0-9]:.*)',
            r'\1',
            category_text,
        )

    if category_text:
        category_array = category_text.split(' ')

    category_table = {}
    for single_category in category_array:
        key_value = single_category.split(':')
        category_table[key_value[0]] = key_value[1]
    return category_table


def update_schema():
    log_extra_crud = {}
    log_extra_crud['skipped_categories'] = []
    log_extra_crud['created_categories'] = []
    log_extra_crud['unknown_categories'] = []
    data_json = request_schema()
    category_table = gen_category_table(data_json)

    if not category_table:
        return

    category_data = {}
    for (
        category_id,
        category_name,
    ) in category_table.items():
        category_data['id'] = category_id
        category_data['category_name'] = category_name
        the_serializer = serializers.ActivityCategorySerializer(
            data=category_data,
        )

        if not the_serializer.is_valid():
            log_extra_crud['skipped_categories'].append(
                copy.deepcopy(
                    category_data,
                ),
            )
            continue

        try:
            the_serializer.save()
            log_extra_crud['created_categories'].append(
                copy.deepcopy(
                    the_serializer.validated_data,
                ),
            )
        except:
            log_extra_crud['unknown_categories'].append(
                copy.deepcopy(
                    the_serializer.validated_data,
                ),
            )

    logger_django_crud.log(
        11,
        "\n".join(
            [
                'Musical activity category schema updated.',
            ],
        ),
        extra=log_extra_crud,
    )
