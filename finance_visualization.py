import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from pandas.io.data import DataReader # datareader no longer support yahoo finance API; import manual file downloads instead
from datetime import datetime
import pylab
import seaborn as sns
import matplotlib.ticker as mtick

sns.set(style="white")

#plt.ion()
plt.style.use('ggplot')

### Visualization

def visualization (x, y, tickers, title, labels, type, xmin, xmax, ymin, ymax, yformat):

	if type=='line':

		fig, ax = plt.subplots(figsize=(8, 7)) #sharex = True
		
		if yformat=='percent':
			fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
			yticks = mtick.FormatStrFormatter(fmt)
			ax.yaxis.set_major_formatter(yticks)

		for t, l in zip(tickers, labels):
        	
			ax = plt.axis([xmin,xmax,ymin,ymax])
			ax = plt.plot(x, y[t], label=l)

		ax = plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=8)
		#ax = plt.legend(loc='upper left', shadow='True', fontsize=7)

		#fig.savefig('samplefigure', bbox_extra_artists=(lgd,), bbox_inches='tight')
		fig.savefig('fig/{}_plot_{}.png'.format(type, title, dpi=1000), bbox_inches='tight') #bbox_extra_artists=(lgd,),
        
		fig.clf()

	elif type=='corr':

		fig, ax = plt.subplots(figsize=(8, 9))
		pos = ax.get_position() # get the original position 
		
		sns.corrplot(y)

		plt.text(pos.x0 -0.5, pos.y0 + 10, labels)

		plt.savefig('fig/{}_plot_{}.png'.format(type, title, dpi=1000, bbox_inches='tight')) #bbox_inches='tight', tight_layout=True
		
		fig.clf()

	elif type=='hist':
		
		fig, ax = plt.subplots(figsize=(8, 9))
		
		for t, l in zip(tickers, labels):
			
			#ax = plt.hist(np.log((y/y.shift(1)).dropna()[t]), bins=50, normed=True, alpha=0.7, label=l)
			ax = np.log(y/y.shift(1)).dropna()[t].plot(kind='kde', alpha=0.7, label=l)

		ax = plt.legend(loc=9, bbox_to_anchor=(0.5, -0.025), ncol=2, fontsize=8)

		plt.savefig('fig/{}_plot_{}.png'.format(type, title, dpi=1000, bbox_inches='tight'))

		fig.clf()

	elif type=='boxplot':

		fig, ax = plt.subplots(figsize=(8, 10))

		ax = plt.boxplot(y.dropna().values)
		ax = plt.xticks(range(len(tickers)), labels, rotation=45, fontsize=8) #range(1,7),

		plt.tight_layout()

		plt.savefig('fig/{}_plot_{}.png'.format(type, title, dpi=1000, bbox_inches='tight'))

		fig.clf()
	
	else:
		print('Visualization type not defined')



'''

def visualization (x, y, tickers, type):
    fig = plt.figure()
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    axes = fig.add_axes([left, bottom, width, height])

    for i in range(len(tickers)):
        axes.plot(x, y, label=tickers)
        axes.legend(loc='upper left')

    fig.savefig('plot123.png')
    fig.clf()
    #axes.set_xlabel('x')
    #axes.set_ylabel('y')
    #axes.set_title('title');


x=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
 y=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[7,8,9,10]]
 colours=['r','g','b','k']

 for i in range(len(x)):
    plt.plot(x[i],y[i],colours[i])

def visualization (x, y, tickers, type):
    fig, axes = plt.subplots(nrows=1, ncols=1)
    for i, c in enumerate(y):
    y[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c)
    plt.savefig('EU1.png', bbox_inches='tight')

#fig.autofmt_xdate()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax3 = fig.add_subplot(2,2,2)

ax1.plot(pan_close.index, pan_close['VTI'], label='Vanguard Total Stock Market ETF')
ax1.plot(pan_close.index, pan_close['VEA'], label='Vanguard FTSE Developed Markets ETF')
ax1.plot(pan_close.index, pan_close['VWO'], label='Vanguard FTSE Emerging Markets ETF')
ax1.plot(pan_close.index, pan_close['VNQ'], label='Vanguard REIT ETF (VNQ)')
ax1.plot(pan_close.index, pan_close['VNQI'], label='Vanguard Global ex-US Real Estate ETF')
ax1.plot(pan_close.index, pan_close['TIP'], label='iShares TIPS Bond (TIP)')
ax1.plot(pan_close.index, pan_close['TLT'], label='iShares 20+ Year Treasury Bond')
ax1.plot(pan_close.index, pan_close['DBC'], label='PowerShares DB Commodity Tracking')

ax2.plot(pan_close_ix.index, pan_close_ix['VTI'], label='VTI')
ax2.plot(pan_close_ix.index, pan_close_ix['VEA'], label='VEA')
ax2.plot(pan_close_ix.index, pan_close_ix['VWO'], label='VWO')
ax2.plot(pan_close_ix.index, pan_close_ix['VNQ'], label='VNQ')
ax2.plot(pan_close_ix.index, pan_close_ix['VNQI'], label='VNQI')
ax2.plot(pan_close_ix.index, pan_close_ix['TIP'], label='TIP')
ax2.plot(pan_close_ix.index, pan_close_ix['TLT'], label='TLT')
ax2.plot(pan_close_ix.index, pan_close_ix['DBC'], label='DBC')

ax2.set_xlim([first_valid_loc, date])

ax3 = plt.matshow(pan_close.corr())

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

plt.pause(5) 

fig.savefig('plot.png')
fig.show()

#pan = pd.DataFrame(list(datalist.items()), columns = tickers)
#pan = pd.DataFrame({"key": datalist.keys(), "value": datalist.values()})
#pan = pd.DataFrame([[i] for i in datalist.values()],index=datalist)
#pan = pd.DataFrame.from_records(datalist, index = 'k1')
#pan = pd.DataFrame(datalist, index=np.arange(2588))
#pan = pd.DataFrame.from_dict(datalist.items(), orient='index')
#pan = pd.DataFrame(datalist.items(), columns=datalist.)

ax3 = plt.matshow(pan_close.corr())
'''





