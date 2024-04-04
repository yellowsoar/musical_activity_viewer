import json
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
