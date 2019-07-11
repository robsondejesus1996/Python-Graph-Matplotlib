import numpy as np
import matplotlib.pyplot as plt

N = 7

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo
aerodromo  = (0,0,0,0,0,1,1)#
arduino = (0,3,5,9,13,22,28)#
ev3 = (5,5,5,5,8,9,9)#
legoMindstorms = (0,5,5,5,5,6,6)#
nenhum = (2,3,7,12,15,17,17)
nxt =(5,6,6,7,11,14,15)
pololu = (0,0,0,0,0,1,2)
raspberryPi = (0,0,1,1,2,2,2)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões
plt.plot(aerodromo ,marker='.',linestyle='-',color='#000000',label='Aerodromo')
plt.plot(arduino,marker='+',linestyle='-',color='#000080',label='Arduino')
plt.plot(ev3,marker='s',linestyle='-',color='#00FFFF',label='EV3')
plt.plot(legoMindstorms,marker='o',linestyle='-',color='#006400',label='Lego Mindstorms')
plt.plot(nenhum,marker='*',linestyle='-',color='#8B4513',label='Nenhum')
plt.plot(nxt,marker='x',linestyle='-',color='#D2691E',label='NXT')
plt.plot(pololu,marker='*',linestyle='-',color='#4B0082',label='Pololu')
plt.plot(raspberryPi,marker='o',linestyle='-',color='#FF00FF',label='Raspberry Pi')

plt.legend()

plt.xticks(ind, ('2010','2012', '2013', '2014', '2015', '2016', '2018'))
#plt.yscale('log')


#plt.show()
plt.savefig('arquitetura.pdf')
#plt.close()

# grafico aparentemente ok