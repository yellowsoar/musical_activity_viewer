import json

import requests


def request_data():
    data_raw = requests.get(
        "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1",
    )
    data_json = json.loads(data_raw.text)
    return data_json


api_remap_table = {
    'UID': 'id',
    'comment': 'additional_remark',
    'category': 'category_code',
    'hitRate': 'click_through_rate',
    'descriptionFilterHtml': 'description_content',
    'discountInfo': 'discount_info',
    'sourceWebName': 'flyer_source',
    'version': 'publish_version',
    'title': 'title',
    'showUnit': 'unit_perform',
    'masterUnit': 'unit_host',
    'subUnit': 'unit_assist',
    'supportUnit': 'unit_sponsor',
    'otherUnit': 'unit_other',
    'imageUrl': 'url_image',
    'webSales': 'url_ticket',
    'sourceWebPromote': 'url_flyer',
    'editModifyDate': 'time_modified',
    'startDate': 'time_start',
    'endDate': 'time_end',
}
