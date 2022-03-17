# from __future__ import print_function
from alpha_vantage.timeseries import TimeSeries


key = 'RP6TUYQ1XGR8KOB2'
ts =TimeSeries(key=key,output_format='pandas')
interval = '60min'

def get_data(tick):
    data, meta_data = ts.get_intraday(tick,interval)
    data.reset_index(inplace=True)
    data.rename(columns={'date':'historical_price_date_time','1. open':"day_open_price", '2. high':"day_high_price", '3. low':"day_low_price", '4. close':"day_close_price", '5. volume':"day_volume"},inplace =True)
    return(data.head(1))    

# ,'msft','aapl'
# tickers=['aa']cls