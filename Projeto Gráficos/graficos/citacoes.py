import numpy as np
import matplotlib.pyplot as plt

N = 7

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo
zero = (10,14,19,24,33,54,62)
um = (1,7,9,11,14,15,15)
dois = (0,0,1,3,6,6,6)
tres = (0,0,1,1,2,2,2)
quadro = (1,1,1,2,5,6,6)
cinco = (0,0,0,1,1,1,1)
seis = (1,1,1,2,2,2,2)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões
plt.plot(zero,marker='*',linestyle='-',color='black',label='Zero')
plt.plot(um,marker='+',linestyle='-',color='red',label='Um ')
plt.plot(dois,marker='s',linestyle='-',color='orange',label='Dois ')
plt.plot(tres,marker='s',linestyle='-',color='yellow',label='Três ')
plt.plot(quadro,marker='s',linestyle='-',color='green',label='Quatro ')
plt.plot(cinco, marker='s',linestyle='-',color='blue',label='Cinco ')
plt.plot(seis, marker='s',linestyle='-',color='violet',label='Seis ')


plt.legend()

plt.xticks(ind, ('2010','2012', '2013', '2014', '2015', '2016', '2018'))
plt.yscale('log')


plt.show()
#plt.savefig('pbalvo.pdf')
plt.close()
