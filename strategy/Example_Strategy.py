from SWING_TRADING_WQU.portfolio.portfolio import Portfolio
from SWING_TRADING_WQU.order.order import Order
from SWING_TRADING_WQU.strategy.base_strategy import Strategy
from SWING_TRADING_WQU.data_processing.get_data_with_features import get_featured_matrix
import numpy as np
import pandas as pd
import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
pd.set_option('mode.chained_assignment', None)

class Example_Strategy(Strategy):

    def create_features(self,data_all):
        Full_Featured_Matrix = []
        for i in range(len(data_all[0])):
            print(i, "/", len(data_all[0]))
            INSIDE_MATRIX = []
            datapoint = data_all[0].index[i]
            INSIDE_MATRIX.append(datapoint)
            Feat_mat_list, Feat_mat_2 = get_featured_matrix(data_all, datapoint)
            INSIDE_MATRIX.append(Feat_mat_2)
            Full_Featured_Matrix.append(INSIDE_MATRIX)

        self.Feature_Matrix = Full_Featured_Matrix

    def create_labels(self):
        """
        This Strategy Exits at profit of 2ATR in 5min, at loss at -1ATR in 5min or max of 2 hrs

        :param :
        :return:
        """
        Labels = []
        for i in range(len(self.Feature_Matrix)):

            data_point = self.Feature_Matrix[i][0]
            data = self.Feature_Matrix[i][1]
            current_close = data[0].Close[0]
            ATR_5min_20 = data[1]['ATR_20'][0]
            long_target = current_close + ATR_5min_20*3
            long_stop = current_close - ATR_5min_20
            short_target = current_close-3*ATR_5min_20
            short_stop = current_close+ATR_5min_20

            end_time = min(data_point+datetime.timedelta(hours = 2),data_point.replace(hour = 15,minute =15))
            mask = data.loc[data_point:end_time]
            #check _long
            hit = 0
            for mask_i in range(len(mask)):
                inst = mask[mask_i]
                if inst['High'] >= long_target:
                    Labels.append(1)
                    hit = 1
                    break
                elif inst['Low'] <= long_stop:
                    Labels.append(0)
                    hit =1
                    break

            if hit == 0:
                Labels.append(0)

            # check_short
            hit = 0
            for mask_i in range(len(mask)):
                inst = mask[mask_i]
                if inst['Low'] <= short_target:
                    Labels.append(-1)
                    hit = 1
                    break
                elif inst['High'] >= short_stop:
                    Labels.append(0)
                    hit = 1
                    break

            if hit == 0:
                Labels.append(0)

        self.Labels = Labels

    def test_train_split(self):
        self.train_features, self.test_features, self.train_labels, self.test_labels = train_test_split(
            self.Feature_Matrix, self.Labels, test_size=0.25, random_state=41)

    def feature_scaler(self):
        sc = MinMaxScaler(feature_range=(0,1))

        self.scaled_train_features = sc.fit_transform(self.train_features)
        self.scaled_train_labels = sc.transform(self.train_labels)
        self.scaler = sc

    def create_model(self):

        model = RandomForestClassifier(n_estimators=100, bootstrap=True, max_features='sqrt')
        self.model = model

    def train(self):
        self.model.fit(self.scaled_train_features, self.scaled_train_labels)

    def backtest(self):
        model_predictions = self.model.predict(self.scaled_test_features)
        model_probs = self.model.predict_proba(self.scaled_test_features)[:, 1]
        Predictions =  list(map(lambda x, y:(x,y), model_predictions, model_probs))
        self.Predictions = self.scaler.inverse_transform(Predictions)

        for i in range(len(test_features)):
            data_index = test_features[i][0]
            data = test_features[i][1]
            new_datapoint = data[0][0]

            ATR = data[1]['ATR_20'][0]
            if self.Predictions[i] == 1:
                print("Long Signal")
                Long_Entry_price = new_datapoint.Close
                Long_Target = Long_Entry_price + 3 * ATR
                Long_Stop = Long_Entry_price - ATR
                Long_Entry_time = new_datapoint.Date
                Long_Holding_period = min(new_datapoint.Date+datetime.timedelta(hours = 2),new_datapoint.Date.replace(hour = 15,minute =15))
                Long_Order = Order(self.Portfolio,new_datapoint['symbol'],'Long',Long_Entry_time,Long_Entry_price,
                                   Long_Target,Long_Stop,10,Long_Holding_period,10)

                if Long_Order.margin_required < self.Portfolio.FreeCapital:
                    self.Portfolio.add(Long_Order)
                    print("Long Order Placed @ ", Long_Entry_time," -Entry Price: ",Long_Entry_price)
            elif self.Predictions[i] == -1:
                print("Short Signal")
                Short_Entry_price = new_datapoint.Close
                Short_Target = Short_Entry_price - 3 * ATR
                Short_Stop = Short_Entry_price + ATR
                Short_Entry_time = new_datapoint.Date
                Short_Holding_period = min(new_datapoint.Date + datetime.timedelta(hours=2),
                                          new_datapoint.Date.replace(hour=15, minute=15))
                Short_Order = Order(self.Portfolio, new_datapoint['symbol'], 'Short', Short_Entry_time, Short_Entry_price,
                                   Short_Target, Short_Stop, 10, Short_Holding_period, 10)

                if Short_Order.margin_required < self.Portfolio.FreeCapital:
                    self.Portfolio.add(Short_Order)
                    print("Short Order Placed @ ", Short_Entry_time, " -Entry Price: ", Short_Entry_price)

            #Call Portfolio.tracker to update the portfolio variables for the current datapoint
            self.Portfolio.tracker(new_datapoint)

    def generate_results(self):
        self.Portfolio.get_portfolio_stats()

    def run(self,data_all):
        self.create_features(data_all=data_all)
        self.create_labels()
        self.test_train_split()
        self.feature_scaler()
        self.create_model()
        self.train()
        self.backtest()
        self.generate_results()



Ex_Port = Portfolio("Example_strategy_1",datetime.datetime.today(),10000)
Ex_Strategy_1 = Example_Strategy('Example_Strategy',Ex_Port)
from SWING_TRADING_WQU.data_processing.data_preprocessing import get_higher_timeframe,read_train_data
path = "Intraday_Trader/rawdata/rawdata_set1/"
symbol ='SBIN'
data_one,data_daily = read_train_data(path,symbol)

data_one = data_one[1000:1100]
data_daily = data_daily


data_all = get_higher_timeframe(data_one,data_daily)

Ex_Strategy_1.run(data_all=data_all)







