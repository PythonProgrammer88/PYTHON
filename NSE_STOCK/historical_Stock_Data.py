import os
os.system('pip install nsepy')
os.system('pip install nsetools')

import pandas as pd

from nsepy import get_history as gh
import dateutil.relativedelta as dr

import math

from nsepy.live import get_holidays_list
from datetime import date, timedelta

from nsetools import Nse


nse = Nse()

all_stock_codes = nse.get_stock_codes()
symbols = all_stock_codes.keys()

dt_today = date.today()
series = "EQ"


for data_symbol in symbols:
    tradingSymbol = data_symbol
    endDate = dt_today
    startDate = endDate - dr.relativedelta(days=365)
    series = "EQ"
    stockData_EQ = pd.DataFrame()
    stockData_EQ = gh(symbol=tradingSymbol, start=startDate, end=endDate,index=False, futures=False, option_type="",
                expiry_date=None, strike_price="",series='EQ')
    print(stockData_EQ)