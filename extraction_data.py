# -*- coding:utf-8 -*-


class ExtractionData:
    def extraction_data(self, weather_json):
        '从原始Json中抽取有用信息'
        if(weather_json == None):
            return None
        else:
            results_dict = weather_json['results']
            location_dict = results_dict[0]['location']
            daily_dict = results_dict[0]['daily']
            return location_dict, daily_dict
