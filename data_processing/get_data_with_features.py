import pandas as pd
import SWING_TRADING_WQU.data_processing.data_preprocessing as pre_processing
import SWING_TRADING_WQU.indicators.add_indicators as add_indicators


def get_featured_matrix(data_all,datapoint):

    FEATURED_MATRIX = []


    curr_state= pre_processing.get_current_state(data_all,datapoint)
    featured_data = add_indicators.add_pivots(curr_state)
    featured_data = add_indicators.add_overlap_studies(curr_state)
    featured_data = add_indicators.add_momentum_indicators(curr_state)
    featured_data = add_indicators.add_volume_indicators(curr_state)
    featured_data = add_indicators.add_volatility_indicators(curr_state)
    featured_data = add_indicators.add_price_transform_indicators(curr_state)
    featured_data = add_indicators.add_cycle_indicators(curr_state)

    data_1min = featured_data[0][-750:]
    data_1min = data_1min.dropna()

    data_5min = featured_data[1][-750:]
    data_5min = data_5min.dropna()

    data_15min = featured_data[2][-250:]
    data_15min = data_15min.dropna()

    data_30min = featured_data[3][-50:]
    data_30min = data_30min.dropna()

    data_60min = featured_data[4][-50:]
    data_60min = data_60min.dropna()

    data_D = featured_data[5][-90:]
    data_D = data_D.dropna()

    data_W = featured_data[6][-60:]
    data_W = data_W.dropna()

    data_M = featured_data[7][-40:]
    data_M = data_M.dropna()


    FEATURED_MATRIX.append(data_1min.values)
    FEATURED_MATRIX.append(data_5min.values)
    FEATURED_MATRIX.append(data_15min.values)
    FEATURED_MATRIX.append(data_30min.values)
    FEATURED_MATRIX.append(data_60min.values)
    FEATURED_MATRIX.append(data_D.values)
    FEATURED_MATRIX.append(data_W.values)
    FEATURED_MATRIX.append(data_M.values)



    return FEATURED_MATRIX, [data_1min,data_5min,data_15min,data_30min,data_60min,data_D,data_W,data_M]





"""test

path = 'SWING_TRADING_WQU/raw_data/train_data/traindata_set1/'
symbol = 'SBIN'
data_1min,data_daily =  pre_processing.read_train_data(path=path,symbol=symbol)
data_all = pre_processing.get_higher_timeframe(data_1min,data_daily)

datapoint = data_all[0].index[5000]
Feat_mat_list,Feat_mat_2 = get_featured_matrix(data_all,datapoint)

"""


##########
"""
1min = 750 candles  --> 2 days
5min = 375 candles --> 5 days
15 min = 250 --10 days
30 min = 13*15 = 195 
60min - 30days --> 210
daily = 3months ---> 60
weekly -- 1year --> 52
monthly  - 3 year --> 36
"""
