import copy
import json
import logging

import pendulum
import requests
from django_q.tasks import async_task
from musical_activity_viewer import settings
from opendata_tw import (
    config,
    serializers,
    utils,
)

logger_django_crud = logging.getLogger('django_crud')

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
    log_extra_crud = {}
    log_extra_crud['skipped_activities'] = []
    log_extra_crud['created_activities'] = []
    log_extra_crud['unknown_activities'] = []
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
        if 'time_start' in remapped_activity:
            remapped_activity['time_start'] = str(
                pendulum.parse(
                    remapped_activity['time_start'],
                )
                .in_timezone(
                    settings.TIME_ZONE,
                )
                .format('YYYY-MM-DD'),
            )

        if 'time_end' in remapped_activity:
            remapped_activity['time_end'] = str(
                pendulum.parse(
                    remapped_activity['time_end'],
                )
                .in_timezone(
                    settings.TIME_ZONE,
                )
                .format('YYYY-MM-DD'),
            )

        theserializer = serializers.MusicalActivitySerializer(
            data=remapped_activity,
        )
        if not theserializer.is_valid():
            log_extra_crud['skipped_activities'].append(
                copy.deepcopy(
                    remapped_activity['id'],
                ),
            )
            continue

        try:
            theserializer.save()
            log_extra_crud['created_activities'].append(
                copy.deepcopy(
                    str(theserializer.validated_data['id']),
                ),
            )
        except:
            log_extra_crud['unknown_activities'].append(
                copy.deepcopy(
                    str(theserializer.validated_data),
                ),
            )

        manytomany_fields = {}
        for item in config.field_model_mapping.keys():
            manytomany_fields[item] = copy.deepcopy(
                str(
                    theserializer.initial_data.pop(item),
                ).split(
                    '、',
                ),
            )
        async_task(
            utils.save_unit(
                copy.deepcopy(
                    theserializer.instance,
                ),
                manytomany_fields,
            ),
        )

    logger_django_crud.log(
        11,
        "\n".join(
            [
                'Musical activity data updated.',
            ],
        ),
        extra=log_extra_crud,
    )
