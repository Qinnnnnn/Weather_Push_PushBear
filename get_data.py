# -*- coding:utf-8 -*-
import requests


class GetData:
    def get_data(self):
        '获取天气原始信息'
        # 获取指定城市未来最多15天每天的白天和夜间预报，以及昨日的历史天气。
        url = "https://api.seniverse.com/v3/weather/daily.json"
        payload = {'key': 'ypenvkqbbguidaik', 'location': '',
                   'language': 'zh-Hans', 'unit': 'c', 'start': '0', 'days': ''}
        # 地区参数
        location = "chengdu"
        payload['location'] = location
        #天气预报天数参数
        days = '2'
        payload['days'] = days
        response = requests.get(url, params=payload)
        weather_dict = response.json()
        return weather_dict
