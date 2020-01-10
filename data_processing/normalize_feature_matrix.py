import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import talib

#Overlap Studies Normalize using Cumulative percentage return.
#key = Current Close value
Overlap_Study_Columns = ['M1_Open', 'M1_High', 'M1_Low', 'M1_Close',
                         'M1_BBU_14_2', 'M1_BBL_14_2', 'M1_BBU_14_3', 'M1_BBL_14_3',
                         'M1_BBU_20_2', 'M1_BBL_20_2', 'M1_DEMA_20', 'M1_EMA_20', 'M1_HT_T',
                         'M1_KAMA_20', 'M1_MA_5', 'M1_MA_8', 'M1_MA_14', 'M1_MA_20', 'M1_MP_14',
                         'M1_MPP_14', 'M1_SAR', 'M1_TEMA_20', 'M1_TRIMA_20', 'M1_WMA_20',

                        'M5_Open', 'M5_High', 'M5_Low', 'M5_Close',
                        'M5_BBU_14_2', 'M5_BBL_14_2', 'M5_BBU_14_3', 'M5_BBL_14_3',
                        'M5_BBU_20_2', 'M5_BBL_20_2', 'M5_DEMA_20', 'M5_EMA_20', 'M5_HT_T',
                        'M5_KAMA_20', 'M5_MA_5', 'M5_MA_8', 'M5_MA_14', 'M5_MA_20', 'M5_MP_14',
                        'M5_MPP_14', 'M5_SAR', 'M5_TEMA_20', 'M5_TRIMA_20', 'M5_WMA_20',

                        'M15_Open', 'M15_High', 'M15_Low', 'M15_Close',
                        'M15_BBU_14_2', 'M15_BBL_14_2', 'M15_BBU_14_3', 'M15_BBL_14_3',
                        'M15_BBU_20_2', 'M15_BBL_20_2', 'M15_DEMA_20', 'M15_EMA_20', 'M15_HT_T',
                        'M15_KAMA_20', 'M15_MA_5', 'M15_MA_8', 'M15_MA_14', 'M15_MA_20',
                        'M15_MP_14', 'M15_MPP_14', 'M15_SAR', 'M15_TEMA_20', 'M15_TRIMA_20',
                        'M15_WMA_20',

                        'M30_Open', 'M30_High', 'M30_Low', 'M30_Close',
                        'M30_BBU_14_2', 'M30_BBL_14_2', 'M30_BBU_14_3', 'M30_BBL_14_3',
                        'M30_BBU_20_2', 'M30_BBL_20_2', 'M30_DEMA_20', 'M30_EMA_20', 'M30_HT_T',
                        'M30_KAMA_20', 'M30_MA_5', 'M30_MA_8', 'M30_MA_14', 'M30_MA_20',
                        'M30_MP_14', 'M30_MPP_14', 'M30_SAR', 'M30_TEMA_20', 'M30_TRIMA_20',
                        'M30_WMA_20',

                        'M60_Open', 'M60_High', 'M60_Low', 'M60_Close',
                        'M60_BBU_14_2', 'M60_BBL_14_2', 'M60_BBU_14_3', 'M60_BBL_14_3',
                        'M60_BBU_20_2', 'M60_BBL_20_2', 'M60_DEMA_20', 'M60_EMA_20', 'M60_HT_T',
                        'M60_KAMA_20', 'M60_MA_5', 'M60_MA_8', 'M60_MA_14', 'M60_MA_20',
                        'M60_MP_14', 'M60_MPP_14', 'M60_SAR', 'M60_TEMA_20', 'M60_TRIMA_20',
                        'M60_WMA_20',

                        'D_Open', 'D_High', 'D_Low', 'D_Close',
                        'D_BBU_14_2', 'D_BBL_14_2', 'D_BBU_14_3', 'D_BBL_14_3', 'D_BBU_20_2',
                        'D_BBL_20_2', 'D_DEMA_20', 'D_EMA_20', 'D_HT_T', 'D_KAMA_20', 'D_MA_5',
                        'D_MA_8', 'D_MA_14', 'D_MA_20', 'D_MP_14', 'D_MPP_14', 'D_SAR',
                        'D_TEMA_20', 'D_TRIMA_20', 'D_WMA_20',

                        'W_Open', 'W_High', 'W_Low', 'W_Close',
                        'W_BBU_14_2', 'W_BBL_14_2', 'W_BBU_14_3', 'W_BBL_14_3', 'W_BBU_20_2',
                        'W_BBL_20_2', 'W_DEMA_20', 'W_EMA_20', 'W_HT_T', 'W_KAMA_20', 'W_MA_5',
                        'W_MA_8', 'W_MA_14', 'W_MA_20', 'W_MP_14', 'W_MPP_14', 'W_SAR',
                        'W_TEMA_20', 'W_TRIMA_20', 'W_WMA_20',

                        'M_Open', 'M_High', 'M_Low', 'M_Close',
                        'M_BBU_14_2', 'M_BBL_14_2', 'M_BBU_14_3', 'M_BBL_14_3', 'M_BBU_20_2',
                        'M_BBL_20_2', 'M_DEMA_20', 'M_EMA_20', 'M_HT_T', 'M_KAMA_20', 'M_MA_5',
                        'M_MA_8', 'M_MA_14', 'M_MA_20', 'M_MP_14', 'M_MPP_14', 'M_SAR',
                        'M_TEMA_20', 'M_TRIMA_20', 'M_WMA_20'
                         ]


