from datetime import datetime
import pandas as pd

DATADIR = ""
DATAFILE = "shmya_final_version.csv"
pattern = '%Y-%m-%d %H:%M:%S'
min_cutlery = 2
min_order_price = 800
min_date = datetime.strptime('2022-01-09 00:00:00', pattern)
result = []
segment = []

def parse_csv(DATAFILE):
    price_dict = pd.read_csv(DATAFILE, delimiter=',')
    sorted_list = price_dict.sort_values(by='order_price', ascending=True)
    filtered_cutlery = sorted_list[sorted_list['cutlery'] > min_cutlery]
    filtered_order_price = filtered_cutlery[filtered_cutlery['order_price'] > min_order_price]
    my_list = filtered_order_price.values.tolist()
    for string in my_list:
        if min_date <= datetime.strptime(string[0], pattern):
            string[0] = string[0].replace('-', '.')
            result.append(string)
    # print(*sorted(result),sep='\n')
    for i in range(len(result)):
        segment.append(result[i][-2])
    print(*segment, sep = '\n')
parse_csv(DATAFILE)