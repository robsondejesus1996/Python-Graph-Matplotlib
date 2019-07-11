import matplotlib.pyplot as plt
import re
import csv
import pandas as pd
from numpy import sort


path_source = 'csv/SSBSE2019c.csv'
path_data = 'results/'

df = pd.read_csv(path_source,  usecols=['Year','Title','Author 1','Country 1','City 1','University 1','Department 1','Author 2','Country 2','City 2','University 2','Department 2','Author 3','Country 3','City 3','University 3','Department 3','Author 4','Country 4','City 4','University 4','Department  4','Author 5','Country 5','City 5','University 5','Department  5','Author 6','Country 6','City 6','University 6','Department 6','Author 7','Country 7','City 7','University 7','Department 7','Keywords','ES Area Classification - level 0','ES Area Classification - level 1','ES Area Classification - level 2','ES Area Classification - level 3','Task Classification','Task','IC Techniques']) #', ' encoding="ISO-8859-1"

# ### media de autores por paper
# autores = []
# for i in range(0, len(df.index)):
#     aux_uni = [df.iloc[i, 2], df.iloc[i, 7], df.iloc[i, 12], df.iloc[i, 17], df.iloc[i, 22], df.iloc[i, 27], df.iloc[i, 32]]
#     cont=0
#     print aux_uni
#     for a in aux_uni:
#         if str(a).strip() != 'nan':
#             cont += 1
#     autores.append(cont)
#
# print autores
# print sum(autores)
# print len(autores)
# print float(sum(autores))/float(len(autores))

####################################### paises diferentes
### media de paises por paper
uni = []
for i in range(0, len(df.index)):
    aux_uni = [df.iloc[i, 3], df.iloc[i, 8], df.iloc[i, 13], df.iloc[i, 18], df.iloc[i, 23], df.iloc[i, 28], df.iloc[i, 33]]
    cont=0
    # print aux_uni
    aux_uni2 = []
    for j in range(0, 7):
        # print aux_uni
        if aux_uni[j] != 'nan':
            values_j = re.split(';| and |,', str(aux_uni[j]).strip())

            for v in values_j:
                if str(v).strip() == 'Republic of Korea':
                    v = 'Korea'
                elif str(v).strip() == 'The Netherlands':
                    v = 'Netherlands'
                elif str(v).strip() == 'Uk':
                    v = 'UK'

                if not aux_uni2.__contains__(v):
                    if str(v).strip() != 'nan':
                        aux_uni2.append(v)

    uni.append(aux_uni2)
cont = 0
for u in uni:
    if len(u) > 1:
        cont += 1
    # print u
print '#papers com paises diferentes'
print cont


####################################### instituicoes diferentes
uniequiv = {
    'university of sheffield': 'the university of sheffield',
    'fbk': 'fondazione bruno kessler',
    'ucl': 'university college london',
    'university of genoa': 'university of genova',
}
uni = []
for i in range(0, len(df.index)):
    aux_uni = [df.iloc[i, 5], df.iloc[i, 10], df.iloc[i, 15], df.iloc[i, 20], df.iloc[i, 25], df.iloc[i, 30], df.iloc[i, 35]]
    cont=0
    # print aux_uni
    aux_uni2 = []
    for j in range(0, 7):
        # print aux_uni
        if aux_uni[j] != 'nan':
            values_j = re.split(';| and ', str(aux_uni[j]).strip())
            values_j = [x.lower() for x in values_j]

            for v in values_j:
                if str(v).strip() == 'the university of sheffield':
                    v = 'university of sheffield'
                elif str(v).strip() == 'fbk':
                    v = 'fondazione bruno kessler'
                elif str(v).strip() == 'ucl':
                    v = 'university college london'
                elif str(v).strip() == 'university of genoa':
                    v = 'university of genova'

                if not aux_uni2.__contains__(v):
                    if str(v).strip() != 'nan':
                        aux_uni2.append(v)

    uni.append(aux_uni2)
cont = 0
media=[]
for u in uni:
    media.append(len(u))
    if len(u) > 1:
        cont += 1
        print u
print '#papers com paises diferentes'
print cont
print 'media'
print media
print '%.2f' % float((sum(media))/float(len(media)))