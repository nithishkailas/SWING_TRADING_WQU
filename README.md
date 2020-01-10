## SWING_TRADING_WQU
## World Quant University Capstone Project - Swing Trading  

Title :
### Technical analysis of stock charts and Machine Learning infrastructure for Algorithmic Swing Trading 

This project aims to find a systematic way to approach the work of creating a short / intermediate term trading strategy that has holding time spanning anywhere from 5 minutes to 1 week, by researching a step by step process of generating and improving Entry, Stop Loss, Target and Maximum Holding Period Signals. This is done by using Technical analysis of Stock Charts and also including machine learning models. In this project we will test the general and popular ideas and create simple strategies that are appropriate for market conditions (i.e. trending vs. range-bound) and evaluate them from a profitability and risk perspective and also investigate the potential of machine learning to create and improve trading strategies. Ml will be used to identify hidden patterns which can generate profitable trades. Furthermore, in order to make the work systematic and efficient, we are trying to wrap our work into a general infrastructure which will standardize the Trade management and help in making the result analysis easier. The infrastructure will include a back-tester which can be used to test the strategies in a systematic manner. 
 
 The project is broadly divided into three parts. 
 #### 1. Technical analysis and feature matrix creation
 #### 2. Creating back-testing infrastructure
 #### 3. Improving strategies using machine learning

### Technical analysis and feature matrix creation

This Project requires OHLCV time series data sampled at 1-minute frequency to get enough patterns for analysis. This project uses 1 minute samples of *DOHLCV data of 150 stocks traded in National Stock Exchange in India (NSE) and also the index Nifty50 from 28-11-2018 to 29-03-2019 as the train data. For higher sampling requirements this project uses the last 5 years End-Of-Day data of the above stocks and index for the train data. It uses the *DOHLCV 1-minute and daily data of same instruments spanning from 01-10-2019 to 11-11-2019 as the test data. 
 
The raw data is presented in CSV format as follows: Date, Open, High, Low, Close, and Volume. (*DOHLCV*) 

