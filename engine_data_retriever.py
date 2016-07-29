#!/usr/bin/python
# Filename: engine_data_retriever.py
# 2016.07.26

import const
import engine_const
import urllib2

class DataRetriever:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def retrieve_data(self, source, items):
        # Build HTTP request string
        requestURL = ''
        result = ''
        if source == const.SOURCE_XL:
            requestURL = self.__build_URL_XL(items)
        elif source == const.SOURCE_TX:
            requestURL = self.__build_URL_TX(items)
        elif source == const.SOURCE_WY:
            requestURL = self.__build_URL_WY(items)
        else:
            pass
        
        # Send HTTP request
        try:
            response = urllib2.urlopen(requestURL)
            result = response.read()
        except urllib2.HTTPError, e:
            # Log error
            print e.code
        except urllib2.URLError, e:
            # Log error
            print e.reason
        except Exception, e:
            print e
        finally:
            pass
        
        return result
    
    def __build_URL_XL(self, items):
        result = const.XL_URL
        for item in items:
            if item[0] == const.SH_STOCK_PREFIX \
                or item[0] == const.SH_ETF_PREFIX \
                or item == const.SHZS:
                result += const.XL_LONG_PREFIX_SH + item + const.XL_ITEM_SEPARATOR
            else:
                result += const.XL_LONG_PREFIX_SZ + item + const.XL_ITEM_SEPARATOR
        return result.strip(const.XL_ITEM_SEPARATOR)
    
    def __build_URL_TX(self, items):
        result = const.TX_URL
        for item in items:
            if item[0] == const.SH_STOCK_PREFIX \
                or item[0] == const.SH_ETF_PREFIX \
                or item == const.SHZS:
                result += const.TX_LONG_PREFIX_SH + item + const.TX_ITEM_SEPARATOR
            else:
                result += const.TX_LONG_PREFIX_SZ + item + const.TX_ITEM_SEPARATOR
        return result.strip(const.TX_ITEM_SEPARATOR)
    
    def __build_URL_WY(self, items):
        result = const.WY_URL
        for item in items:
            if item[0] == const.SH_STOCK_PREFIX \
                or item[0] == const.SH_ETF_PREFIX \
                or item == const.SHZS:
                result += const.WY_LONG_PREFIX_SH + item + const.WY_ITEM_SEPARATOR
            else:
                result += const.WY_LONG_PREFIX_SZ + item + const.WY_ITEM_SEPARATOR
        return result.strip(const.WY_ITEM_SEPARATOR)
    
