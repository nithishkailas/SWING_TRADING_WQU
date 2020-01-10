## SWING_TRADING_WQU
## World Quant University Capstone Project - Swing Trading  

Title :
### Technical analysis of stock charts and Machine Learning infrastructure for Algorithmic Swing Trading 

This project aims to find a systematic way to approach the work of creating a short / intermediate term trading strategy that has holding time spanning anywhere from 5 minutes to 1 week, by researching a step by step process of generating and improving Entry, Stop Loss, Target and Maximum Holding Period Signals. This is done by using Technical analysis of Stock Charts and also including machine learning models. In this project we will test the general and popular ideas and create simple strategies that are appropriate for market conditions (i.e. trending vs. range-bound) and evaluate them from a profitability and risk perspective and also investigate the potential of machine learning to create and improve trading strategies. Ml will be used to identify hidden patterns which can generate profitable trades. Furthermore, in order to make the work systematic and efficient, we are trying to wrap our work into a general infrastructure which will standardize the Trade management and help in making the result analysis easier. The infrastructure will include a back-tester which can be used to test the strategies in a systematic manner. 
 
 The project is broadly divided into three parts. 
 #### 1. Technical analysis and feature matrix creation
 #### 2. Creating strategy back-testing infrastructure
 #### 3. Improving strategies using machine learning


### Technical analysis and feature matrix creation

This Project requires OHLCV time series data sampled at 1-minute frequency to get enough patterns for analysis. This project uses 1 minute samples of *DOHLCV data of 150 stocks traded in National Stock Exchange in India (NSE) and also the index Nifty50 from 28-11-2018 to 29-03-2019 as the train data. For higher sampling requirements this project uses the last 5 years End-Of-Day data of the above stocks and index for the train data. It uses the *DOHLCV 1-minute and daily data of same instruments spanning from 01-10-2019 to 11-11-2019 as the test data. 
 
The raw data is presented in CSV format as follows: Date, Open, High, Low, Close, and Volume. (*DOHLCV*) 

##### run dataprocessing/get_feature_matrix.py 

This will restructure the raw data into 1minute, 5minute, 15minute, 30minute, 60minute, daily, weekly and Monthly samples and add a detailed set of technical indicators to each timeframe. Then the data is normalized using differnt methods and a List of dataframe is returned corresponding to each 1-minute interval which is abuntant to create strategies and also structured to be inputted to machine learning algorithms.

### Creating strategy back-testing infrastructure

To systematically test the strategies researched and also the ones which are coded as part of this project, this part of the project plan to create a simple yet powerful infrastructure where strategies can be structured with ease and also back-tested on historical and synthetic data. It will take into account Commissions generated as a part of trading so that accurate net profitability of the strategies can be calculated. The infrastructure will generate various statistics for the strategy like hit rate, mean holding period and much more so that the trades in the strategies can be analyzed with respect to a bunch of valuable information and also the strategy as a whole can be evaluated. Any good trading research needs to have its own infrastructure for efficient testing. This project does research on the top of its own custom infrastructure which gives greater flexibility and also provide data selectivity. 

The infrastructure consists of 2 classes.
##### Portfolio class @ portfolio/portfolio.py
##### Order Class @ order.order.py

See this link for an example usage of these two classes: 
 
##### examples/portfolio_and_order_usage_example.py
 
 