####ADX and ADXR
#ADX Value -Range 0 -100 so use min max scaler to normalize between 0 and 1
adx_scaler = MinMaxScaler(feature_range=(0,1))
adx_fit_list = np.array([0,100]).astype(float).reshape(-1,1)
adx_scaler.fit_transform(adx_fit_list)
# ADX_columns
ADX_columns = ['M1_ADX_14', 'M5_ADX_14', 'M15_ADX_14', 'M30_ADX_14', 'M60_ADX_14', 'D_ADX_14', 'W_ADX_14', 'M_ADX_14']
ADXR_columns = ['M1_ADXR_14', 'M5_ADXR_14', 'M15_ADXR_14', 'M30_ADXR_14', 'M60_ADXR_14', 'D_ADXR_14', 'W_ADXR_14', 'M_ADXR_14']


# Candle Stick patterns range -100 to 100 normalize using minmax scaler
CDL_columns = []
prefix_list = ['M1_', 'M5_', 'M15_', 'M30_', 'M60_', 'D_', 'W_', 'M_']
for x in prefix_list:
    for name in talib.get_function_groups()['Pattern Recognition']:
        CDL_columns.append(x + name)

cdl_scaler = MinMaxScaler(feature_range=(-1, 1))
cdl_scaler_list = np.array([-100, 100]).astype(float).reshape(-1, 1)
cdl_scaler.fit_transform(cdl_scaler_list)

#APO scale using cumulative ratio to close
APO_columns = []
for x in prefix_list:
    APO_columns.append(x + 'APO')


#AROON range 0-100 use adx scaler here also
Aroon_columns = []
Aroon_column_names = ['Aroon_down_14', 'Aroon_up_14', 'AROONOSC_14']
for x in prefix_list:
    for y in Aroon_column_names:
        Aroon_columns.append(x + y)

#BOP value is between -1 and 1 so no need to normalize
BOP_columns =[]
for x in prefix_list:
    BOP_columns.append(x + 'BOP')

#CCI - range outside -100,100 is possible but scale using cdlscaler
#CMO - range -100 to 100
CCI_CMO_Columns = []
for x in prefix_list:
    for y in ['CCI_14','CMO_14']:
        CCI_CMO_Columns.append(x + y)

#DMI range -0 to 100
DMI_columns =[]
for x in prefix_list:
    for y in ['DMI_14']:
        DMI_columns.append(x + y)

#Price transform columns -- cumulative percent change
pt_columns = []
pt_column_names = ['AVERAGE', 'MEDPRICE', 'TYPPRICE','WCLPRICE']
for x in prefix_list:
    for y in pt_column_names:
        pt_columns.append(x + y)

#SQRT
sqrt_columns =[]
for x in prefix_list:
    for y in ['SQRT']:
        sqrt_columns.append(x + y)

set_cum_per = ['LINEARREG','TSF','LINEARREG_INTERCEPT','CEIL','FLOOR']
set_cum_per_columns = []
for x in prefix_list:
    for y in set_cum_per:
        set_cum_per_columns.append(x + y)

set_1_1 = ['CORREL','SIN','BETA','COS','HT_SINE_sine','HT_SINE_leadsine','HT_TRENDMODE','NATR_14']
set_1_1_columns = []
for x in prefix_list:
    for y in set_1_1:
        set_1_1_columns.append(x + y)

#SET 0-100
set_0_100 = ['HT_DCPERIOD','ULTOSC','fastd','slowd','fastk','slowk','RSI_14']
set_0_100_columns = []
for x in prefix_list:
    for y in set_0_100:
        set_0_100_columns.append(x + y)

#-45 to 315
angle_45_315_scaler = MinMaxScaler(feature_range=(0,1))
angle_45_315_list = np.array([-45,315]).astype(float).reshape(-1,1)
angle_45_315_scaler.fit_transform(angle_45_315_list)
set_45_315 = ['HT_DCPHASE']
set_45_315_columns = []
for x in prefix_list:
    for y in set_45_315:
        set_45_315_columns.append(x + y)


