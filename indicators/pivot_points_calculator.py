

def standard_pivot_points(Candlestick):

    PP = (Candlestick.High + Candlestick.Low + Candlestick.Close)/3

    Sup_1 = (2 * PP) - Candlestick.High
    Res_1 = (2 * PP) - Candlestick.Low

    Sup_2 = PP + (Candlestick.High - Candlestick.Low)
    Res_2 = PP - (Candlestick.High - Candlestick.Low)

    Sup_3 = Candlestick.Low - 2*(Candlestick.High - PP)
    Res_3 = Candlestick.High + 2*(PP - Candlestick.Low)

    return (PP,Sup_1,Res_1,Sup_2,Res_2,Sup_3,Res_3)


def fibonacci_pivot_points(Candlestick):

    PP = (Candlestick.High + Candlestick.Low + Candlestick.Close) / 3
    S1 = PP - .382 * (Candlestick.High - Candlestick.Low)
    S2 = PP - .618 * (Candlestick.High - Candlestick.Low)
    S3 = PP - 1 * (Candlestick.High - Candlestick.Low)
    R1 = PP + .382 * (Candlestick.High - Candlestick.Low)
    R2 = PP + .618 * (Candlestick.High - Candlestick.Low)
    R3 = PP + 1 * (Candlestick.High - Candlestick.Low)

    return (PP,S1,R1,S2,R2,S3,R3)


def camarilla_pivot_points(Candlestick):
    R3 = Candlestick.Close + ( Candlestick.High - Candlestick.Low) * 1.1 / 4

    R2 = Candlestick.Close + (Candlestick.High - Candlestick.Low) * 1.1 / 6

    R1 = Candlestick.Close + (Candlestick.High - Candlestick.Low) * 1.1 / 12

    Pivot = (Candlestick.High + Candlestick.Low + Candlestick.Close) / 3

    S1 = Candlestick.Close - (Candlestick.High - Candlestick.Low) * 1.1 / 12

    S2 = Candlestick.Close - (Candlestick.High - Candlestick.Low) * 1.1 / 6

    S3 = Candlestick.Close - (Candlestick.High - Candlestick.Low) * 1.1 / 4

    return (Pivot,S1,R1,S2,R2,S3,R3)


def woodies_pivot_points(Candlestick):
    PP = (Candlestick.High + Candlestick.Low + 2 * Candlestick.Close) / 4


    S1 = ( 2 * PP ) - Candlestick.High
    S2 = PP - ( Candlestick.High - Candlestick.Low )
    S3 = Candlestick.Low - 2 * (Candlestick.High - PP)

    R1 = (2 * PP) - Candlestick.Low
    R2 = PP + (Candlestick.High - Candlestick.Low)
    R3 = Candlestick.High + 2 * (PP - Candlestick.Low)

    return (PP,S1,R1,S2,R2,S3,R3)


"""
#test

from Intraday_Trader.candlestick.candlestick_new import Candlestick

import pandas as pd
import random
import os
data_path = 'Intraday_Trader/data/minute_1/'
symbol_list = os.listdir(data_path)
symbol = random.choice(symbol_list)
symbol = symbol[0:-9]
data_60_min = pd.read_csv('Intraday_Trader/data/minute_60/'+symbol+'-60min.csv' )
data_60_min['symbol'] = symbol

data_point = data_60_min.loc[0]

candlestick = Candlestick(data_point,'60')

standard_pivots = standard_pivot_points(candlestick)
fib_pivots = fibonacci_pivot_points(candlestick)
cam_pivots = camarilla_pivot_points(candlestick)
wodd_pivots = woodies_pivot_points(candlestick)



"""

