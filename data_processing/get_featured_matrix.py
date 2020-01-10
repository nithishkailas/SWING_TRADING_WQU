import os
import pandas as pd
pd.set_option('chained_assignment', None)


from SWING_TRADING_WQU.data_processing.data_preprocessing import read_train_data, get_higher_timeframe

from SWING_TRADING_WQU.indicators.add_indicators import add_overlap_studies, add_momentum_indicators, \
    add_volume_indicators, add_volatility_indicators, add_pivots, add_price_transform_indicators, add_cycle_indicators, \
    add_CDLpatterns, add_math_transform_funcs, add_statistic_funtions


path = "Intraday_Trader/rawdata/rawdata_set1/"

symbol_list = os.listdir(path)
symbol_list_new = []
for i in range(len(symbol_list)):
    if i % 2 == 0:
        symbol_list_new.append(symbol_list[i][:-7])

symbol = symbol_list_new[0]

data_minute, data_daily = read_train_data(path, symbol)

data_all = get_higher_timeframe(data_minute, data_daily)


prefix_list = ['M1_', 'M5_', 'M15_', 'M30_', 'M60_', 'D_', 'W_', 'M_']


def create_featured_matrix(data_all):
    Featured_Dataframe_dict = {}

    for i in range(1500, len(data_all[0])):
        Featured_Dataframe = pd.DataFrame()
        print(i, "/", len(data_all[0]))
        new_df_list = []
        index = data_all[0].index[i]
        for data in data_all:
            higher_mask = data.loc[data.index <= index]

            lower_mask = data_all[0].loc[higher_mask.index[-1]:index]

            higher_mask.loc[higher_mask.index[-1], 'Close'] = lower_mask.loc[lower_mask.index[-1], 'Close']

            higher_mask.loc[higher_mask.index[-1], 'High'] = max(lower_mask.High)
            higher_mask.loc[higher_mask.index[-1], 'Low'] = min(lower_mask.Low)
            higher_mask.loc[higher_mask.index[-1], 'Volume'] = sum(lower_mask.Volume)

            new_df = higher_mask.copy(deep=True)

            new_df_list.append(new_df)

        new_df_list = add_pivots(new_df_list)
        new_df_list = add_overlap_studies(new_df_list)
        new_df_list = add_momentum_indicators(new_df_list)
        new_df_list = add_volume_indicators(new_df_list)
        new_df_list = add_volatility_indicators(new_df_list)
        new_df_list = add_cycle_indicators(new_df_list)
        new_df_list = add_price_transform_indicators(new_df_list)
        new_df_list = add_CDLpatterns(new_df_list)
        new_df_list = add_math_transform_funcs(new_df_list)
        new_df_list = add_statistic_funtions(new_df_list)

        for i in range(len(new_df_list)):
            df = new_df_list[i][-25:]
            for column_name in df.columns:
                Featured_Dataframe[prefix_list[i] + column_name] = df[column_name].values

        Featured_Dataframe_dict[index] = Featured_Dataframe

    return Featured_Dataframe_dict


Featured_list = create_featured_matrix(data_all)