#-90 to 90
angle_90_90_scaler = MinMaxScaler(feature_range=(0,1))
angle_90_90_list = np.array([-90,90]).astype(float).reshape(-1,1)
angle_90_90_scaler.fit_transform(angle_90_90_list)
set_90_90 = ['LINEARREG_ANGLE']
set_90_90_columns = []
for x in prefix_list:
    for y in set_90_90:
        set_90_90_columns.append(x + y)


set_cum_ratio = ['ATR_14']
set_cum_ratio_columns = []
for x in prefix_list:
    for y in set_cum_ratio:
        set_cum_ratio_columns.append(x + y)

#WILLR -100-0
willr_scaler = MinMaxScaler(feature_range=(-1,0))
willr_list = np.array([-100,0]).astype(float).reshape(-1,1)
willr_scaler.fit_transform(willr_list)
willr_columns = []
for x in prefix_list:
    for y in ['WILLR_14']:
        willr_columns.append(x + y)


def normalize_matrix(Featured_Dataframe):
    Normalized_Dataframe = pd.DataFrame()

    #OVERLAP STUDIES
    key = Featured_Dataframe['M1_Close'][24]
    for column in Overlap_Study_Columns:
        Normalized_Dataframe[column] = (Featured_Dataframe[column]-key)/key*100

    #ADX & ADXR
    for column in ADX_columns:
        Normalized_Dataframe[column] = adx_scaler.transform(Featured_Dataframe[column].values.reshape(-1,1))
    for column in ADXR_columns:
        Normalized_Dataframe[column] = adx_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    #CDL patterns
    for column in CDL_columns:
        Normalized_Dataframe[column] = cdl_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    #APO
    for column in APO_columns:
        Normalized_Dataframe[column] = (Featured_Dataframe[column]) / key * 100

    #Aroon
    for column in Aroon_columns:
        Normalized_Dataframe[column] = adx_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    #BOP
    for column in BOP_columns:
        Normalized_Dataframe[column] = Featured_Dataframe[column]

    # CCI and CMO
    for column in CCI_CMO_Columns:
        Normalized_Dataframe[column] = cdl_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    #DMI
    for column in DMI_columns:
        Normalized_Dataframe[column] = adx_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    #PTransform -Avg,Typ,WCl, median prices
    for column in pt_columns:
        Normalized_Dataframe[column] = (Featured_Dataframe[column]-key)/key*100

    #set cum per
    for column in set_cum_per_columns:
        Normalized_Dataframe[column] = (Featured_Dataframe[column] - key) / key * 100

    # set cum per
    for column in set_cum_ratio_columns:
        Normalized_Dataframe[column] = (Featured_Dataframe[column]) / key * 100

    #set_1_1
    for column in set_1_1_columns:
        Normalized_Dataframe[column] = Featured_Dataframe[column]

    #sqrt
    for column in sqrt_columns:
        Normalized_Dataframe[column] = (Featured_Dataframe[column] - np.sqrt(key)) / np.sqrt(key) * 100

    #set0-100
    for column in set_0_100_columns:
        Normalized_Dataframe[column] = adx_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    # -45-315
    for column in set_45_315_columns:
        Normalized_Dataframe[column] = angle_45_315_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    # -90-90
    for column in set_90_90_columns:
        Normalized_Dataframe[column] = angle_90_90_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))

    #Willr
    for column in willr_columns:
        Normalized_Dataframe[column] = willr_scaler.transform(Featured_Dataframe[column].values.reshape(-1, 1))


Featured_Dataframe.columns[40:50]
maxi = max(y.values)
mini= min(y.values)

pivots = []

y = Featured_Dataframe['M_PPO']
F
maxi = max(maxi, max(y.values))
mini = min(mini, min(y.values))

360 - 45


#
#0-100
#HT_DCPERIOD
#
#-45to315
#HT_DCPHASE

#0,1
HT-Trendmode
#-1,1
HT-sine,Ht leadsine

#



set_0_1 = ['HT-Trendmode']
set_100_100 = []
set_45_315 = ['HT_DCPHASE']




for i in range(len(Featured_Dataframe.columns)):
    print(i," : ",Featured_Dataframe.columns[i])


Featured_Dataframe['M15_VOLUME_MA_14'].values[0]

pivot_columns = ['daily_pivots_Standard_PP',]



#50 rows to go
(1264-864)/8
#35 to go
(1264-984)/8

from statsmodels.tsa.stattools import adfuller

X = data_all[2].Volume
result = adfuller(X)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
print('\t%s: %.3f' % (key, value))


import talib
avg_volume = talib.MA(X,5)

X.plot()
avg_volume.plot()