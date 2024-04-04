from opendata_tw import utils


class TestOpendata_twUtils:

    def test_gen_category_table(self):

        test_obj = {
            'openapi': '3.0.1',
            'info': {
                'title': '音樂表演資訊',
                'description': '音樂劇場表演訊息JSON格式',
                'termsOfService': 'https://opendata.culture.tw/cms/1958862',
                'contact': {'email': 'jch12@moc.gov.tw'},
                'license': {
                    'name': '政府資料開放授權條款-第1版',
                    'url': 'https://data.gov.tw/license',
                },
                'version': '1.4',
            },
            'servers': [
                {
                    'url': 'https://cloud.culture.tw',
                    'description': '文化部活動網站',
                },
            ],
            'paths': {
                '/frontsite/trans/SearchShowAction.do': {
                    'get': {
                        'operationId': 'activityGet',
                        'parameters': [
                            {
                                'name': 'method',
                                'in': 'query',
                                'required': True,
                                'schema': {
                                    'type': 'string',
                                    'default': 'doFindTypeJ',
                                    'enum': ['doFindTypeJ'],
                                },
                            },
                            {
                                'name': 'category',
                                'in': 'query',
                                'required': True,
                                'schema': {
                                    'type': 'string',
                                    'default': '1',
                                    'enum': ['1'],
                                },
                            },
                        ],
                        'responses': {
                            '200': {
                                'description': '成功',
                                'content': {
                                    'application/json': {
                                        'schema': {
                                            'type': 'array',
                                            'items': {
                                                '$ref': '#/components/schemas/Activity',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'servers': [
                            {
                                'url': 'https://cloud.culture.tw',
                                'description': '文化部活動網站',
                            },
                        ],
                    },
                },
            },
            'components': {
                'schemas': {
                    'ShowInfo': {
                        'type': 'object',
                        'properties': {
                            'time': {
                                'type': 'string',
                                'description': '單場次演出時間',
                            },
                            'location': {
                                'type': 'string',
                                'description': '地址',
                            },
                            'locationName': {
                                'type': 'string',
                                'description': '場地名稱',
                            },
                            'onSales': {
                                'type': 'string',
                                'description': '是否售票',
                                'enum': ['Y', 'N'],
                            },
                            'price': {
                                'type': 'string',
                                'description': '售票說明',
                            },
                            'latitude': {
                                'type': 'string',
                                'description': '緯度',
                            },
                            'longitude': {
                                'type': 'string',
                                'description': '經度',
                            },
                            'endTime': {
                                'type': 'string',
                                'description': '結束時間',
                            },
                        },
                    },
                    'Activity': {
                        'type': 'object',
                        'properties': {
                            'version': {
                                'type': 'string',
                                'description': '發行版本',
                            },
                            'UID': {
                                'type': 'string',
                                'description': '唯一辨識碼',
                            },
                            'title': {
                                'type': 'string',
                                'description': '活動名稱',
                            },
                            'category': {
                                'type': 'string',
                                'description': '活動類別 1:音樂 2:戲劇 3:舞蹈 4:親子 5:獨立音樂 6:展覽 7:講座 8:電影 11:綜藝 13:競賽 14:徵選 15:其他 17:演唱會 19:研習課程 200:閱讀',
                            },
                            'showInfo': {
                                'type': 'array',
                                'description': '活動場次資訊',
                                'items': {
                                    '$ref': '#/components/schemas/ShowInfo',
                                },
                            },
                            'showUnit': {
                                'type': 'string',
                                'description': '演出單位',
                            },
                            'discountInfo': {
                                'type': 'string',
                                'description': '折扣資訊',
                            },
                            'descriptionFilterHtml': {
                                'type': 'string',
                                'description': '簡介說明',
                            },
                            'imageUrl': {
                                'type': 'string',
                                'description': '圖片連結',
                            },
                            'masterUnit': {
                                'type': 'array',
                                'description': '主辦單位',
                                'items': {'type': 'string'},
                            },
                            'subUnit': {
                                'type': 'array',
                                'description': '協辦單位',
                                'items': {'type': 'string'},
                            },
                            'supportUnit': {
                                'type': 'array',
                                'description': '贊助單位',
                                'items': {'type': 'string'},
                            },
                            'otherUnit': {
                                'type': 'array',
                                'description': '其他單位',
                                'items': {'type': 'string'},
                            },
                            'webSales': {
                                'type': 'string',
                                'description': '售票網址',
                            },
                            'sourceWebPromote': {
                                'type': 'string',
                                'description': '推廣網址',
                            },
                            'comment': {
                                'type': 'string',
                                'description': '備註',
                            },
                            'editModifyDate': {
                                'type': 'string',
                                'description': '編輯時間',
                            },
                            'sourceWebName': {
                                'type': 'string',
                                'description': '來源網站名稱',
                            },
                            'startDate': {
                                'type': 'string',
                                'description': '活動起始日期',
                            },
                            'endDate': {
                                'type': 'string',
                                'description': '活動結束日期',
                            },
                            'hitRate': {
                                'type': 'integer',
                                'description': '點閱數',
                                'format': 'Int32',
                            },
                        },
                    },
                },
            },
        }
        result_obj = {
            '1': '音樂',
            '2': '戲劇',
            '3': '舞蹈',
            '4': '親子',
            '5': '獨立音樂',
            '6': '展覽',
            '7': '講座',
            '8': '電影',
            '11': '綜藝',
            '13': '競賽',
            '14': '徵選',
            '15': '其他',
            '17': '演唱會',
            '19': '研習課程',
            '200': '閱讀',
        }
        the_result = bool(result_obj == utils.gen_category_table(test_obj))
        error_message = "Something wrong while generating the category table"
        assert the_result, error_message
