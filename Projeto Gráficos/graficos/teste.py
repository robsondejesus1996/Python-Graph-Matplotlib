import numpy as np
import matplotlib.pyplot as plt

N = 7

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo
Zero = (10,14,19,24,33,54,62)
Um = (1,7,9,11,14,15,15)
Teste = (1,1,1,1,1,1,1)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões
plt.plot(Zero,marker='*',linestyle='-',color='black',label='Zero')
plt.plot(Um,marker='p',linestyle='-',color='red',label='Um')
plt.plot(Teste,marker='x',linestyle='-',color='black',label='teste')

plt.legend()

plt.xticks(ind, ('2010','2012', '2013', '2014', '2015', '2016', '2018'))
#plt.yscale('log')


plt.show()
#plt.savefig('pbalvo.pdf')
plt.close()
