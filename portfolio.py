import numpy as np
import pandas as pd

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

		#for placeholder in ['mean', 'min', 'max', 'std']:
		#	self.placeholder = np.round(placeholder, decimals = 2)

		return self.mean, self.min, self.max, self.std

### Portfolio p1
data1 = pd.DataFrame({'row1': [25, 30, 45],
					  'row2': [50, 34, 98],
					  'row3': [100, 56, 80],
					})

data2 = pd.DataFrame({'row1': [25, 30, 45],
					  'row2': [50, 34, 98],
					  'row3': [9000, 3500, 500000],
					})

#infile = XXX
#for count, p in enumerate(portfolio, 0):
#	portfolio[count] = pd.read
#portfolio_set = pd.read_csv(infile, sheet_name = 'X', header=0)
portfolio_set = {'Portfolio1': data1, 
				 'Portfolio2': data2,
				 }

if __name__ == '__main__':
    portfolios = []
    #for obj in range(len(portfolio_set)):
    for obj in portfolio_set:
        obj = analysis(portfolio_set[obj])
        portfolios.append(obj)

out = {}
for count, n in enumerate(portfolio_set,0):
	out[n] = portfolios[count].summary_stats('row3')

out_dat = pd.DataFrame.from_dict(out, orient='columns') #orient='index' for column-row inverse
out_dat = out_dat.set_axis(['mean', 'min', 'max', 'std'], axis=0, inplace=False) #axis = 1 for column-row inverse

out_dat['mean'] = out_dat.mean(axis=1)

