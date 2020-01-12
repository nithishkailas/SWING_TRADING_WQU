import sys

sys.path.append('../')

import numpy as np
import pandas as pd

def get_features(raw_data):

	features = pd.DataFrame(index=raw_data.index)

	features['above_BBU_14_2'] = 0
	features['below_BBL_14_2'] = 0
	features['above_BBU_14_3'] = 0
	features['below_BBL_14_3'] = 0
	features['above_BBU_20_2'] = 0
	features['below_BBL_20_2'] = 0

	features['sma_align'] = 0

	features['5_min_above_BBU_14_2'] = 0
	features['5_min_below_BBL_14_2'] = 0
	features['5_min_above_BBU_14_3'] = 0
	features['5_min_below_BBL_14_3'] = 0
	features['5_min_above_BBU_20_2'] = 0
	features['5_min_below_BBL_20_2'] = 0

	features['5_min_sma_align'] = 0

	features['60_min_above_BBU_14_2'] = 0
	features['60_min_below_BBL_14_2'] = 0
	features['60_min_above_BBU_14_3'] = 0
	features['60_min_below_BBL_14_3'] = 0
	features['60_min_above_BBU_20_2'] = 0
	features['60_min_below_BBL_20_2'] = 0

	features['60_min_sma_align'] = 0

	for i in range(0,len(raw_data.index)):
		print(i)
		features.at[features.index[i], 'above_BBU_14_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'BBU_14_2'] else 0
		features.at[features.index[i], 'below_BBL_14_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'BBL_14_2'] else 0
		features.at[features.index[i], 'above_BBU_14_3'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'BBU_14_3'] else 0
		features.at[features.index[i], 'below_BBL_14_3'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'BBL_14_3'] else 0
		features.at[features.index[i], 'above_BBU_20_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'BBU_20_2'] else 0
		features.at[features.index[i], 'below_BBL_20_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'BBU_20_2'] else 0

		features.at[features.index[i], '5min_above_BBU_14_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'5min_BBU_14_2'] else 0
		features.at[features.index[i], '5min_below_BBL_14_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'5min_BBL_14_2'] else 0
		features.at[features.index[i], '5min_above_BBU_14_3'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'5min_BBU_14_3'] else 0
		features.at[features.index[i], '5min_below_BBL_14_3'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'5min_BBL_14_3'] else 0
		features.at[features.index[i], '5min_above_BBU_20_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'5min_BBU_20_2'] else 0
		features.at[features.index[i], '5min_below_BBL_20_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'5min_BBU_20_2'] else 0

		features.at[features.index[i], '60_min_above_BBU_14_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'60min_BBU_14_2'] else 0
		features.at[features.index[i], '60_min_below_BBL_14_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'60min_BBL_14_2'] else 0
		features.at[features.index[i], '60_min_above_BBU_14_3'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'60min_BBU_14_3'] else 0
		features.at[features.index[i], '60_min_below_BBL_14_3'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'60min_BBL_14_3'] else 0
		features.at[features.index[i], '60_min_above_BBU_20_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  > raw_data.loc[raw_data.index[i],'60min_BBU_20_2'] else 0
		features.at[features.index[i], '60_min_below_BBL_20_2'] = 1 if raw_data.loc[raw_data.index[i],'Close']  < raw_data.loc[raw_data.index[i],'60min_BBL_20_2'] else 0

		if raw_data.loc[raw_data.index[i],'MA_5'] > raw_data.loc[raw_data.index[i],'MA_8'] > raw_data.loc[raw_data.index[i],'MA_14'] > raw_data.loc[raw_data.index[i],'MA_20']:
			features.at[features.index[i], 'sma_align'] = 1
		elif raw_data.loc[raw_data.index[i],'MA_5'] < raw_data.loc[raw_data.index[i],'MA_8'] < raw_data.loc[raw_data.index[i],'MA_14'] < raw_data.loc[raw_data.index[i],'MA_20']:
			features.at[features.index[i], 'sma_align'] = -1

		if raw_data.loc[raw_data.index[i],'5min_MA_5'] > raw_data.loc[raw_data.index[i],'5min_MA_8'] > raw_data.loc[raw_data.index[i],'5min_MA_14'] > raw_data.loc[raw_data.index[i],'5min_MA_20']:
			features.at[features.index[i], '5min_sma_align'] = 1
		elif raw_data.loc[raw_data.index[i],'5min_MA_5'] < raw_data.loc[raw_data.index[i],'5min_MA_8'] < raw_data.loc[raw_data.index[i],'5min_MA_14'] < raw_data.loc[raw_data.index[i],'5min_MA_20']:
			features.at[features.index[i], '5min_sma_align'] = -1

		if raw_data.loc[raw_data.index[i],'60min_MA_5'] > raw_data.loc[raw_data.index[i],'60min_MA_8'] > raw_data.loc[raw_data.index[i],'60min_MA_14'] > raw_data.loc[raw_data.index[i],'60min_MA_20']:
			features.at[features.index[i], '60_min_sma_align'] = 1
		elif raw_data.loc[raw_data.index[i],'60min_MA_5'] < raw_data.loc[raw_data.index[i],'60min_MA_8'] < raw_data.loc[raw_data.index[i],'60min_MA_14'] < raw_data.loc[raw_data.index[i],'60min_MA_20']:
			features.at[features.index[i], '60_min_sma_align'] = -1

	indicator_col_list = ['ADX_14','AROONOSC_14','BOP','CCI_14','DMI_14','RSI_14','slowk','slowd','fastk','fastd','WILLR_14','HT_TRENDMODE',\
	'5min_ADX_14','5min_AROONOSC_14','5min_BOP','5min_CCI_14','5min_DMI_14','5min_RSI_14','5min_slowk','5min_slowd','5min_fastk','5min_fastd','5min_WILLR_14','5min_HT_TRENDMODE']

	indicators = raw_data[indicator_col_list]

	features_full = pd.concat([features,indicators],axis=1)

	return features_full