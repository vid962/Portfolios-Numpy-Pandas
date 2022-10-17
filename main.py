from idlelib.multicall import r

import ap as ap
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime as dt

import requests

tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
start = dt.datetime(2021, 1, 1)
data = pdr.get_data_yahoo(tickers, start)

data = data['Adj Close']

data_head = data.head()

# -------------------------------------->>     PORTFOLIOS

# Apple, Microsoft, Twitter, IBM

portfolios = [.25, .15, .40, .20]

np.sum(portfolios)

# our data normalized to 1 (1.0 is the moment we bought the shares)
data_normalized = data/data.iloc[0]

# total investment in our portfolio
initial_investment = 100000

# normalized data multiplied by our portfolio
data_normalized_portfolio = data/data.iloc[0] * portfolios * initial_investment

print(data_normalized_portfolio)






