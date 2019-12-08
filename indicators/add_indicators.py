from SWING_TRADING_WQU.indicators.pivot_points_calculator import standard_pivot_points,fibonacci_pivot_points
import talib

def add_pivots(data_list):
    # 1.Adding monthly pivots to weekly data
    data_weekly = data_list[6]
    data_monthly = data_list[7]
    data_15min = data_list[2]
    data_daily = data_list[5]
    data_60min = data_list[4]
    data_1min = data_list[0]
    data_5min = data_list[1]
    data_30min = data_list[3]

    monthly_standard_pivots = []
    monthly_fib_pivots = []

    for i in range(len(data_weekly)):

        this_month_data = data_monthly[data_monthly.index.month == data_weekly.index[i].month]
        try:
            previous_month_data = data_monthly.loc[data_monthly[:this_month_data.index[-1]][:-1].index[-1]]

            stnd_pivots = standard_pivot_points(previous_month_data)
            fib_pivots = fibonacci_pivot_points(previous_month_data)
            monthly_standard_pivots.append(stnd_pivots)
            monthly_fib_pivots.append(fib_pivots)
        except:
            monthly_standard_pivots.append(0)
            monthly_fib_pivots.append(0)

    data_weekly['monthly_pivots_Standard'] = monthly_standard_pivots
    data_weekly['monthly_pivots_fibonacci'] = monthly_fib_pivots

    # 2.Adding weekly pivots to 60min data

    weekly_standard_pivots = []
    weekly_fib_pivots = []

    for i in range(len(data_60min)):

        this_week_data = data_weekly.loc[data_weekly[data_weekly.index < data_60min.index[i]].index[-1]]
        try:
            previous_week_data = data_weekly.loc[data_weekly[:this_week_data.name][:-1].index[-1]]

            stnd_pivots = standard_pivot_points(previous_week_data)
            fib_pivots = fibonacci_pivot_points(previous_week_data)
            weekly_standard_pivots.append(stnd_pivots)
            weekly_fib_pivots.append(fib_pivots)
        except:
            weekly_standard_pivots.append(0)
            weekly_fib_pivots.append(0)

    data_60min['weekly_pivots_Standard'] = weekly_standard_pivots
    data_60min['weekly_pivots_fibonacci'] = weekly_fib_pivots

    # 3.Adding daily pivots to 15min data

    daily_standard_pivots = []
    daily_fib_pivots = []

    for i in range(len(data_15min)):

        this_day_data = data_daily.loc[data_daily[data_daily.index < data_15min.index[i]].index[-1]]
        try:
            previous_day_data = data_daily.loc[data_daily[:this_day_data.name][:-1].index[-1]]

            stnd_pivots = standard_pivot_points(previous_day_data)
            fib_pivots = fibonacci_pivot_points(previous_day_data)
            daily_standard_pivots.append(stnd_pivots)
            daily_fib_pivots.append(fib_pivots)
        except:
            daily_standard_pivots.append(0)
            daily_fib_pivots.append(0)

    data_15min['daily_pivots_Standard'] = daily_standard_pivots
    data_15min['daily_pivots_fibonacci'] = daily_fib_pivots
    return [data_1min, data_5min, data_15min, data_30min, data_60min, data_daily, data_weekly, data_monthly]






