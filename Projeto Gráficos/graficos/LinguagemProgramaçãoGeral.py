import numpy as np
import matplotlib.pyplot as plt

N = 18

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo

#todas as linguagens de programação
C = (0,1,1,1,1,1,1,1,1,3,3,4,7,9,13,22,23,30)#ok
#C_Sharp = (0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2)#ok
C_POO = (0,1,1,2,2,2,3,3,3,4,4,7,11,13,19,32,35,45)#ok
Java = (0,0,0,0,0,0,1,1,1,2,3,3,4,4,4,4,6,7)#ok
#Legal = (0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2)#ok
Logo = (0,0,0,0,1,1,2,3,3,4,4,4,4,4,4,4,6,6)#ok
Nenhuma_Linguagem = (0,0,0,0,0,0,1,2,2,4,6,10,12,21,29,32,37,38)#ok
Programacao_Blocos = (0,1,3,3,4,5,6,7,7,17,19,26,28,35,45,62,71,79)#
Python = (0,0,0,0,0,0,0,0,0,0,0,2,4,4,6,9,11,14)
R_EDUC = (0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,4,4,4)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões



plt.plot(Programacao_Blocos,marker='.',linestyle='-',color='#FF4500',label='Programação em blocos')
plt.plot(C_POO,marker='o',linestyle='-',color='red',label='C++')
plt.plot(Nenhuma_Linguagem,marker='*',linestyle='-',color='#800000',label='Nenhuma')
plt.plot(C,marker='s',linestyle='-',color='#000000',label='C')
plt.plot(Python,marker='+',linestyle='-',color='#FFFF00',label='Python')
plt.plot(Java,marker='X',linestyle='-',color='#006400',label='Java')
plt.plot(Logo,marker='.',linestyle='-',color='#8B008B',label='Linguagem Logo')
plt.plot(R_EDUC,marker='s',linestyle='-',color='#B0E0E6',label='R-EDUC')
#plt.plot(C_Sharp,marker='*',linestyle='-',color='#000080',label='C#')
#plt.plot(Legal,marker='o',linestyle='-',color='#8B4513',label='Linguagem Legal')

plt.legend()
plt.xticks(ind, ('2001','2002', '2003', '2004', '2005', '2006', '2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'))
plt.xticks(rotation=90)


#plt.yscale('log')


plt.show()
#plt.savefig('LinguagemProgrramacaoGeral.pdf')
plt.close()
