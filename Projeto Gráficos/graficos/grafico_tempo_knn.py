import numpy as np
import matplotlib.pyplot as plt

#https://matplotlib.org/examples/api/barchart_demo.html

N = 10
UK = (6, 15,	27,	37, 39,	40,	55,	65,	69,	72)
USA =  (7,	12,	12,	16,	29,	36,	36,	42,	47,	59)
Italy = (3,	10,	15,	23,	23,	30,	32,	42,	47,	48)
Brazil = (0,	4,	15,	16,	27,	30,	33,	41,	42,	42)
Canada = (3,	6,	15,	25,	29,	34,	34,	34,	34,	38)
China = (0,	1,	1,	1,	5,	5,	13,	21,	21,	21)
Spain = (3,	6,	11,	17,	17,	17,	17,	17,	17,	17)
Luxembourg = (0,	0,	0,	1,	7,	10,	11,	12,	15,	15)
Norway = (0, 0,	1,	4,	4,	8,	9,	10,	12,	12)
Germany =(0,	3,	9,	9,	9,	9,	10,	11,	11,	11)
Sweden =(0,	5,	5,	5,	5,	5,	7,	7,	7,	11)
Czech_Republic =(0,	0,	0,	5,	5,	10,	10,	10,	10,	10)

ind = np.arange(N)    # the x locations for the groups
width = 0.6       # the width of the bars

#
plt.plot(UK, marker='P', color='navy', label='UK')

plt.plot(USA, marker='s', color='blue', label='USA')
plt.plot(Italy, marker='|', linestyle=':', color='green', label='Italy')
plt.plot(Brazil, marker='D', linestyle='-.', color='gold', label='Brazil')
plt.plot(Canada, marker='v', linestyle='--', color='red', label='Canada')

plt.plot(China, marker='*', linestyle='-', color='red', label='China')
plt.plot(Spain, marker='p', linestyle=':', color='gold', label='Spain')
plt.plot(Luxembourg, marker='+', linestyle='-.', color='cyan', label='Luxembourg')
plt.plot(Norway,  linestyle='--', color='purple', label='Norway')
plt.plot(Germany,  linestyle='-', color='black', label='Germany')
plt.plot(Sweden,  linestyle=':', color='steelblue', label='Sweden')
plt.plot(Czech_Republic, linestyle='-.', color='orange', label='Czech Republic')
# plt.plot(Total, marker=)
plt.legend()

plt.xticks(ind, ('2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'))
# plt.yscale('log')


# plt.show()
plt.savefig('paises.pdf')
plt.close()