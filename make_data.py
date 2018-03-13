import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime 

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage_key import av_key

###
tickers = ['VTI',
           'VEA',
           'VWO',
           'VNQ',
           'VNQI',
           'TIP',
           'TLT',
           'DBC']

labels_list = ['Vanguard Total Stock Market ETF',
               'Vanguard FTSE Developed Markets ETF',
               'Vanguard FTSE Emerging Markets ETF',
               'Vanguard REIT ETF (VNQ)',
               'Vanguard Global ex-US Real Estate ETF',
               'iShares TIPS Bond (TIP)',
               'iShares 20+ Year Treasury Bond',
               'PowerShares DB Commodity Tracking']

tkr_lbl = dict(zip(tickers, labels_list))
tkr_lbl = '\n'.join('{}: {}'.format(key, val) for key, val in sorted(tkr_lbl.items()))
print(tkr_lbl)
labels = np.asarray(labels_list)


infile = 'portfolio.xlsx'

def portfolio_load(portfolios):

	portfolio = {}
	
	for p in portfolios:
		print "Reading {} portfolio...".format(p)
		tmpdata = pd.read_excel(infile, sheet_name=p, header=0)
	
	#return X

def data_load():
	raw_data = {}

	ts = TimeSeries(key=av_key, output_format='pandas')

	for t in tickers:

	    #data = DataReader(t,'yahoo', start, end)
	    #data = pd.read_csv('stock_prices.csv', header=0) # offline read-in of sample data
	    data, metadata = ts.get_weekly_adjusted(t)

	    raw_data[t] = data

	pan = pd.Panel(raw_data)
	#pan_close = pan.minor_xs('Adj Close')
	pan_close = pan.minor_xs('4. close') # activate when online read-in 
	pan_close.index = pan_close.index.to_datetime() #convert index to timeseries format

	return pan, pan_close
	print('executed')

