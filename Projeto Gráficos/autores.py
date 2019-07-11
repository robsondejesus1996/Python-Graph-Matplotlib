import matplotlib.pyplot as plt
import re
import csv
import pandas as pd
from numpy import sort


path_source = 'csv/autores.csv'
path_data = 'results/'

df = pd.read_csv(path_source,  usecols=['Year', 'Author 1', 'Country 1', 'City 1', 'University 1', 'Department 1', 'Gender', 'Type']) #', ' encoding="ISO-8859-1"

# sobrenomes = []
# for i in range(0, len(df.index)):
#     autor = df.iloc[i, 1]
#     # print aux_uni
#     # print autor
#     sobrenome = autor.split(' ')[-1:]
#     # print sobrenome
#     sobrenomes.append(sobrenome)
#
# for i in range(0, len(sobrenomes)-1):
#     for j in range(i+1, len(sobrenomes)):
#         if sobrenomes[i] == sobrenomes[j]:
#             if df.iloc[i, 1] != df.iloc[j, 1]:
#                 # if df.iloc[i, 1][0] == df.iloc[j, 1][0]:
#                 print df.iloc[i, 1]
#                 print df.iloc[j, 1]
#                 print '--------------------'

# autores, sairam, entraram, churn
resultados = {}

#calcular entradas por ano
for a in range(2009, 2019):
    entrada = []
    saida = []
    manteve = []
    if a > 2009:
        saida = resultados[a-1][0] + resultados[a-1][1]
    for i in range(0, len(df.index)):
        ano = df.iloc[i, 0]
        autor = df.iloc[i, 1]
        if a == 2009 and ano == 2009:
            entrada.append(autor)
        elif ano == a:
            if not entrada.__contains__(autor):
                if not resultados[a-1][0].__contains__(autor) and not resultados[a-1][1].__contains__(autor):
                    #novo
                    entrada.append(autor)
                    if saida.__contains__(autor):
                        saida.remove(autor)

                elif resultados[a-1][0].__contains__(autor) or resultados[a-1][1].__contains__(autor):
                    #manteve
                    if not manteve.__contains__(autor):
                        manteve.append(autor)
                        if saida.__contains__(autor):
                            saida.remove(autor)



    # print entrada
    resultados[a] = [entrada, manteve, saida]


#for i in resultados:
#     print i
#     for j in resultados[i]:
#         print str(len(j))
#         print j

for i in range(2009, 2019):
    # churn
    rotatividade = 0.0
    if i > 2009:
        total_ant = float(len(resultados[i - 1][0]) + len(resultados[i - 1][1]))
        novos = float(len(resultados[i][0]))

        rotatividade = float(float((float(novos*100))/total_ant))

    print str(i) + '; ' + str(len(resultados[i][0])) + '; ' + str(len(resultados[i][1])) + '; ' + str(len(resultados[i][2])) + '; ' + str(rotatividade)

