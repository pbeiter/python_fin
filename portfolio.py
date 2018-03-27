import numpy as np
import pandas as pd
import openpyxl as pyxl

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


#/ Time-weighted rate of return (TWRR)

def twror(pv,c,superiods):

	twr = 1.0

	for t in range(1,subperiods,1):

		hpr = (pv[t] - c[t])/pv[t-1] - 1.0
		print(t, hpr)
		twr *= (1.0 + hpr)
		print(twr)

	ctwr = (twr**(1.0/(subperiods-1))) - 1
	return ctwr

pv = [10.0, 1.1*10, 1.1*1.1*10, 1.1*1.1*1.1*10]
c = [0.0, 0.0, 0.0, 0.0]
subperiods = len(pv)
result = twror(pv,c,subperiods)
print(result)