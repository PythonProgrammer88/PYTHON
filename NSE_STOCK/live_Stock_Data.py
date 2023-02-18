import os
os.system('pip install nsepy')
os.system('pip install nsetools')

import pandas as pd

from nsepy.live import get_holidays_list
from datetime import date, timedelta

from nsetools import Nse
import nsepy as NSE

nse = Nse()

all_stock_codes = nse.get_stock_codes()
symbols = all_stock_codes.keys()
series = "EQ"
for data_symbol in symbols:
    tradingSymbol = data_symbol
    series = "EQ"
    quote = NSE.live.get_quote(symbol=tradingSymbol)
    stock_data = quote["data"]
    #print(pd.DataFrame(quote["data"]).T)
    if(len(stock_data) == 0):
      continue
    Close_Price = stock_data[0]["closePrice"]
    Last_Price = stock_data[0]["lastPrice"]
    print('symbol: {}, LastPrice: {}, ClosePrice: {}'.format(tradingSymbol, Last_Price, Close_Price))