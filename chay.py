from datetime import datetime
import pandas as pd
import csv

DATADIR = ""
DATAFILE = "shmya_final_version.csv"
# pattern = '%Y-%m-%d %H:%M:%S'
min_cutlery = 2
# min_order_price = 800
# min_date = datetime.strptime('2022-01-09 00:00:00', pattern)
result = []
result_2 = []


def parsing_1(DATAFILE):
    price_dict = pd.read_csv(DATAFILE, delimiter=',')
    sorted_list = price_dict.sort_values(by='cutlery', ascending=True)
    filtered_cutlery = sorted_list[sorted_list['cutlery'] > min_cutlery]
    my_list = filtered_cutlery.values.tolist()
    for i in my_list:
        result.append(i[-4])
    a=sum(result)/len(result)
    print(a)
    # print(*result, sep='\n')
    # print(len(result))


def parsing_2(DATAFILE):
    price_dict = pd.read_csv(DATAFILE, delimiter=',')
    sorted_list = price_dict.sort_values(by='cutlery', ascending=True)
    filtered_cutlery = sorted_list[sorted_list['cutlery'] <= min_cutlery]
    my_list = filtered_cutlery.values.tolist()
    for i in my_list:
        result_2.append(i[-4])
    b = sum(result_2) / len(result_2)
    print(b)
    # print(*result_2, sep='\n')
    # print(len(result_2))


parsing_1(DATAFILE)
parsing_2(DATAFILE)
