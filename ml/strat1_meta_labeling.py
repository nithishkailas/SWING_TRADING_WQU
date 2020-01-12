import sys

sys.path.append('../')

import datetime as dt
import numpy as np
import pandas as pd

symbols = ['BHEL','BIOCON','KOTAKBANK','LT','LUPIN','NATIONALUM','PCJEWELLER']

for symbol in symbols:

	print('processing ' + symbol)

	raw_data = pd.read_csv('data/' + symbol + '_consolidated.csv', index_col='Date',parse_dates=True,infer_datetime_format=True)

	data_for_labeling = raw_data[['Open','High','Low','Close','Volume','MA_5','MA_20']].dropna()

	data_for_labeling['upbound_1'] = data_for_labeling['Close'] * 1.01 #7
	data_for_labeling['lowbound_1'] = data_for_labeling['Close'] * 0.99 #8
	data_for_labeling['upbound_3'] = data_for_labeling['Close'] * 1.02 #9
	data_for_labeling['lowbound_3'] = data_for_labeling['Close'] * 0.98 #10

	data_for_labeling['label'] = np.zeros
	data_for_labeling['meta_label'] = np.zeros
	data_for_labeling['exit_price'] = np.zeros

	now = dt.datetime.now()

	for i in range(1, len(data_for_labeling.index)):	
		ma_cross = 0
		
		if data_for_labeling.iloc[i-1,5] < data_for_labeling.iloc[i-1,6] and data_for_labeling.iloc[i,5] > data_for_labeling.iloc[i,6]:
			ma_cross = 1
		elif data_for_labeling.iloc[i-1,5] > data_for_labeling.iloc[i-1,6] and data_for_labeling.iloc[i,5] < data_for_labeling.iloc[i,6]:
			ma_cross = -1

		data_for_labeling.iat[i,11] = ma_cross
		
		print(i)
		
	for i in range(1, len(data_for_labeling.index)):

		ma_cross = data_for_labeling.iat[i,11]
		meta_label = 0
		
		events_df = data_for_labeling[data_for_labeling['label'] != 0]	

		if ma_cross == 1:
		
			curr_cross_ix = events_df.index.get_loc(data_for_labeling.index[i])
			
			vert_bound_ix = -1 if curr_cross_ix >= len(events_df) else data_for_labeling.index.get_loc(events_df.index[curr_cross_ix+1])
		
			data_time_sliced = data_for_labeling.iloc[i:vert_bound_ix]
		
			lowbound_1_rows = data_time_sliced[data_time_sliced['Low'] <= data_for_labeling.iloc[i,8]]
			upbound_3_rows = data_time_sliced[data_time_sliced['High'] >= data_for_labeling.iloc[i,9]]
			
			lowbound_1_ix = now if lowbound_1_rows.empty else lowbound_1_rows.index[0]
			upbound_3_ix =  now if upbound_3_rows.empty else upbound_3_rows.index[0]
			
			if upbound_3_ix < lowbound_1_ix:
				meta_label = 1
			elif upbound_3_ix > lowbound_1_ix:
				meta_label = -1
			elif lowbound_1_rows.empty and upbound_3_rows.empty:
				if len(data_time_sliced) > 1 and data_time_sliced.iloc[0,3] < data_time_sliced.iloc[-1,3]:
					meta_label = 1
				else:
					meta_label = -1
				
			
		elif ma_cross == -1:
		
			curr_cross_ix = events_df.index.get_loc(data_for_labeling.index[i])
			
			vert_bound_ix = -1 if curr_cross_ix < len(events_df) else data_for_labeling.index.get_loc(events_df.index[curr_cross_ix+1])
		
			data_time_sliced = data_for_labeling.iloc[i:vert_bound_ix]
			
			upbound_1_rows = data_time_sliced[data_time_sliced['High'] >= data_for_labeling.iloc[i,7]]
			lowbound_3_rows = data_time_sliced[data_time_sliced['Low'] <= data_for_labeling.iloc[i,10]]

			upbound_1_ix =  now if upbound_1_rows.empty else upbound_1_rows.index[0]
			lowbound_3_ix = now if lowbound_3_rows.empty else lowbound_3_rows.index[0]
			
			if lowbound_3_ix < upbound_1_ix:
				meta_label = -1
			elif lowbound_3_ix > upbound_1_ix:
				meta_label = 1
			elif upbound_1_rows.empty and lowbound_3_rows.empty:
				if len(data_time_sliced) > 1 and data_time_sliced.iloc[0,3] > data_time_sliced.iloc[-1,3]:
					meta_label = -1
				else:
					meta_label = 1
					
		data_for_labeling.iat[i,12] = meta_label

	data_for_labeling.to_csv('strat1_' + symbol + '_meta_labeled.csv')
	
	print('done')

print('completed')