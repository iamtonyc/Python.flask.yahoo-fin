def find_stock_sharpe_by_yahoo_fin(code):
	import numpy as np
	import pandas as pd
	import matplotlib as plt
	import matplotlib.dates as date
	import datetime
	# %matplotlib inline
	from numpy.random import randn
	from yahoo_fin.stock_info import get_analysts_info, get_data
	from stock import Stock

	df=get_data(code)
	df=df.drop(df.columns[[0,1,2,3,5,6]], axis=1)
	df.sort_index(inplace=True,ascending=False)
	stock_returns = df.pct_change()
	stock_mean_return = stock_returns.mean()
	stock_return_stdev = stock_returns.std()
	stock_annualised_return = round(stock_mean_return * 252,2)
	stock_annualised_stdev = round(stock_return_stdev * np.sqrt(252),2)
	stock_sharpe_ratio=(stock_mean_return/stock_return_stdev)
	stock_sharpe_ratio=(252**0.5)*stock_sharpe_ratio

	myStock=Stock()
	myStock.code=code
	myStock.stock_annualised_return=format(stock_annualised_return.values)
	myStock.stock_return_stdev=format(stock_annualised_stdev.values)
	myStock.stock_sharpe_ratio=format(stock_sharpe_ratio.values)
	
	return myStock
