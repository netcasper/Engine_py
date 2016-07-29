#!/usr/bin/python
# Filename: engine_data_formatter.py
# 2016.07.26

import time
import const
import engine_const
import engine_data_item

class DataFormatter:
    def __init__(self):
        pass

    def __del__(self):
        pass
    
    def format_data(self, items, mode):
        if mode == const.MODE_TINY:
            return self.__format_data_tiny(items)
        elif mode == const.MODE_SIMPLE:
            return self.__format_data_simple(items)
        elif mode == const.MODE_FULL:
            return self.__format_data_full(items)
        else:
            return

    def __format_data_tiny(self, items):
        # local time, market time, item list(price, ratio)
        result = ''
        market_time = ''
        for item in items:
            market_time =  item.time
            data_item = engine_data_item.DataItem()
            data_item = item
            data_item.price = self.__format_price(data_item.price)
            result += data_item.price + const.FIELD_SEPARATOR \
                + data_item.ratio + const.ITEM_SEPARATOR
            
        local_time = time.strftime("%H:%M:%S", time.localtime())
        result = local_time + ' ' + market_time + const.ITEM_SEPARATOR + result
        return result.strip().strip(const.ITEM_SEPARATOR)
    
    def __format_data_simple(self, items):
        # local date, local time, market time
        # index list
            # code, name, price, ratio, high, low, amount
        # stock list
            # code, name, price, ratio, high, low, amount
        result = ''
        market_time = ''
        for item in items:
            market_time =  item.time
            data_item = engine_data_item.DataItem()
            data_item = item
            data_item.price = self.__format_price(data_item.price)
            data_item.high = self.__format_price(data_item.high)
            data_item.low = self.__format_price(data_item.low)
            result += data_item.code + const.SIMPLE_SEPARATOR \
                + self.__format_name(data_item.name) + const.SIMPLE_SEPARATOR \
                + data_item.ratio + '%' + const.SIMPLE_SEPARATOR \
                + data_item.price + const.SIMPLE_SEPARATOR \
                + data_item.high + const.SIMPLE_SEPARATOR \
                + data_item.low + const.SIMPLE_SEPARATOR \
                + data_item.amount + '\r\n'
            
        local_date = time.strftime("%Y-%m-%d", time.localtime())
        local_time = time.strftime("%H:%M:%S", time.localtime())
        result = local_date + const.SIMPLE_SEPARATOR \
            + local_time + const.SIMPLE_SEPARATOR \
            + market_time + '\r\n' + result
        return result.strip().strip(const.ITEM_SEPARATOR)
    
    def __format_data_full(self, items):
        # local date, local time, market time
        # index list
            # code, name, price, ratio, high, low, amount
        # stock list
            # code, price, ratio
            # high, low, amount
            # sell 5
            # buy 5
        result = ''
        market_time = '00:00:00'
        for item in items:
            if item.time > market_time:
                market_time = item.time
            data_item = engine_data_item.DataItem()
            data_item = item
            data_item.price = self.__format_price(data_item.price)
            data_item.high = self.__format_price(data_item.high)
            data_item.low = self.__format_price(data_item.low)
            result += data_item.code + const.SIMPLE_SEPARATOR \
                + self.__format_name(data_item.name) + const.SIMPLE_SEPARATOR \
                + data_item.ratio + '%' + const.SIMPLE_SEPARATOR \
                + data_item.price + const.SIMPLE_SEPARATOR \
                + data_item.high + const.SIMPLE_SEPARATOR \
                + data_item.low + const.SIMPLE_SEPARATOR \
                + data_item.amount + '\r\n'
            
        local_date = time.strftime("%Y-%m-%d", time.localtime())
        local_time = time.strftime("%H:%M:%S", time.localtime())
        result = local_date + const.SIMPLE_SEPARATOR \
            + local_time + const.SIMPLE_SEPARATOR \
            + market_time + '\r\n' + result
        result = result.strip().strip(const.ITEM_SEPARATOR) + '\r\n'
        result = result + const.INDEX_STOCK_SEPARATOR
        
        # when items len < index_len+1, only output index info, no stock items
        index_len = len(const.INDEX_LIST.strip().split(' '))
        if len(items) < index_len+1:
            return result
        
        # sell 5 and buy5
        price_volume = [[0 for i in range(len(items)-index_len)] for i in range(10)]
        i = 0
        for item in items:
            if item.code == const.SHZS or item.code == const.SZZS \
                or item.code == const.CYBZ:
                continue
            price_volume[0][i] = item.sp5 + const.SELL_SEPARATOR + item.sv5
            price_volume[1][i] = item.sp4 + const.SELL_SEPARATOR + item.sv4
            price_volume[2][i] = item.sp3 + const.SELL_SEPARATOR + item.sv3
            price_volume[3][i] = item.sp2 + const.SELL_SEPARATOR + item.sv2
            price_volume[4][i] = item.sp1 + const.SELL_SEPARATOR + item.sv1
            price_volume[5][i] = item.bp1 + const.BUY_SEPARATOR + item.bv1
            price_volume[6][i] = item.bp2 + const.BUY_SEPARATOR + item.bv2
            price_volume[7][i] = item.bp3 + const.BUY_SEPARATOR + item.bv3
            price_volume[8][i] = item.bp4 + const.BUY_SEPARATOR + item.bv4
            price_volume[9][i] = item.bp5 + const.BUY_SEPARATOR + item.bv5
            i = i + 1;
        
        # Fill to the result
        pv = ''
        for i in range(10):
            for j in range(len(items)-index_len):
                pv += str(price_volume[i][j]) + const.FULL_SEPARATOR
            pv = pv.strip(const.FULL_SEPARATOR) + '\r\n'
        
        return result + pv
    
    def __format_price(self, price):
        if float(price) > 1000:
            return str(round(float(price),1))
        else:
            return price
    def __format_name(self, name):
        if len(name) < 8:
            output = name + '        '
            return str(output[0:8])
        else:
            return name
