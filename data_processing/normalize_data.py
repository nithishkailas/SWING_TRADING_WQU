

def normalize_data(data,data_point):
    n_data = pd.DataFrame()
    n_data['Date'] = data.Date

    n_data['Open'] = (data['Open'] - data.loc[data_point]['Close'])/data.loc[data_point]['Close'] *100
    n_data['High'] = (data['High'] - data.loc[data_point]['Close'])/data.loc[data_point]['Close'] *100
    n_data['Low'] = (data['Low'] - data.loc[data_point]['Close'])/data.loc[data_point]['Close'] *100
    n_data['Close'] = (data['Close'] - data.loc[data_point]['Close'])/data.loc[data_point]['Close'] *100
    n_data.index = n_data.Date
    #Minmax Scaler for volume

    sc = MinMaxScaler(feature_range=(0,1))
    n_data['Volume'] = sc.fit_transform(np.array(data['Volume'].astype(float)).reshape(-1,1))

    return n_data


######################################
#test
data = pd.read_csv("Intraday_Trader/data/minute_1/SBIN-1min.csv")
data.index = data.Date



n_data = normalize_data(data,data.Date[10])

#test for pattern shape retention
import matplotlib.pyplot as plt
plt.style.use('seaborn')
#import seaborn as sns
#sns.set()
from mpl_finance import candlestick2_ohlc

data = Featured_Dataframe
n_data =Normalized_Dataframe



length = len(data.values)
x1 = np.linspace(0,length,length)
x2 = np.linspace(0,length,length)

y1_1 = data['M5_Open']
y1_2 = data['M5_High']
y1_3 = data['M5_Low']
y1_4 = data['M5_Close']
y1_5 = data['M5_BBU_14_2']
y1_6 = data['M5_MA_14']
y1_7 = data['M5_BBL_14_2']



y2_1 = n_data['M5_Open']
y2_2 = n_data['M5_High']
y2_3 = n_data['M5_Low']
y2_4 = n_data['M5_Close']
y2_5 = n_data['M5_BBU_14_2']
y2_6 = n_data['M5_MA_14']
y2_7 = n_data['M5_BBL_14_2']

ax1 = plt.subplot(1, 2, 1)
plt.title("Original data")
candlestick2_ohlc(ax1,y1_1,y1_2,y1_3,y1_4, width= .5, colorup='green', colordown='red')
ax1.plot(y1_5)
ax1.plot(y1_6)
ax1.plot(y1_7)

plt.ylabel("OHLC+MA14+BB14_2STDV")

ax2 = plt.subplot(1, 2, 2)
plt.title("Normalised data ")
candlestick2_ohlc(ax2,y2_1,y2_2,y2_3,y2_4, width= .5, colorup='green', colordown='red')
ax2.plot(y2_5)
ax2.plot(y2_6)
ax2.plot(y2_7)



plt.show()

print(plt.style.available)

import  seaborn as sns

sns.kdeplot(data['Open'])