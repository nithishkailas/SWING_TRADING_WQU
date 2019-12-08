import pandas as pd
import datetime

def read_train_data(path,symbol):
    dataframe_1min = pd.read_csv(path + symbol + "-1m.csv")
    dataframe_daily = pd.read_csv(path+symbol+"-D.csv")

    column_names = {symbol + '-EQ O': 'Open', symbol + '-EQ H': 'High', symbol + '-EQ L': 'Low',
                        symbol + '-EQ C': 'Close', symbol + '-EQ V': 'Volume'}

    dataframe_1min = dataframe_1min.rename(columns=column_names)
    dates = []
    for i in dataframe_1min.Date:

        try:
            t = datetime.datetime.strptime(i, "%d/%m/%Y %H:%M")
        except:
            t = datetime.datetime.strptime(i, "%d/%m/%y %H:%M")
        dates.append(t)

    dataframe_1min.Date = dates
    dataframe_1min = dataframe_1min[::-1]
    dataframe_1min.index = dataframe_1min.Date
    dataframe_1min['symbol'] =symbol

    dataframe_daily = dataframe_daily.rename(columns=column_names)
    dailydates = []

    for i in dataframe_daily.Date:

        try:
            t = datetime.datetime.strptime(i, "%d/%m/%Y")
        except:
            t = datetime.datetime.strptime(i, "%d/%m/%y")
        dailydates.append(t)
    dataframe_daily.Date = dailydates
    dataframe_daily = dataframe_daily[::-1]
    dataframe_daily.index = dataframe_daily.Date
    dataframe_daily['symbol'] = symbol

    return dataframe_1min,dataframe_daily


def get_higher_timeframe(dataframe,dataframe_daily):

    data_1min = dataframe
    data_5min = dataframe.resample('5T').agg({'Open': 'first',
                                              'High': 'max',
                                              'Low': 'min',
                                              'Close': 'last',
                                              'Volume': 'sum'})

    data_15min = dataframe.resample('15T').agg({'Open': 'first',
                                                'High': 'max',
                                                'Low': 'min',
                                                'Close': 'last',
                                                'Volume': 'sum'})

    data_30min = dataframe.resample('30T', base=15).agg({'Open': 'first',
                                                         'High': 'max',
                                                         'Low': 'min',
                                                         'Close': 'last',
                                                         'Volume': 'sum'})
    data_60min = dataframe.resample('60T', base=15).agg({'Open': 'first',
                                                         'High': 'max',
                                                         'Low': 'min',
                                                         'Close': 'last',
                                                         'Volume': 'sum'})

    data_Daily = dataframe_daily

    data_Weekly = dataframe_daily.resample('W-MON', closed='left', label='left').agg({'Open': 'first',
                                               'High': 'max',
                                               'Low': 'min',
                                               'Close': 'last',
                                               'Volume': 'sum'})



    data_Monthly = dataframe_daily.resample('MS').agg({'Open': 'first',
                                                'High': 'max',
                                                'Low': 'min',
                                                'Close': 'last',
                                                'Volume': 'sum'})

    data_5min = data_5min.dropna()
    data_15min = data_15min.dropna()
    data_30min = data_30min.dropna()
    data_60min = data_60min.dropna()
    data_Daily = data_Daily.dropna()
    data_Weekly = data_Weekly.dropna()
    data_Monthly = data_Monthly.dropna()

    return [data_1min,data_5min,data_15min,data_30min,data_60min,data_Daily,data_Weekly,data_Monthly]




##########
##Technical Analysis
##

#1.Features to represent the price level
#2.Price Pattern
"""
From the understranding of Technical analysis we are looking at the market from multiple timeframes. 
The larger timeframes will mostly have indicator matrix to identify trends and also support and resistance
levels.The smaller timeframes will have oscillators and fast moving averages and volatility indicators.

So we want to get the corresponding state of the market at all timeframes when a new 1 min candle forms.

"""
#Designing price level matrix
"""
Weekly : The algorithm will have information of last 5 weeks of data with monthly standard and fibonacci pivots.
Daily : 1 month daily data with MAs, BBB, MACDs.
60 min,30min : It will have trend indicators and also some oscillators and it will have weekly pivots
15min,5min : for patterns, also fast moving averages, bollingers and daily pivots.
1min : will have moving average ribbons and bollinger bands of 2 and 3 stds.

"""



def get_current_state(stock, data_point):
    current_state = []
    current_state.append(stock[0].loc[:data_point])
    for i in range(1, len(stock)):


        df_o = stock[i].loc[:data_point]

        df = df_o.copy(deep=True)
        mask = stock[0].loc[df.index[-1]:data_point]

        df['Open'][df.index[-1]] = mask.Open[0]
        df['High'][df.index[-1]] = max(mask.High)
        df['Low'][df.index[-1]] = min(mask.Low)
        df['Close'][df.index[-1]] = mask.Close[-1]
        df['Volume'][df.index[-1]] = sum(mask.Volume)
        current_state.append(df)

    return current_state



##########################
#Adding technical indicators
#





"""
#######test
path = 'SWING_TRADING_WQU/raw_data/'
symbol = 'SBIN'
sbin = read_data(path=path,symbol=symbol)

sbin_all = get_higher_timeframe(sbin)

sbin_1min = sbin_all[0]
sbin_5min = sbin_all[1]
sbin_15min = sbin_all[2]
sbin_30min = sbin_all[3]
sbin_60min = sbin_all[4]
sbin_daily = sbin_all[5]
sbin_weekly = sbin_all[6]
sbin_monthly = sbin_all[7]




#test
stock = sbin_all
data_point = '2019-11-11 15:12:00+05:30'
curr_state = get_current_state(stock,data_point)


data_list =sbin_all


#test
new_data_list = add_technical_indicators(data_list)

###
"""

