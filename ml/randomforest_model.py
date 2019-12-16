import numpy as np
import pandas as pd

from sklearn.enseble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

features = pd.read_csv('data/SBIN_features_no_hourly.csv',index_col='Date', parse_dates=True,infer_datetime_format=True)
labeled_data = pd.read_csv('data/SBIN_labeled.csv', index_col='Date',parse_dates=True,infer_datetime_format=True)

features = features.fillna(method='ffill')
features_no_nan = features.dropna()
labels = features_no_nan['label']
features_final = features_no_nan.drop('label',axis=1)

train_features, test_features, train_labels, test_labels = train_test_split(features_final,labels, test_size=0.25, random_state=41)

model = RandomForestClassifier(n_estimators=100, bootstrap=True, max_features='sqrt')

model.fit(train_features, train_labels)
model_predictions = model.predict(test_features)
model_probs = model.predict_proba(test_features)[:,1]

cm = confusion_matrix(test_labels,model_predictions)
print(cm)

cr = classification_report(test_labels,model_predictions,labels=[-1,0,1])

print(cr)
