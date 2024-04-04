import json

import requests
from opendata_tw import serializers


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


def retrieve_data():
    data_json = request_data()
    for single_activity in data_json:
        remapped_activity = {}
        for (
            activity_key,
            activity_value,
        ) in single_activity.items():
            if activity_key in api_remap_table:
                remapped_activity.update(
                    {
                        api_remap_table.get(
                            activity_key,
                        ): activity_value,
                    },
                )

        theserializer = serializers.MusicalActivitySerializer(
            data=remapped_activity,
        )
        if not theserializer.is_valid():
            print(
                "\n".join(
                    [
                        "Activity exist:",
                        f"{remapped_activity['id']}",
                        "(Activity creation skipped)",
                    ],
                ),
            )
            continue

        try:
            theserializer.save()
            print(
                "\n".join(
                    [
                        "Activity created:",
                        f"{theserializer.validated_data}",
                    ],
                ),
            )
        except:
            print(
                "\n".join(
                    [
                        "Something wrong here while handling:",
                        f"{theserializer.validated_data}",
                    ],
                ),
            )
    pass
