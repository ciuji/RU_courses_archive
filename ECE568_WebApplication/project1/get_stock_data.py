from yahoofinancials2 import YahooFinancials
import pandas as pd
import requests
''' requirement
real-time data:
    contain the price, time** and volume. (time slice between two points no more than one minute)
historical data:
    time, open, high, low, close, volume.
'''
#06JRP8S4736D1FE6

'''
ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)
historical_data= yahoo_financials.get_historical_price_data('2018-01-03','2019-01-03','weekly')
print(historical_data['AAPL']['prices'])
#print(len(historical_stock_prices))
#print(type(historical_stock_prices))
'''
class get_stock_data:
    def __init__(self,ticker):
        self.ticker=ticker
        self.yahoo_financials=YahooFinancials(ticker)
        self.currentTime=0
        self.url='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ticker+'&interval=1min&apikey=06JRP8S4736D1FE6'

    def get_historical_data(self):
        raw_historical_data=self.yahoo_financials.get_historical_price_data('2018-01-03','2019-01-03','weekly')
        historical_price_data=raw_historical_data[self.ticker]['prices']
        '''timelist=[];openlist=[];highlist=[];lowlist=[];closelist=[];volumelist=[]
        for eachday in historical_price_data:
            openlist.append(eachday['open'])
            highlist.append(eachday['high'])
            closelist.append(eachday['close'])
            volumelist.append(eachday['volume'])
            lowlist.append(eachday['low'])
            timelist.append(eachday['formatted_date'])

        historical_data_df=pd.DataFrame({'time':timelist,'open':openlist,'high':highlist,'low':lowlist,'close':closelist,'volume':volumelist})
        return historical_data_df'''
        historical_data_df=pd.DataFrame.from_dict(historical_price_data)
        return historical_data_df

    def get_realtime_data(self):
        resp_json = requests.get(self.url).json()
        realtime_data_df=pd.DataFrame.from_dict(resp_json['Time Series (1min)'],orient='index')
        return realtime_data_df

test=get_stock_data('AAPL')
print(test.get_historical_data())
print(test.get_realtime_data())