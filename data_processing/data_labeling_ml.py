import sys

sys.path.append('../')

import datetime as dt
import numpy as np
import pandas as pd

VERT_BOUND_MINUTES = 120

raw_data = pd.read_csv('SBIN_consolidated.csv', index_col='Date',parse_dates=True,infer_datetime_format=True)

data_for_labeling = raw_data[['Open','High','Low','Close','Volume','5min_ATR_14']].dropna()

data_for_labeling['upbound_1'] = data_for_labeling['Close'] + data_for_labeling['5min_ATR_14'] #6
data_for_labeling['lowbound_1'] = data_for_labeling['Close'] - data_for_labeling['5min_ATR_14'] #7
data_for_labeling['upbound_3'] = data_for_labeling['Close'] + data_for_labeling['5min_ATR_14']*3 #8
data_for_labeling['lowbound_3'] = data_for_labeling['Close'] - data_for_labeling['5min_ATR_14']*3 #9

data_for_labeling['label'] = np.zeros

for i in range(0, len(data_for_labeling.index)):
    data_time_sliced = data_for_labeling.iloc[i:i+VERT_BOUND_MINUTES]

    upbound_1_rows = data_time_sliced[data_time_sliced['High'] >= data_for_labeling.iloc[i,6]]
    lowbound_1_rows = data_time_sliced[data_time_sliced['Low'] <= data_for_labeling.iloc[i,7]]
    upbound_3_rows = data_time_sliced[data_time_sliced['High'] >= data_for_labeling.iloc[i,8]]
    lowbound_3_rows = data_time_sliced[data_time_sliced['Low'] <= data_for_labeling.iloc[i,9]]

    direction = 0

    upbound_1_ix =  dt.date.today() if upbound_1_rows.empty else upbound_1_rows.index[0]
    lowbound_1_ix = dt.date.today() if lowbound_1_rows.empty else lowbound_1_rows.index[0]
    upbound_3_ix =  dt.date.today() if upbound_3_rows.empty else upbound_3_rows.index[0]
    lowbound_3_ix = dt.date.today() if lowbound_3_rows.empty else lowbound_3_rows.index[0]

    if upbound_3_ix < lowbound_1_ix:
        direction = 1
    if lowbound_3_ix < upbound_1_ix:
        direction = -1

    data_for_labeling.iat[i,10] = direction
    
    print(i)

print('done')