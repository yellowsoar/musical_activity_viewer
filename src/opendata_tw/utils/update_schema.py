import json
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
