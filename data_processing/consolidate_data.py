import numpy as np
import pandas as pd
import sys

sys.path.append('../')

symbols = ['SBILIFE','SIEMENS','SBIN','SOUTHBANK']

for symbol in symbols:

    print('Loading ' + symbol + '...')

    data_1min = pd.read_csv(symbol + '_feat_mat_two_1min.csv',index_col='Date',parse_dates=True,infer_datetime_format=True)
    data_5min = pd.read_csv(symbol + '_feat_mat_two_5min.csv',index_col='Date',parse_dates=True,infer_datetime_format=True)
    data_15min = pd.read_csv(symbol + '_feat_mat_two_15min.csv',index_col='Date',parse_dates=True,infer_datetime_format=True)
    data_60min = pd.read_csv(symbol + '_feat_mat_two_60min.csv',index_col='Date',parse_dates=True,infer_datetime_format=True)

    print('Done.')
    print('Processing ' + symbol + '...')

    data_5min_shifted = data_5min.shift(1).add_prefix('5min_')
    data_15min_shifted = data_15min.shift(1).add_prefix('15min_')
    data_60min_shifted = data_60min.shift(1).add_prefix('60min_')

    data_1_5 = pd.concat([data_1min, data_5min_shifted],axis=1)
    data_1_to_15 = pd.concat([data_1_5, data_15min_shifted],axis=1)
    data_1_to_60 = pd.concat([data_1_to_15, data_60min_shifted],axis=1)

    data_1_to_60_filled = data_1_to_60.fillna(method='ffill')

    print('Done.')
    print('creating csv file...')

    data_1_to_60_filled.to_csv(symbol + '_consolidated.csv')

    print('Done with ' + symbol)

print('done')