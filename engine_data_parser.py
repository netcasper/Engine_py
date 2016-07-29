#!/usr/bin/python
# Filename: engine_data_parser.py
# 2016.07.26

import json
import const
import engine_const
import engine_data_item

class DataParser:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def parse_data(self, source, input, items):
        if source == const.SOURCE_XL:
            return self.__parse_data_XL(input)
        elif source == const.SOURCE_TX:
            return self.__parse_data_TX(input)
        elif source == const.SOURCE_WY:
            return self.__parse_data_WY(input, items)
        else:
            return []

    def __parse_data_XL(self, input):
        outputs = []
        # Get each item: var hq_str_sz159915="xxx,2.147,...,";var
        items = input.strip(';').split(';')
        for item in items:
            output_item = engine_data_item.DataItem()
            # Get valuable part: "xxx,2.147,...,"
            valuable_parts = item.split('=')
            if len(valuable_parts) == 2:
                header = valuable_parts[0].strip()
                # len('var hq_str_sz159915')=19
                # len('var hq_str_s_sz159915')=21
                if len(header) == 19: 
                    output_item.code = header[-6:];
                fields = valuable_parts[1].strip(r'"').split(',')
                if len(fields) == 33:
                    output_item.name = fields[0]
                    output_item.price = fields[3]
                    output_item.ratio = self.__get_ratio(fields[2], fields[3])
                    output_item.high = fields[4]
                    output_item.low = fields[5]
                    # fields[6] buy price 1
                    # fields[7] sell price 1
                    output_item.volume = str(int(fields[8])/100)
                    output_item.amount = str(round(float(fields[9])/100000000.0, 2))
                    output_item.bv1 = str(round(float(fields[10])/10000.0, 2))
                    output_item.bp1 = fields[11]
                    output_item.bv2 = str(round(float(fields[12])/10000.0, 2))
                    output_item.bp2 = fields[13]
                    output_item.bv3 = str(round(float(fields[14])/10000.0, 2))
                    output_item.bp3 = fields[15]
                    output_item.bv4 = str(round(float(fields[16])/10000.0, 2))
                    output_item.bp4 = fields[17]
                    output_item.bv5 = str(round(float(fields[18])/10000.0, 2))
                    output_item.bp5 = fields[19]
                    output_item.sv1 = str(round(float(fields[20])/10000.0, 2))
                    output_item.sp1 = fields[21]
                    output_item.sv2 = str(round(float(fields[22])/10000.0, 2))
                    output_item.sp2 = fields[23]
                    output_item.sv3 = str(round(float(fields[24])/10000.0, 2))
                    output_item.sp3 = fields[25]
                    output_item.sv4 = str(round(float(fields[26])/10000.0, 2))
                    output_item.sp4 = fields[27]
                    output_item.sv5 = str(round(float(fields[28])/10000.0, 2))
                    output_item.sp5 = fields[29]
                    output_item.date = fields[30]
                    output_item.time = fields[31]
                    # field[32] unknown
                    outputs.append(output_item)
            else:
                # Failed to parse the data
                pass
        return outputs

    def __parse_data_TX(self, input):
        outputs = []
        # Get each item: v_sz159915="51~cyb~159915~2.146~;v_sz159915 
        items = input.strip(';').split(';')
        for item in items:
            output_item = engine_data_item.DataItem()
            # Get valuable part: "xxx,2.147,...,"
            valuable_parts = item.split('=')
            if len(valuable_parts) == 2:
                header = valuable_parts[0].strip()
                # len('v_sz159915')=10
                # len('v_s_sz159915')=12
                fields = valuable_parts[1].strip(r'"').split('~')
                if len(fields) == 50:
                    # field[0] unknown
                    output_item.name = fields[1]
                    output_item.code = fields[2]
                    output_item.price = fields[3]
                    # field[4] last price
                    # output_item.ratio = self.__get_ratio(fields[4], fields[3])
                    # fields[5] today's begin price
                    # fields[6] volume (shou)
                    output_item.volume = fields[6]
                    # fields[7] waipan
                    # fields[8] neipan
                    
                    output_item.amount = str(round(float(fields[9])/100000000.0, 2))
                    output_item.bp1 = fields[9]
                    output_item.bv1 = str(float(fields[10])/100.0)
                    output_item.bp2 = fields[11]
                    output_item.bv2 = str(float(fields[12])/100.0)
                    output_item.bp3 = fields[13]
                    output_item.bv3 = str(float(fields[14])/100.0)
                    output_item.bp4 = fields[15]
                    output_item.bv4 = str(float(fields[16])/100.0)
                    output_item.bp5 = fields[17]
                    output_item.bv5 = str(float(fields[18])/100.0)
                    output_item.sp1 = fields[19]
                    output_item.sv1 = str(float(fields[20])/100.0)
                    output_item.sp2 = fields[21]
                    output_item.sv2 = str(float(fields[22])/100.0)
                    output_item.sp3 = fields[23]
                    output_item.sv3 = str(float(fields[24])/100.0)
                    output_item.sp4 = fields[25]
                    output_item.sv4 = str(float(fields[26])/100.0)
                    output_item.sp5 = fields[27]
                    output_item.sv5 = str(float(fields[28])/100.0)
                    # fields[29] each deal
                    # fields[30] datetime e.g. '20160727100615'
                    if len(fields[30]) == len('20160727100615'):
                        output_item.date = fields[30][:4] + '-' \
                            + fields[30][4:6] + '-' + fields[30][6:8]
                        output_item.time = fields[30][8:10] + ':' \
                            + fields[30][10:12] + ':' + fields[30][12:14]
                    else:
                        output_item.date = '00-00-00'
                        output_item.time = '00:00:00'
                    # fields[31] price offset
                    # fields[32] price offset ratio
                    output_item.ratio = fields[32]
                    output_item.high = fields[33]
                    output_item.low = fields[34]
                    # fields[35] price/volume/amount
                    # fields[36] volume (shou)
                    # fields[37] amount (wang)
                    output_item.amount = str(round(float(fields[37])/10000.0, 2)) # yiyuan
                    # fields[38] huan shou lv
                    # fields[39] shi ying lv
                    # fields[40] unknown
                    # fields[41] highest
                    # fields[42] lowest
                    # fields[43] zhen fu
                    # fields[44] liu tong shi zhi
                    # fields[45] zong shi zhi
                    # fields[46] shi jing lv
                    # fields[47] zhang ting jia
                    # fields[48] die ting jia
                    
                    outputs.append(output_item)
            else:
                # Failed to parse the data
                pass
        return outputs

    def __parse_data_WY(self, input, items):
        # input: _ntes_quote_callback({"1159915":{"key":"value",...},"":"",...});
        outputs = []
        value = input.strip(';').strip('_ntes_quote_callback').strip('(').strip(')')
        
        try:
            jvalue = json.loads(value)
        except Exception, e:
            print e
            return outputs
        
        for item in items:
            key = ''
            if item[0] == const.SH_STOCK_PREFIX \
                or item[0] == const.SH_ETF_PREFIX \
                or item == const.SHZS:
                key = const.WY_LONG_PREFIX_SH + item
            else:
                key = const.WY_LONG_PREFIX_SZ + item

            output_item = engine_data_item.DataItem()
            output_item.code = str(jvalue[key]['symbol'])
            output_item.name = jvalue[key]['code']
            output_item.price = str(jvalue[key]['price'])
            output_item.ratio = str(round(float(jvalue[key]['percent'])*100, 2))
            output_item.high = str(jvalue[key]['high'])
            output_item.low = str(jvalue[key]['low'])
            output_item.volume = jvalue[key]['volume']
            output_item.amount = str(round(float(jvalue[key]['turnover'])/100000000.0, 2))
            output_item.sv5 = str(round(float(jvalue[key]['askvol5'])/10000.0, 2))
            output_item.sp5 = str(jvalue[key]['ask5'])
            output_item.sv4 = str(round(float(jvalue[key]['askvol4'])/10000.0, 2))
            output_item.sp4 = str(jvalue[key]['ask4'])
            output_item.sv3 = str(round(float(jvalue[key]['askvol3'])/10000.0, 2))
            output_item.sp3 = str(jvalue[key]['ask3'])
            output_item.sv2 = str(round(float(jvalue[key]['askvol2'])/10000.0, 2))
            output_item.sp2 = str(jvalue[key]['ask2'])
            output_item.sv1 = str(round(float(jvalue[key]['askvol1'])/10000.0, 2))
            output_item.sp1 = str(jvalue[key]['ask1'])
            output_item.bv1 = str(round(float(jvalue[key]['bidvol1'])/10000.0, 2))
            output_item.bp1 = str(jvalue[key]['bid1'])
            output_item.bv2 = str(round(float(jvalue[key]['bidvol2'])/10000.0, 2))
            output_item.bp2 = str(jvalue[key]['bid2'])
            output_item.bv3 = str(round(float(jvalue[key]['bidvol3'])/10000.0, 2))
            output_item.bp3 = str(jvalue[key]['bid3'])
            output_item.bv4 = str(round(float(jvalue[key]['bidvol4'])/10000.0, 2))
            output_item.bp4 = str(jvalue[key]['bid4'])
            output_item.bv5 = str(round(float(jvalue[key]['bidvol5'])/10000.0, 2))
            output_item.bp5 = str(jvalue[key]['bid5'])
            value_datetime = jvalue[key]['time'].split(' ')
            if len(value_datetime) == 2:
                output_item.date = value_datetime[0]
                output_item.time = value_datetime[1]

            outputs.append(output_item)
        return outputs

    def __get_ratio(self, last, price):
        if float(last) == 0.0 or float(price) == 0.0:
            return '0.0'
        else:
            ratio = (float(price) - float(last)) / float(last) * 100
            return str(round(ratio, 2))