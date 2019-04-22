def find_stock_sharpe(fileName):
	import numpy as np
	import pandas as pd
	import matplotlib as plt
	import matplotlib.dates as date
	import datetime
	#%matplotlib inline
	from numpy.random import randn
	from stock import Stock


	dfStock = pd.read_csv(fileName, parse_dates=['Date'], dayfirst =True)
	dfStock= dfStock.drop(dfStock.columns[[1,2,3,4,6]], axis=1)
	dfStock=dfStock.set_index(dfStock.columns[0])
	stock_returns = dfStock.pct_change()
	stock_mean_return = stock_returns.mean()
	stock_return_stdev = stock_returns.std()
	stock_annualised_return = round(stock_mean_return * 252,2)
	stock_annualised_stdev = round(stock_return_stdev * np.sqrt(252),2)
	stock_sharpe_ratio=(stock_mean_return/stock_return_stdev)
	stock_sharpe_ratio=(252**0.5)*stock_sharpe_ratio

	myStock=Stock()
	code=fileName.split(".")
	myStock.code=code[0]
	myStock.stock_annualised_return=format(stock_annualised_return.values)
	myStock.stock_return_stdev=format(stock_annualised_stdev.values)
	myStock.stock_sharpe_ratio=format(stock_sharpe_ratio.values)
	#print("The annualised mean return of stock is {}".format(stock_annualised_return.values))
	#print("The annualised volatility is {}".format(stock_annualised_stdev.values))
	#print("Sharpe Ratio of stock is {}".format(stock_sharpe_ratio.values))
	# return format(stock_annualised_return.values)
	return myStock
