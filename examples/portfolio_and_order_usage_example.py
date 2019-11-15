

import pandas as pd

sample_data = pd.read_csv("SWING_TRADING_WQU/examples/sample_data/TATAMOTORS-15min.csv")

sample_data.head()

sample_data['symbol'] = 'TATAMOTORS'
sample_data.Date = pd.to_datetime(sample_data.Date)

sample_data['SMA200'] = sample_data.Close.rolling(window = 200).mean()

#Strategy GO long if price crosees 200SMA from below, stop 1% below 200sam , target 2% above 200SMA
# .Max holding period 4hrs.

# Go Short if Price Croses 200SMA from above.Stop and target reverse

from SWING_TRADING_WQU.portfolio.portfolio import Portfolio
from SWING_TRADING_WQU.order.order import Order

import datetime

SMA_portfolio = Portfolio('SMA200_Crossover',datetime.date,10000)

SMA_portfolio.issue_capital(2000)

print(SMA_portfolio.TotalCapital)

i=1
while i < len(sample_data.values):
    new_data_point = sample_data.loc[i]
    prev_data_point = sample_data.loc[i-1]

    if prev_data_point.Close < prev_data_point.SMA200 and new_data_point.Close>new_data_point.SMA200:
        print("Long Entry Signal")
        Long_Entry_price = new_data_point.Close
        Long_Stop_Price = new_data_point.SMA200 * 0.99
        Long_Target_Price = new_data_point.Close * 1.02
        Long_Quantity = 10
        Long_Max_Holding_period = min(new_data_point.Date + datetime.timedelta(hours =4), new_data_point.Date.replace(hour = 15,minute =15) )
        Long_Order = Order(SMA_portfolio,new_data_point.symbol,'Long',new_data_point.Date,Long_Entry_price,
                           Long_Target_Price,Long_Stop_Price,Long_Quantity,Long_Max_Holding_period,5)

        if SMA_portfolio.FreeCapital > Long_Order.margin_required:
            SMA_portfolio.add(Long_Order)


    if prev_data_point.Close > prev_data_point.SMA200 and new_data_point.Close<new_data_point.SMA200:
        print("Short Entry Signal")
        Short_Entry_price = new_data_point.Close
        Short_Stop_Price = new_data_point.SMA200 * 1.01
        Short_Target_Price = new_data_point.Close * 0.98
        Short_Quantity = 10
        Short_Max_Holding_period = min(new_data_point.Date + datetime.timedelta(hours =4), new_data_point.Date.replace(hour = 15,minute =15) )
        Short_Order = Order(SMA_portfolio,new_data_point.symbol,'Short',new_data_point.Date,Short_Entry_price,
                           Short_Target_Price,Short_Stop_Price,Short_Quantity,Short_Max_Holding_period,5)

        if SMA_portfolio.FreeCapital > Short_Order.margin_required:
            SMA_portfolio.add(Short_Order)

    SMA_portfolio.tracker(new_data_point)

    i+=1


print("---------------------------------------------")
SMA_portfolio.get_portfolio_stats()


Sample_Trade = SMA_portfolio.Closed_Trades[22]


SMA_portfolio.plot_trade(Sample_Trade)




