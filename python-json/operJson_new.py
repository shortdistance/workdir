# -*- coding:utf-8 -*-
import json
import time
from datetime import datetime


def timestamp_to_date(timestamp_str):
    timestamp = float(timestamp_str)
    timeArray = time.localtime(timestamp)
    ret_date = time.strftime("%B %Y", timeArray)
    return ret_date


def add_or_update_result_list(food_type, date_str):
    if ret_list == 0:
        ret_list.append(dict(foodType=food_type, time=date_str, count=1))
    else:
        is_exist = False
        for record in ret_list:
            if record['foodType'] == food_type and record['time'] == date_str:
                record['count'] += 1
                is_exist = True
                break
        if is_exist == False:
            ret_list.append(dict(foodType=food_type, time=date_str, count=1))


food_type = ['pizza', 'burger', 'coffee', 'tea', 'vegan']

ret_list = []
def analysisJsonFile(file_path):
    with open(file_path) as data_file:
        data = json.load(data_file)
        for d in data:
            create_time = d['createdTime']
            dt = datetime.strptime(create_time, '%a %b %d %H:%M:%S +0000 %Y')
            dt_str = dt.strftime('%d %b %Y')
            foodType = d['foodType']
            is_type_exist = False
            for ft in food_type:
                if ft == foodType:
                    add_or_update_result_list(ft, dt_str)
                    is_type_exist = True
                    break
            if is_type_exist == False:
                pass
    print ret_list


if __name__ == '__main__':
    #each time run one sentence
    #analysisJsonFile('jsonfile/twitter_pizza.json')
    #analysisJsonFile('jsonfile/twitter_burger.json')
    #analysisJsonFile('jsonfile/twitter_coffee.json')
    #analysisJsonFile('jsonfile/twitter_tea.json')
    analysisJsonFile('jsonfile/twitter_vegan.json')