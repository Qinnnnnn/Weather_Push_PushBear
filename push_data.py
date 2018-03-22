# -*- coding:utf-8 -*-
import requests


class PushData:
    def push_data(self, location_dict, daily_dict):
        '向微信Server酱推送天气消息'
        self.url = 'https://pushbear.ftqq.com/sub'
        self.payload = {'sendkey': '',
                        'text': '', 'desp': ''}
        # 消息推送Key
        self.sendkey = '2922-16acefd6fbdcc9f8915ec9dc81985d33'
        self.payload['sendkey'] = self.sendkey
        # 推送消息Title
        self.title = '%s市 天气预报' % location_dict['name']
        self.payload['text'] = self.title
        # 推送消息Description
        self.description = '# 今日天气\n* 日间(%s):%s℃\n* 夜间(%s):%s℃\n\n# 明日天气\n* 日间(%s):%s℃\n* 夜间(%s):%s℃' % (
            daily_dict[0]['text_day'], daily_dict[0]['high'], daily_dict[0]['text_night'], daily_dict[0]['low'], daily_dict[1]['text_day'], daily_dict[1]['high'], daily_dict[1]['text_night'], daily_dict[1]['low'])
        self.payload['desp'] = self.description
        requests.get(self.url, params=self.payload)
