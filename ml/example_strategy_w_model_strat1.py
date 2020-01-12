
import sys
sys.path.append('../')

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

#Set this constant to True if you want to run the backtest with only the base strategy rules and ignore the machine learning model signal
DEBUG_BASE_ONLY = False

#use this constant to set the number of shares traded per trade
QTY = 1

sample_data = pd.read_csv('data/NATIONALUM_consolidated.csv')
sample_data_features_raw = pd.read_csv('data/strat1_NATIONALUM_features_no_hourly.csv',index_col='Date',parse_dates=True,infer_datetime_format=True)

features = sample_data_features_raw.fillna(method='ffill')
features_no_nan = features.dropna()
features_final = features_no_nan.drop('side',axis=1).drop('label',axis=1)

model = pickle.load(open('randomforestmodel_strat1.sav','rb'))

sample_data.head()

sample_data.Date = pd.to_datetime(sample_data.Date)


from portfolio.portfolio import Portfolio
from order.order import Order

import datetime

SMA_portfolio = Portfolio('Strat1',datetime.date,100000)

print(SMA_portfolio.TotalCapital)

#we start backtesting from the beginning of the 'test dataset' while training the ML model
i=sample_data[sample_data.Date == '2018-12-12 14:21:00'].index[0]

while i < len(sample_data.values):
    print(i)
    new_data_point = sample_data.loc[i]
    prev_data_point = sample_data.loc[i-1]

    if prev_data_point.MA_5 < prev_data_point.MA_20 and new_data_point.MA_5>new_data_point.MA_20:
		
		new_data_point_features = features_final.loc[new_data_point.Date].values.reshape(1, -1)
		
		signal = model.predict(new_data_point_features)
		
		if signal == 1 or DEBUG_BASE_ONLY:
		
			print("Long Entry Signal")
			Long_Entry_price = new_data_point.Close
			Long_Stop_Price = new_data_point.Close * 0.99
			Long_Target_Price = new_data_point.Close * 1.02
			Long_Quantity = QTY
			Long_Max_Holding_period = datetime.datetime.now()
			Long_Order = Order(SMA_portfolio,new_data_point.symbol,'Long',new_data_point.Date,Long_Entry_price,
							   Long_Target_Price,Long_Stop_Price,Long_Quantity,Long_Max_Holding_period,5)

			if SMA_portfolio.FreeCapital > Long_Order.margin_required:
				SMA_portfolio.add(Long_Order)
				
		open_trades = SMA_portfolio.Open_Trades
			
		for trade in open_trades:
			if trade.direction == 'Short':
				trade.max_holding_period = new_data_point.Date


    if prev_data_point.MA_5 > prev_data_point.MA_20 and new_data_point.MA_5<new_data_point.MA_20:
	
		new_data_point_features = features_final.loc[new_data_point.Date].values.reshape(1, -1)
		
		signal = model.predict(new_data_point_features)
		
		if signal == -1 or DEBUG_BASE_ONLY:
		
			print("Short Entry Signal")
			Short_Entry_price = new_data_point.Close
			Short_Stop_Price = new_data_point.Close * 1.01
			Short_Target_Price = new_data_point.Close -0.98
			Short_Quantity = QTY
			Short_Max_Holding_period = min(new_data_point.Date + datetime.timedelta(hours =2), new_data_point.Date.replace(hour = 15,minute =15) )
			Short_Order = Order(SMA_portfolio,new_data_point.symbol,'Short',new_data_point.Date,Short_Entry_price,
							   Short_Target_Price,Short_Stop_Price,Short_Quantity,Short_Max_Holding_period,5)

			if SMA_portfolio.FreeCapital > Short_Order.margin_required:
				SMA_portfolio.add(Short_Order)
				
		open_trades = SMA_portfolio.Open_Trades
			
		for trade in open_trades:
			if trade.direction == 'Long':
				trade.max_holding_period = new_data_point.Date

    SMA_portfolio.tracker(new_data_point)

    i+=1


print("---------------------------------------------")
SMA_portfolio.get_portfolio_stats()


#Sample_Trade = SMA_portfolio.Closed_Trades[22]


#SMA_portfolio.plot_trade(Sample_Trade)




