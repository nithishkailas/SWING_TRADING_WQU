
from SWING_TRADING_WQU.strategy.base_strategy import Strategy
import pandas as pd

class EMA_Crossover_strategy(Strategy):
    """
    This strategy Enter long if
    5 minute 8MA  crosses over 5 minute 20 MA
    if 60 hr 8 MA is above 60 minute 20 MA.

    This strategy Enter short if
    5 minute 8MA  crosses below 5 minute 20 MA
    if 60 hr 8 MA is below 60 minute 20 MA.
    """


    def create_features(self):


        self.data_1min = pd.read_csv('SWING_TRADING_WQU/examples/sample_data/data_w_indicators_nan_included/SBIN_feat_mat_two_1min.csv')
        self.data_5min = pd.read_csv('SWING_TRADING_WQU/examples/sample_data/data_w_indicators_nan_included/SBIN_feat_mat_two_5min.csv')
        self.data_60min = pd.read_csv('SWING_TRADING_WQU/examples/sample_data/data_w_indicators_nan_included/SBIN_feat_mat_two_60min.csv')


    def strategy_logic(self,index):

        if data[index]['M60_EMA_8'] > data_point[index]['M60_EMA_20']:
            if (data[index-1]['M5_EMA_8'] <= data[index-1]['M5_EMA_20'] and
                data[index]['M5_EMA_8'] > data[index]['M5_EMA_20']):
                #Long Signal.
                signal = {'direction':'Long',
                                       'entry_time' : data[index].Date,
                                       'entry_price' : data[index].Close}


        elif data[index]['M60_EMA_8'] < data_point[index]['M60_EMA_20']:
            if (data[index-1]['M5_EMA_8'] >= data[index-1]['M5_EMA_20'] and
                data[index]['M5_EMA_8'] < data[index]['M5_EMA_20']):
                #Long Signal.
                signal = {'direction':'Short',
                                       'entry_time' : data[index].Date,
                                       'entry_price' : data[index].Close}

        else:
            signal = 0

        return signal


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

features = pd.read_csv('SBIN_no_hourly.csv', index_col='Date', parse_dates=True,
                       infer_datetime_format=True)
labeled_data = pd.read_csv('SBIN_labelled.csv', index_col='Date', parse_dates=True,
                           infer_datetime_format=True)

features = features.fillna(method='ffill')
features_no_nan = features.dropna()
labels = features_no_nan['label']
features_final = features_no_nan.drop('label', axis=1)

train_features, test_features, train_labels, test_labels = train_test_split(features_final, labels,
                                                                            test_size=0.25, random_state=41)

model = RandomForestClassifier(n_estimators=100, bootstrap=True, max_features='sqrt')

model.fit(train_features, train_labels)
model_predictions = model.predict(test_features)
model_probs = model.predict_proba(test_features)[:, 1]

cm = confusion_matrix(test_labels, model_predictions)
print(cm)

cr = classification_report(test_labels, model_predictions, labels=[-1, 0, 1])

print(cr)


len(model_predictions)
len(model_probs)


len(labeled_data)

test_features.columns
labeled_data.columns.values

len(labeled_data)*0.25


data =
