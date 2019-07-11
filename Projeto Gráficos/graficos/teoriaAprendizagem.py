import numpy as np
import matplotlib.pyplot as plt
from numpy.core.tests.test_scalarinherit import A

N = 18

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo
ABP = (0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,6,7,7)
C = (1,1,1,1,1,1,2,2,3,9,9,9,9,12,12,15,17,18)
CT = (0,0,1,1,4,5,9,11,12,23,26,35,43,53,73,91,100,109)
#DC =(0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2)
#DD = (0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,3)
DT = (0,0,0,0,0,0,0,0,0,1,4,8,8,12,15,15,15,15)
#ID = (0,0,0,0,0,0,0,0,0,0,0,1,1,1,3,3,3,4)
LB = (0,0,1,1,1,1,1,3,3,4,7,8,12,19,24,27,30,36)
nenhuma = (0,0,0,1,1,1,1,1,2,2,3,3,4,4,4,6,7,7)
PC = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,9)
PS = (0,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3)
#RF = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2)
#TL = (0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,3)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões

plt.plot(CT,marker='o',linestyle='-',color='#D8BFD8',label='Construtivismo (CT)')
plt.plot(LB,marker='*',linestyle='-',color='#4B0082',label='Experimental (LB)')
plt.plot(C,marker='*',linestyle='-',color='#DC143C',label='Construcionismo (C)')
plt.plot(DT,marker='X',linestyle='-',color='#F0E68C',label='Demonstrativo (DT)')
plt.plot(PC,marker='s',linestyle='-',color='#FFA500',label='Pensamento computacional (PC)')
plt.plot(nenhuma,marker='o',linestyle='-',color='red',label='Nenhuma')
#plt.plot(ID,marker='.',linestyle='-',color='#FF1493',label='Indutivo (ID)')
#plt.plot(TL,marker='.',linestyle='-',color='#B0E0E6',label='Teaching Learning (TL)')
plt.plot(ABP,marker='.',linestyle='-',color='#000000',label='Abordagem Baseada em Problemas (ABP)')
#plt.plot(DC,marker='s',linestyle='-',color='#000080',label=' Directiva (DC)')
#plt.plot(DD,marker='+',linestyle='-',color='#006400',label='Dedutiva (DD)')
plt.plot(PS,marker='+',linestyle='-',color='#7FFFD4',label='Solução de Problemas (PS)')
#plt.plot(RF,marker='X',linestyle='-',color='#8B4513',label='Reflexivo (RF)')


plt.legend()
plt.xticks(ind, ('2001','2002', '2003', '2004', '2005', '2006', '2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'))
plt.xticks(rotation=90)

#plt.yscale('log')


#plt.show()
plt.savefig('teoriaAprendizagem.pdf')
#plt.close()