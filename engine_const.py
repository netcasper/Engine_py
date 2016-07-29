#!/usr/bin/python
# Filename: engine_const.py
# 2016.07.26

import const

const.MODE_DEFAULT = '0' # TINY MODE
const.MODE_TINY = '0'
const.MODE_SIMPLE = '1'
const.MODE_FULL = '2'

const.SOURCE_DEFAULT = '0' # XL
const.SOURCE_XL = '0'
const.SOURCE_TX = '1'
const.SOURCE_WY = '2'

const.USAGE = r'Usage: >python engine_main [0|1|2] [0|1|2] #[tiny|simple|full] [XL|TX|WY]'

const.XL_URL = r'http://hq.sinajs.cn/list='
const.TX_URL = r'http://qt.gtimg.cn/q='
const.WY_URL = r'http://api.money.126.net/data/feed/'
const.XL_SHORT_PREFIX_SH = 's_sh'
const.XL_SHORT_PREFIX_SZ = 's_sz'
const.XL_LONG_PREFIX_SH = 'sh'
const.XL_LONG_PREFIX_SZ = 'sz'
const.TX_SHORT_PREFIX_SH = 's_sh'
const.TX_SHORT_PREFIX_SZ = 's_sz'
const.TX_LONG_PREFIX_SH = 'sh'
const.TX_LONG_PREFIX_SZ = 'sz'
const.WY_SHORT_PREFIX_SH = '0'
const.WY_SHORT_PREFIX_SZ = '1'
const.WY_LONG_PREFIX_SH = '0'
const.WY_LONG_PREFIX_SZ = '1'
const.XL_ITEM_SEPARATOR = ','
const.TX_ITEM_SEPARATOR = ','
const.WY_ITEM_SEPARATOR = ','

const.SHZS = '000001'
const.SZZS = '399001'
const.CYBZ = '399006'
const.SH_STOCK_PREFIX = '6'
const.SH_ETF_PREFIX = '5'

const.TINY_LIST = '159915 000001 510050'
const.STOCK_LIST = '159915 510050 600026'
const.INDEX_LIST = '000001 399001 399006'

const.ITEM_SEPARATOR = ' | '
const.FIELD_SEPARATOR = '/'
const.SIMPLE_SEPARATOR = '\t'
const.FULL_SEPARATOR = '\t\t'

const.SELL_SEPARATOR = '   '
const.BUY_SEPARATOR = ' ^ '
const.INDEX_STOCK_SEPARATOR = '-------------------------------------------------------------\r\n'

const.INTERVAL = 1.0 # float: 1.0 Second



