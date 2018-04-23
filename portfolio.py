import numpy as np
import pandas as pd
import openpyxl as pyxl
from datetime import datetime

class _Portfolio (object):
	def __init__(self, indata):
		self.data = indata

	def subclass(self):
		pass

class analysis(_Portfolio):

	def __init__(self, indata):
		_Portfolio.__init__(self, indata)

	def summary_stats(self, column):
		
		self.data = self.data[column]
		self.mean = self.data.mean()
		self.min = self.data.min()
		self.max = self.data.max()
		self.std = self.data.std()

		#ctwr = (1 + HPR1)*(1 + HPR2)*(1 + HPR3)…*(1 + HPRn-1)*(1 + HPRn) – 1
		#twr = (1 + compounded TWRR) 1/n – 1

		#self.bv = self.data['Purchase amount'] * self.data['Purchase price'] # buy value
		#self.pv = (self.data['Purchase amount'] - self.data['Sell amount']) * self.data['Market price'] #present value

		return self.mean, self.min, self.max, self.std

### Data read-in
wb = pyxl.load_workbook('portfolio.xlsx')

data, portfolio_set = {}, {}
for count, sheet in enumerate(wb.worksheets, 0):
	#name = 'p{}'.format(count)
	data[count] = pd.DataFrame(sheet.values)
	columns = data[count].iloc[0]

	data[count].columns = columns
	data[count] = data[count][1:]

	portfolio_set[count] = data[count]


#/ Create portfolio objects
if __name__ == '__main__':
    portfolios = []
    for obj in portfolio_set:
        obj = analysis(portfolio_set[obj])
        portfolios.append(obj)

out = {}
for count, n in enumerate(portfolio_set,0):
	out[n] = portfolios[count].summary_stats('Sell price')

out_dat = pd.DataFrame.from_dict(out, orient='columns') #orient='index' for column-row inverse
out_dat = out_dat.set_axis(['mean', 'min', 'max', 'std'], axis=0, inplace=False) #axis = 1 for column-row inverse

out_dat['mean'] = out_dat.mean(axis=1)


#/ Time-weighted rate of return (twror)

#def twror(pv,c,superiods, data):

	#twror = 1.0
	#pv[0] = 0.0

	#for t in range(0,subperiods,1):

		#pv[t] = portfolio_value(t, data)
		#netinflow[t] = portfolio[t]['Purchase price'] * portfolio[t]['Purchase amount'] - portfolio[t]['Sell price'] * portfolio[t]['Sell amount']
		#hpr[t] = (pv[t] - netinflow[t]) / pv[t-1] -1

		#twror *= (1.0 + hpr)

	#ctwror = (twror**(1.0/(subperiods-1))) - 1
	#return ctwror

#pv = [10.0, 1.1*10, 1.1*1.1*10, 1.1*1.1*1.1*10] # portfolio value in period t
#c = [0.0, 0.0, 0.0, 0.0] # net inflow in period t
#subperiods = len(pv)
#result = twror(pv,c,subperiods,portfolio_set)

'''
def portfolio_value(t, data):
	for p in portfolio_set:
		for d in portfolio_set:

		holding = data[p][][df.index <= t].sum()  
		holding_amount = 
		pv[t] = [index<=t]
'''

price = 1 #45.60
end_date = '2017-12-31'
end_date = datetime.strptime(end_date, '%Y-%m-%d')
t=1

purchases, sales, holding_amount, pv, net_inflow, pv_change, tw_ror = {}, {}, {}, {}, {}, {}, {}
df_temp = {'DBX': 1.0,
		   'HFG': 1.0}

def twror(inital):

	for p in portfolio_set:
		#purchases = portfolio_set[p]['Purchase amount']
		#sales = portfolio_set[p]['Sell amount']
		tw_ror[p] = 1.0
		holding = ['DBX', 'HFG']

		for t in range(0,len(portfolio_set[p].index)+1,1):
			columns = 'Holding'
			purchases_cum = portfolio_set[p]['Purchase amount'].iloc[0:t].groupby(portfolio_set[p][columns]).agg('sum') # < datetime.strptime('2017-07-01', '%Y-%m-%d')
			sales_cum 	  = portfolio_set[p]['Sell amount'].iloc[0:t].groupby(portfolio_set[p][columns]).agg('sum')
			
			if t==0:
				pv[p,t]= initial
				pv_change[p,t] = 1.0

				df_temp[p] = 1.0
			else:
				pv[p,t] = (purchases_cum - sales_cum) * price # Merge pv and price datasets
			
				#net_inflow[t] = portfolio_set[p]['Purchase amount'].iloc[(t-1):t]  
				pv_change[p,t] = (pv[p,t] / pv[p,(t-1)]) 
				pv_change[p,t] = pv_change[p,t].fillna(1.0) # delete after issues resolved

			'''
			for h in holding:
				if t == 0:
					continue
				else:
					df_temp[p] *= pv_change[p,t]['HFG']
			'''

		#df_temp[p] = pv_change[p,t].groupby(pv_change[p,t].keys()).agg('sum')

				#for h in ['DBX', 'HFG']:
				#	df_temp[p] *= pv_change[p,t][h]


		#for i in np.arange(0,10,1):
		#	temp[p] *= (1 + pv_change[p,i])

		#temp = 1.0
		#temp[p] += pv_change[p,t].values()
 
		'''
		for i in pv_change:
			temp *= (1+pv_change[i])
			print(temp)
		'''
			#tw_ror[p] += pv_change[p,t].agg('sum')

			#tw_ror[p] *= pv_change[p,t][pv_change[p,t].index == 'DBX']
			#tw_ror[p] *= pv_change[p,t][pv_change[p,t].index == 'DBX']
			



				#tw_ror[p]   *= (1.0 + pv_change[p,t]) -1

		#ctwror = (twror**(1.0/(len(portfolio_set[p].index)-1)))
		#return ctwror

initial = 1000
result = twror(initial)
print(result)