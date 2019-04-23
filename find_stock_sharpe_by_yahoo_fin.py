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
	df['daily_return'] = df['adjclose'].pct_change()
	df.sort_index(inplace=True,ascending=False)
	stock_mean_return = df['daily_return'].mean()
	stock_return_stdev =df['daily_return'].std()

	stock_annualised_return = round(252*stock_mean_return,2)
	stock_annualised_stdev = round(np.sqrt(252)*stock_return_stdev,2)
	stock_sharpe_ratio=round(np.sqrt(252)*stock_mean_return/stock_return_stdev,2)

	myStock=Stock()
	myStock.code=code
	myStock.stock_annualised_return=stock_annualised_return
	myStock.stock_return_stdev=stock_annualised_stdev
	myStock.stock_sharpe_ratio=stock_sharpe_ratio
	
	return myStock
