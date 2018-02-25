import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from pandas_datareader import data, wb # datareader no longer support yahoo finance API; import via alpha_vantage or manual file downloads instead
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime 
import webbrowser
from urllib import pathname2url
import os
from alpha_vantage_key import av_key
import finance_visualization as vis
import html

reload(vis)

#plt.ion()
plt.style.use('ggplot')

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

date = datetime.now()
start = datetime(1990,1,1)
end = date

raw_data = {}

'''
for t in tickers:

    data = DataReader(t,'yahoo', start, end)

    raw_data[t] = data
'''

ts = TimeSeries(key=av_key)
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')

pan = pd.Panel(raw_data)
pan_close = pan.minor_xs('Adj Close')

corr = pan_close.corr()

pan_close.to_csv('stock_prices.csv')

# Indexed data
first_valid_loc = pan_close.apply(lambda col: col.first_valid_index()).max()

pan_close_ix = (pan_close/pan_close.ix[first_valid_loc])*100-100

max_pan_close, max_pan_close_ix = pan_close.dropna().values.max(), pan_close_ix.dropna().values.max()
min_pan_close, min_pan_close_ix = pan_close.dropna().values.min(), pan_close_ix.dropna().values.min()

print(max_pan_close, max_pan_close_ix,)

#Visualization

title1, type1 ='Historical', 'line'
name1 = type1+'_plot_'+title1
title2, type2 ='Historical (indexed)', 'line'
name2 = type2+'_plot_'+title2
title3, type3 ='Correlation matrix', 'corr'
name3 = type3+'_plot_'+title3
title4, type4 ='Histogram', 'hist'
name4 = type4+'_plot_'+title4
title5, type5 ='Boxplot', 'boxplot'
name5 = type5+'_plot_'+title5

vis.visualization(pan_close.index, pan_close, tickers, title1, labels, type1, datetime(2000,1,1), end, 0, max_pan_close*1.1, 'None')
vis.visualization(pan_close_ix.index, pan_close_ix, tickers, title2, labels, type2, first_valid_loc, end, min_pan_close_ix*1.1, max_pan_close_ix*1.1, 'percent')
vis.visualization('None', pan_close, 'None', title3, tkr_lbl, type3, 'None', 'None', 'None', 'None', 'None')
vis.visualization('None', pan_close, tickers, title4, labels, type4, 'None', 'None', 'None', 'None', 'None')
vis.visualization('None', pan_close, tickers, title5, labels, type5, 'None', 'None', 'None', 'None', 'None')

# Generate HTML report
html_loc = 'html/report.html' #C:/Users/pbeiter/Desktop/Python finance

html.html_gen(html_loc, name1, name2, name3, name4, name5)


'''
df['ma50'] = pd.rolling_mean(df['Close'], 50)
df['ma200'] = pd.rolling_mean(df['Close'], 200)

df_percent_chg = df_individual.pct_change()
'''