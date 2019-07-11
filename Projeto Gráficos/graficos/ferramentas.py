import numpy as np
import matplotlib.pyplot as plt

N = 7

#Citação gráfico cumulativo
aerodromo = (0,0,0,1,1,2)
arduinoIde = (0,2,4,7,10,18,21)
ferramentaPropria = (4,4,4,4,4,4,4)
labView = (0,0,1,1,3,3,3)
legalPlataform = (0,0,0,0,1,2,0)
legoMindstorms = (4,9,9,9,14,18,20)
matLab = (0,0,0,1,4,4,1)
mindstorms = (0,0,0,0,0,1,2)
nenhumaFerramenta = (3,7,9,14,17,20,20)
openCv = (0,0,0,0,0,2,2)
rEduc = (1,1,1,2,3,3,3)
scratch = (0,0,1,1,1,2,2)
simulink = (0,0,1,1,2,2,2)
vRep = (0,0,0,0,0,1,3)
wEduc = (0,0,0,0,1,3,3)



ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões
plt.plot(aerodromo, marker='.', linestyle='-', color='#000000', label='Aerodromo')
plt.plot(arduinoIde, marker='+', linestyle='-', color='#000080', label='Arduino IDE')
plt.plot(ferramentaPropria, marker='s', linestyle='-', color='#00FFFF', label='Ferramenta Propria')
plt.plot(labView, marker='o', linestyle='-', color='#006400', label='Lab View')
plt.plot(legalPlataform, marker='*', linestyle='-', color='#8B4513', label='Legal Plataform')
plt.plot(legoMindstorms, marker='x', linestyle='-', color='#D2691E', label='Lego Mindstorms')
plt.plot(matLab, marker='.', linestyle='-', color='#4B0082', label='Mat Lab')
plt.plot(mindstorms, marker='+', linestyle='-', color='#FF00FF', label='Mindstorms')
plt.plot(nenhumaFerramenta, marker='*', linestyle='-', color='#9932CD', label='Nenhuma Ferramenta')
plt.plot(openCv, marker='s', linestyle='-', color='#CFB53B', label='Open CV')
plt.plot(rEduc, marker='o', linestyle='-', color='#FF6EC7', label='R-Educ')
plt.plot(scratch, marker='*', linestyle='-', color='#236B8E', label='Scratch')
plt.plot(simulink, marker='.', linestyle='-', color='#D8BFD8', label='Simulink')
plt.plot(vRep, marker='+', linestyle='-', color='#4F4F2F', label='vRep')
plt.plot(wEduc, marker='*', linestyle='-', color='#4F2F4F', label='wEduc')
plt.legend()

plt.xticks(ind, ('2010','2012', '2013', '2014', '2015', '2016', '2018'))
#plt.yscale('log')


#plt.show()
plt.savefig('ferramentas.pdf')
#plt.close()

#grafico aparentemente ok
