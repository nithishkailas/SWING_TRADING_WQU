import numpy as np
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

symbols = ['BIOCON','KOTAKBANK','LT','LUPIN','NATIONALUM','SBIN']

features = pd.read_csv('data/strat1_BHEL_features_no_hourly.csv',index_col='Date', parse_dates=True,infer_datetime_format=True)
labeled_data = pd.read_csv('data/strat1_BHEL_meta_labeled.csv', index_col='Date',parse_dates=True,infer_datetime_format=True)

features = features.fillna(method='ffill')
features_no_nan = features.dropna()

features_final_filtered = features_no_nan[features_no_nan['label'] != 0]
labels = features_final_filtered['label']

features_final = features_final_filtered.drop('side',axis=1).drop('label',axis=1)

train_features, test_features, train_labels, test_labels = train_test_split(features_final,labels, test_size=0.25, random_state=41), shuffle=False)

for symbol in symbols:

	print(len(train_features))
	print(len(test_features))

	features = pd.read_csv('data/strat1_' + symbol + '_features_no_hourly.csv',index_col='Date', parse_dates=True,infer_datetime_format=True)
	labeled_data = pd.read_csv('data/strat1_'+ symbol +'_meta_labeled.csv', index_col='Date',parse_dates=True,infer_datetime_format=True)

	features = features.fillna(method='ffill')
	features_no_nan = features.dropna()

	features_final_filtered = features_no_nan[features_no_nan['label'] != 0]
	labels = features_final_filtered['label']

	features_final = features_final_filtered.drop('side',axis=1).drop('label',axis=1)

	train_feats, test_feats, train_lbls, test_lbls = train_test_split(features_final,labels, test_size=0.25, random_state=41), shuffle=False)
	
	train_features = train_features.append(train_feats)
	train_labels = train_labels.append(train_lbls)
	test_features = test_features.append(test_feats)
	test_labels = test_labels.append(test_lbls)
	
print(len(train_features))
print(len(test_features))

model = RandomForestClassifier(n_estimators=100, bootstrap=True, max_features='sqrt')

model.fit(train_features, train_labels)
model_predictions = model.predict(test_features)
model_probs = model.predict_proba(test_features)[:,1]

cm = confusion_matrix(test_labels,model_predictions)
print(cm)

cr = classification_report(test_labels,model_predictions,labels=[-1,1])
print(cr)

pickle.dump(model,open('randomforestmodel_strat1.sav','wb'))


