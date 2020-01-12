import numpy as np
import pandas as pd

ticker_list = ['BIOCON','KOTAKBANK','LT','LICHSGFIN','LUPIN','NATIONALUM','PCJEWELLER']
base = pd.read_csv('data/BHEL_features_no_hourly.csv',index_col='Date',parse_dates=True,infer_datetime_format=True).drop('label',axis=1).drop('meta_label',axis=1)

cols = base.columns

for ticker in ticker_list:
	print('processing ' + ticker + '...')
	raw_file = pd.read_csv('data/' + ticker + '_features.csv',index_col='Date',parse_dates=True,infer_datetime_format=True)
	
	formatted_file = raw_file[cols]
	
	formatted_file.to_csv('data/' + ticker + '_features_no_hourly.csv')
	
	print('done with ' + ticker)
	
print('Done with all.')