def add_overlap_studies(data_list):



    #(overlap study) Indicators common for all Time-frames
    for data in data_list:
        # 1) 14 period 2 std Bollinger Bands
        upperband, middleband, lowerband = talib.BBANDS(data.Close, timeperiod=14, nbdevup=2, nbdevdn=2, matype=0)
        data['BBU_14_2'] = upperband
        data['BBL_14_2'] = lowerband

        # 2) 14 period 3 std  and 20 period 2 std Bollinger Bands
        upperband, middleband, lowerband = talib.BBANDS(data.Close, timeperiod=14, nbdevup=3, nbdevdn=3, matype=0)
        data['BBU_14_3'] = upperband
        data['BBL_14_3'] = lowerband

        upperband, middleband, lowerband = talib.BBANDS(data.Close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
        data['BBU_20_2'] = upperband
        data['BBL_20_2'] = lowerband

        # 3) DEMA - Double Exponential Moving Average of period 20
        real = talib.DEMA(data.Close, timeperiod=20)
        data['DEMA_20'] = real

        # 4) EMA - Exponential Moving Average 20
        real = talib.EMA(data.Close, timeperiod=20)
        data['EMA_20'] = real

        # 5) HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
        real = talib.HT_TRENDLINE(data.Close)
        data['HT_T'] = real

        # 6) KAMA - Kaufman Adaptive Moving Average Period 20
        real = talib.KAMA(data.Close, timeperiod=20)
        data['KAMA_20'] = real

        # 7) MA - Moving average periods 5,8,14,20
        real = talib.MA(data.Close, timeperiod=5, matype=0)
        data['MA_5'] = real
        real = talib.MA(data.Close, timeperiod=8, matype=0)
        data['MA_8'] = real
        real = talib.MA(data.Close, timeperiod=14, matype=0)
        data['MA_14'] = real
        real = talib.MA(data.Close, timeperiod=20, matype=0)
        data['MA_20'] = real

        # 8) MIDPOINT - MidPoint over period
        real = talib.MIDPOINT(data.Close, timeperiod=14)
        data['MP_14'] = real

        # 9) MIDPRICE - Midpoint Price over period
        real = talib.MIDPRICE(data.High, data.Low, timeperiod=14)
        data['MPP_14'] = real

        # 10) SAR - Parabolic SAR
        real = talib.SAR(data.High, data.Low, acceleration=0, maximum=0)
        data['SAR'] = real

        # 11) TEMA - Triple Exponential Moving Average
        real = talib.TEMA(data.Close, timeperiod=20)
        data['TEMA_20'] = real

        # 12) TRIMA - Triangular Moving Average
        real = talib.TRIMA(data.Close, timeperiod=20)
        data['TRIMA_20'] = real

        # 13) WMA - Weighted Moving Average
        real = talib.WMA(data.Close, timeperiod=20)
        data['WMA_20'] = real

    data_weekly = data_list[6]
    data_monthly = data_list[7]
    data_15min = data_list[2]
    data_daily = data_list[5]
    data_60min = data_list[4]
    data_1min = data_list[0]
    data_5min = data_list[1]
    data_30min = data_list[3]

    #Create (overlap study) indicators for a only to a particular timeframe here..




    return data_list


def add_momentum_indicators(data_list):
    # (momentum) Indicators common for all Time-frames
    for data in data_list:
        # 1) ADX - Average Directional Movement Index
        real = talib.ADX(data.High, data.Low, data.Close, timeperiod=14)
        data['ADX_14'] = real

        # 2) ADXR - Average Directional Movement Index Rating
        real = talib.ADXR(data.High, data.Low, data.Close, timeperiod=14)
        data['ADXR_14'] = real

        # 3) APO - Absolute Price Oscillator
        real = talib.APO(data.Close, fastperiod=12, slowperiod=26, matype=0)
        data['APO'] = real

        # 4) AROON - Aroon
        aroondown, aroonup = talib.AROON(data.High, data.Low, timeperiod=14)
        data['Aroon_down_14'] = aroondown
        data['Aroon_up_14'] = aroonup

        # 5) AROONOSC - Aroon Oscillator
        real = talib.AROONOSC(data.High, data.Low, timeperiod=14)
        data['AROONOSC_14'] = real

        # 6) BOP - Balance Of Power
        real = talib.BOP(data.Open, data.High, data.Low, data.Close)
        data['BOP'] = real

        # 7) CCI - Commodity Channel Index
        real = talib.CCI(data.High, data.Low, data.Close, timeperiod=14)
        data['CCI_14'] = real

        # 8) CMO - Chande Momentum Oscillator
        real = talib.CMO(data.Close, timeperiod=14)
        data['CMO_14'] = real

        # 9) DX - Directional Movement Index
        real = talib.DX(data.High, data.Low, data.Close, timeperiod=14)
        data['DMI_14'] = real

        # 10) MACD - Moving Average Convergence/Divergence
        macd, macdsignal, macdhist = talib.MACD(data.Close, fastperiod=12, slowperiod=26, signalperiod=9)
        data['macd'] = macd
        data['macd_sig'] = macdsignal
        data['macd_hist'] = macdhist

        # 11) MFI - Money Flow Index
        real = talib.MFI(data.High, data.Low, data.Close, data.Volume, timeperiod=14)
        data['MFT_14'] = real

        # 12) MINUS_DI - Minus Directional Indicator
        real = talib.MINUS_DI(data.High, data.Low, data.Close, timeperiod=14)
        data['MINUS_DI_14'] = real

        # 13) MINUS_DM - Minus Directional Movement
        real = talib.MINUS_DM(data.High, data.Low, timeperiod=14)
        data['MINUS_DM_14'] = real

        # 14) MOM - Momentum
        real = talib.MOM(data.Close, timeperiod=14)
        data['MOM_14'] = real

        # 15) PLUS_DI - Plus Directional Indicator
        real = talib.PLUS_DI(data.High, data.Low, data.Close, timeperiod=14)
        data['PLUS_DI_14'] = real

        # 16) PLUS_DM - Plus Directional Movement
        real = talib.PLUS_DM(data.High, data.Low, timeperiod=14)
        data['PLUS_DM_14'] = real

        # 17) PPO - Percentage Price Oscillator
        real = talib.PPO(data.Close, fastperiod=12, slowperiod=26, matype=0)
        data['PPO'] = real

        # 18) ROC - Rate of change : ((price/prevPrice)-1)*100
        real = talib.ROC(data.Close, timeperiod=14)
        data['ROC_14'] = real

        # 19) RSI - Relative Strength Index
        real = talib.RSI(data.Close, timeperiod=14)
        data['RSI_14'] = real

        # 20) STOCH - Stochastic
        slowk, slowd = talib.STOCH(data.High, data.Low, data.Close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        data['slowk'] = slowk
        data['slowd'] = slowd

        # 21) STOCHF - Stochastic Fast
        fastk, fastd = talib.STOCHF(data.High, data.Low, data.Close, fastk_period=5, fastd_period=3, fastd_matype=0)
        data['fastk'] = fastk
        data['fastd'] = fastd

        # 22) TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        real = talib.TRIX(data.Close, timeperiod=20)
        data['TRIX_20'] = real

        # 23) ULTOSC - Ultimate Oscillator
        real = talib.ULTOSC(data.High, data.Low, data.Close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
        data['ULTOSC'] = real

        # 24) WILLR - Williams' %R
        real = talib.WILLR(data.High, data.Low, data.Close, timeperiod=14)
        data['WILLR_14'] = real

    data_weekly = data_list[6]
    data_monthly = data_list[7]
    data_15min = data_list[2]
    data_daily = data_list[5]
    data_60min = data_list[4]
    data_1min = data_list[0]
    data_5min = data_list[1]
    data_30min = data_list[3]

    # Create (momentum) indicators for a only to a particular timeframe here..

    return data_list



def add_volume_indicators(data_list):
    # (volume) Indicators common for all Time-frames
    for data in data_list:

        # 1) AD - Chaikin A / D Line
        real = talib.AD(data.High, data.Low, data.Close, data.Volume)
        data['AD'] = real

        # 2) ADOSC - Chaikin A/D Oscillator
        real = talib.ADOSC(data.High, data.Low, data.Close, data.Volume, fastperiod=3, slowperiod=10)
        data['ADOSC'] = real

        # 3) OBV - On Balance Volume
        real = talib.OBV(data.Close, data.Volume)
        data['OBV'] = real

    data_weekly = data_list[6]
    data_monthly = data_list[7]
    data_15min = data_list[2]
    data_daily = data_list[5]
    data_60min = data_list[4]
    data_1min = data_list[0]
    data_5min = data_list[1]
    data_30min = data_list[3]

    # Create (volume) indicators for a only to a particular timeframe here..

    return data_list

def add_volatility_indicators(data_list):
    # (volatility) Indicators common for all Time-frames
    for data in data_list:

        # 1) ATR - Average True Range
        real = talib.ATR(data.High, data.Low, data.Close, timeperiod=14)
        data['ATR_14'] = real

        # 2) NATR - Normalized Average True Range
        real = talib.NATR(data.High, data.Low, data.Close, timeperiod=14)
        data['NATR_14'] = real

        # 3) TRANGE - True Range
        real = talib.TRANGE(data.High, data.Low, data.Close)
        data['TRANGE'] = real

    data_weekly = data_list[6]
    data_monthly = data_list[7]
    data_15min = data_list[2]
    data_daily = data_list[5]
    data_60min = data_list[4]
    data_1min = data_list[0]
    data_5min = data_list[1]
    data_30min = data_list[3]

    # Create (volatility) indicators for a only to a particular timeframe here..

    return data_list


def add_price_transform_indicators(data_list):
    for data in data_list:
        # 1) AVGPRICE - Average Price
        real = talib.AVGPRICE(data.Open, data.High, data.Low, data.Close)
        data['AVERAGE'] = real

        # 2) MEDPRICE - Median Price
        real = talib.MEDPRICE(data.High, data.Low)
        data['MEDPRICE'] = real

        # 3) TYPPRICE - Typical Price
        real = talib.TYPPRICE(data.High, data.Low, data.Close)
        data['TYPPRICE'] = real

        # 4) WCLPRICE - Weighted Close Price
        real = talib.WCLPRICE(data.High, data.Low, data.Close)
        data['WCLPRICE'] = real

    return data_list


def add_cycle_indicators(data_list):
    for data in data_list:
        #HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period
        real = talib.HT_DCPERIOD(data.Close)
        data['HT_DCPERIOD'] = real

        #HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase
        real = talib.HT_DCPHASE(data.Close)
        data['HT_DCPHASE'] = real

        #HT_PHASOR - Hilbert Transform - Phasor Components
        inphase, quadrature = talib.HT_PHASOR(data.Close)
        data['HT_PHASOR_inphase'] = inphase
        data['HT_PHASOR_quadrature'] = quadrature

        #HT_SINE - Hilbert Transform - SineWave
        sine, leadsine = talib.HT_SINE(data.Close)
        data['HT_SINE_sine'] = sine
        data['HT_SINE_leadsine'] = leadsine

        #HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode
        integer = talib.HT_TRENDMODE(data.Close)
        data['HT_TRENDMODE'] = integer

    return data_list

