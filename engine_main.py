#!/usr/bin/python
# Filename: engine_main.py
# 2016.07.26

import sys
import time
import const
import engine_const
import engine_data_retriever
import engine_data_parser
import engine_data_formatter

mode = const.MODE_DEFAULT
source = const.SOURCE_DEFAULT
modes = [const.MODE_TINY, const.MODE_SIMPLE, const.MODE_FULL]
sources = [const.SOURCE_XL, const.SOURCE_TX, const.SOURCE_WY]

if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 2:
    if sys.argv[1] in modes:
        mode = sys.argv[1]
    else:
        print const.USAGE
        exit()
elif len(sys.argv) == 3:
    if sys.argv[1] in modes:
        mode = sys.argv[1]
        if sys.argv[2] in sources:
            source = sys.argv[2]
        else:
            print const.USAGE
            exit()
    else:
        print const.USAGE
        exit()
else:
    print const.USAGE
    exit()

def build_items():
    items = []
    if mode == const.MODE_TINY:
        items = const.TINY_LIST.split(' ')
    elif mode == const.MODE_SIMPLE or mode == const.MODE_FULL:
        list_str = const.INDEX_LIST + ' ' + const.STOCK_LIST
        items = list_str.strip().split(' ')
    return items
        
def check_datetime():
    localtime = time.localtime(time.time())
    if localtime.tm_wday == 5 or localtime.tm_wday == 6:
        return False
    elif localtime.tm_hour < 9 or localtime.tm_hour > 15:
        return False
    elif localtime.tm_hour == 9 and localtime.tm_min < 10:
        return False
    elif localtime.tm_hour == 15 and localtime.tm_min > 5:
        return False
    elif localtime.tm_hour == 11 and localtime.tm_min > 35:
        return False
    elif localtime.tm_hour == 12 and localtime.tm_min < 55:
        return False
    else:
        return True

def output_data():
    dr = engine_data_retriever.DataRetriever()
    dp = engine_data_parser.DataParser()
    df = engine_data_formatter.DataFormatter()
    items = build_items()
    data = dr.retrieve_data(source, items)
    values = dp.parse_data(source, data, items)
    result = df.format_data(values, mode)

    # sys.stdout.write('\r' + result)
    sys.stdout.write(result + "\r\n")

output_data()
running = True
while running:
    running = check_datetime()
    if running == True:
        output_data()
        time.sleep(const.INTERVAL)
    else:
        time.sleep(60)
