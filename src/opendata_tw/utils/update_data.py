import json

import requests


def request_data():
    data_raw = requests.get(
        "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1",
    )
    data_json = json.loads(data_raw.text)
    return data_json
