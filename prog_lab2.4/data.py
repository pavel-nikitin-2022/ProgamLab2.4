from recover import vinz, smoothing, smoothing_average, approximation
from datetime import timedelta, datetime
import requests
import json

#получаем список нужных нам запросов
api_moex_list = open("requesr.txt", 'r')
api_moex_list = api_moex_list.readlines()

#период трейдинга
def trade_game(recover, smooth, start, end, ticker, k):
    list = start_data_factory_info(ticker, start, api_moex_list, end)
    if recover == "vinz": recover = vinz
    if recover == "linear": recover = approximation
    if smooth == "static": smooth = smoothing_average(recover(list), k)
    if smooth == "dinamyc": smooth = smoothing(recover(list), k)
    return (recover(list), smooth)

#разница между 2 датами
def differance_days(start_date, finish_date):
    return int(str(datetime(
        int(finish_date.split('-')[0]),
        int(finish_date.split('-')[1]),
        int(finish_date.split('-')[2])) - datetime(
        int(start_date.split('-')[0]),
        int(start_date.split('-')[1]),
        int(start_date.split('-')[2]))).split()[0])

#собираем данные по конкретной компании за период
def start_data_factory_info(company, start_date, requests_list, finish_date):
    number_days = differance_days(start_date, finish_date)
    res = [None] * (number_days + 1)
    last = start_date
    prev_last = False
    while last != finish_date and differance_days(last, finish_date) > 0 and prev_last != last:
        url = (requests_list[0][0:-1] + company +
           requests_list[1][0:-1] + "from=" +
           last + "&till=" + finish_date)
        prev_last = last
        data = requests.get(url)
        data = data.json()

        for j in data['history']["data"]:
            if j[-1] != None: 
                last = j[0]
                if start_date == j[0]: res[0] = j[-1]
                else: res[differance_days(start_date, j[0])] = j[-1]

    return res