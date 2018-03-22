# -*- coding:utf-8 -*-
from get_data import GetData
from extraction_data import ExtractionData
from push_data import PushData


class Main:
    def __init__(self):
        '初始化程序各模块'
        self.get_data = GetData()
        self.extraction_data = ExtractionData()
        self.push_data = PushData()

    def push(self):
        weather_json = self.get_data.get_data()
        location_dict, daily_dict = self.extraction_data.extraction_data(
            weather_json)
        self.push_data.push_data(location_dict, daily_dict)


if __name__ == '__main__':
    main = Main()
    #while True:
    main.push()
