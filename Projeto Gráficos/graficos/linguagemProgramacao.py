import numpy as np
import matplotlib.pyplot as plt

N = 7

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo
blocoMindstorms = (8,14,14,14,19,23,23)
c = (1,1,2,2,3,4,6)
cMais = (0,2,4,7,11,22,29)
java = (0,1,2,2,2,2,3)
nenhum = (2,3,5,10,15,17,17)
programacaoBloco = (0,0,1,1,2,8,10)
python = (0,2,5,5,7,9,9)
rodoEduc = (1,2,2,3,4,6,6)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões
plt.plot(blocoMindstorms,marker='.',linestyle='-',color='#000000',label='Bloco Mindstorms')
plt.plot(c,marker='+', linestyle='-', color='black',label='Linguagem C')
plt.plot(cMais, marker='s',linestyle='-',color='#00FFFF',label='Linguagem C++')
plt.plot(java, marker='o', linestyle='-', color='#006400', label='Java')
plt.plot(nenhum, marker='*', linestyle='-',color='#8B4513', label='Nenhuma')
plt.plot(programacaoBloco, marker='X', linestyle='-', color='#D2691E', label='Programação em blocos')
plt.plot(python, marker='.', linestyle='-', color='#4B0082', label='Python')
plt.plot(rodoEduc, marker='+', linestyle='-', color='#FF00FF', label='RodoEduc')

plt.legend()

plt.xticks(ind, ('2010','2012', '2013', '2014', '2015', '2016', '2018'))
#plt.yscale('log')


plt.show()
#plt.savefig('pbalvo.pdf')
plt.close()
