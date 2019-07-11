

import matplotlib.pyplot as plt
import re
import csv
import pandas as pd
from numpy import sort


path_source = 'D:/OneDrive/OneDrive - UDESC Universidade do Estado de Santa Catarina/doutorado/artigos/sbse/ssbse/SSBSE2019b.csv'
path_data = 'D:/OneDrive/OneDrive - UDESC Universidade do Estado de Santa Catarina/doutorado/artigos/sbse/ssbse/artigo/data/'

df = pd.read_csv(path_source, usecols=['Year', 'Author 1', 'Country 1', 'City 1', 'University 1', 'Department 1', 'Author 2', 'Country 2', 'City 2', 'University 2', 'Department 2', 'Author 3', 'Country 3', 'City 3', 'University 3', 'Department 3', 'Author 4', 'Country 4', 'City 4', 'University 4', 'Department  4', 'Author 5', 'Country 5', 'City 5', 'University 5', 'Department  5', 'Author 6', 'Country 6', 'City 6', 'University 6', 'Department 6', 'Author 7', 'Country 7', 'City 7', 'University 7', 'Department 7']) #, encoding="ISO-8859-1"


# def split_sentences(col, equiv, filename):
#     auxdf = pd.read_csv(path_source, usecols=[col]).dropna()
#
#     rows = ''
#     dic = {}
#
#     for k in auxdf.get_values():
#         if k[0]:
#             rows += str(k[0].lower().replace(' and ', ', ')) + ', '
#
#     splitted = re.split(r'[.,;]', kw)
#     for k in splitted:
#         if k.strip() != '':
#             newk = k.lower().strip()
#             # check equivalents keywords
#             if newk in equiv:
#                 newk = equiv[newk]
#             if newk in dic:
#                 dic[newk] += 1
#             else:
#                 dic[newk] = 1
#     sorted_dic = sorted(dic)
#     with open(path_data + filename + '.csv', 'wb') as csv_file:
#         writer = csv.writer(csv_file)
#         for k in sorted_dic:
#             writer.writerow([k, dic[k]])
#     #########################################################


# #Years
# ydf1 = df.groupby("Year")["Year"].count().reset_index(name="count")
# ydf1.to_csv(path_data + "years.csv")

########################################################################################################################

#Universidades
unidic = {}

uniequiv = {
    'university of sheffield': 'the university of sheffield',
    'fbk': 'fondazione bruno kessler',
    'ucl': 'university college london',
    'university of genoa': 'university of genova',
}


for c in range(1, 6, 1):
    col = 'University {}'.format(c)
    adf1 = df.groupby(col)[col].count().reset_index(name="count")
    for a, b in adf1.itertuples(index=False):
        if a.strip() != '':
            values = a.split(';')
            for n in values:
                newk = n.lower().strip()
                # check equivalents keywords
                if newk in uniequiv:
                    newk = uniequiv[newk]
                if newk in unidic:
                    unidic[newk] += 1
                else:
                    unidic[newk] = 1

unilist = []
for k in unidic:
    unilist.append(k)

# for k in unilist:
#     print k

# print '####################333'

with open(path_data + 'University-nodes.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "label"])
    for v in unilist:
       writer.writerow([unilist.index(v), v])

### collaboration
uni = []
for i in range(0, len(df.index)):
    aux_uni = sort([df.iloc[i, 4], df.iloc[i, 9], df.iloc[i, 14], df.iloc[i, 19], df.iloc[i, 24], df.iloc[i, 29], df.iloc[i, 34]])
    ano = df.iloc[i, 35]
    # print aux_uni
    print ano
    aux_uni2 = []
    for j in range(0, 7):
        # print type(aux_uni[j])
        if aux_uni[j] != 'nan':
            values_j = str(aux_uni[j]).split(';')
            for val_j in values_j:
                for k in range(j, 7):
                    if str(aux_uni[k]).strip() != 'nan':
                        values_k = str(aux_uni[k]).split(';')
                        for val_k in values_k:
                            if val_j != val_k:
                                # //checar se ja nao tem
                                col = [val_j, val_k]
                                if not aux_uni2.__contains__(col):
                                    aux_uni2.append(col)

    # print unidic
    for u in aux_uni2:
        # print u[0]
        cont = 0
        cont1 = None
        cont2 = None
        # print u[0]
        # print '-----'
        for v in unilist:
            # print v

            if v == u[0].lower().strip():
                cont1 = cont
            elif v == u[1].lower().strip():
                cont2 = cont
            cont += 1

        if cont1 != None and cont2 != None:
            new = [cont1, cont2]
            uni.append([ano, new])
print uni

#arestas
with open(path_data + 'University-arestas.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["source", "target"])
    for k in uni:
       writer.writerow(k)

#######################################################################################################################
# AUTORES

autdic = {}
autdic_uni = {}
autequiv = {
}

aut = []
for i in range(0, len(df.index)):
    for j in range(0, 30, 5):
        # aux_uni = sort([df.iloc[i, 0], df.iloc[i, 5], df.iloc[i, 10], df.iloc[i, 15], df.iloc[i, 20], df.iloc[i, 25], df.iloc[i, 30]])
        newk = str(df.iloc[i, j]).lower().strip()
        # check equivalents keywords
        if newk in autequiv:
            newk = autequiv[newk]
        if newk in autdic:
            autdic[newk] += 1
        else:
            autdic[newk] = 1
        autdic_uni[newk] = df.iloc[i, j+4]

autlist = []
for k in autdic:
    autlist.append(k)

# for k in autlist:
#     print k

# print '####################333'

with open(path_data + 'Author-nodes.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "label"])
    for v in autlist:
       writer.writerow([autlist.index(v), v])

### collaboration
aut = []
for i in range(0, len(df.index)):
    aux_uni = sort([df.iloc[i, 0], df.iloc[i, 5], df.iloc[i, 10], df.iloc[i, 15], df.iloc[i, 20], df.iloc[i, 25], df.iloc[i, 30]])
    # print aux_uni
    aux_uni2 = []
    for j in range(0, 7):
        # print type(aux_uni[j])
        if aux_uni[j] != 'nan':
            values_j = str(aux_uni[j]).split(';')
            for val_j in values_j:
                for k in range(j, 7):
                    if str(aux_uni[k]).strip() != 'nan':
                        values_k = str(aux_uni[k]).split(';')
                        for val_k in values_k:
                            if val_j != val_k:
                                # //checar se ja nao tem
                                col = [val_j, val_k]
                                if not aux_uni2.__contains__(col):
                                    aux_uni2.append(col)

    # print autdic
    for u in aux_uni2:
        # print u[0]
        cont = 0
        cont1 = None
        cont2 = None
        # print u[0]
        # print '-----'
        for v in autlist:
            # print v

            if v == u[0].lower().strip():
                cont1 = cont
            elif v == u[1].lower().strip():
                cont2 = cont
            cont += 1

        if cont1 != None and cont2 != None:
            new = [cont1, cont2]
            aut.append(new)
# print aut

#arestas
with open(path_data + 'Authors-arestas.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["source", "target"])
    for k in aut:
       writer.writerow(k)




# #Authors
# autdic = {}
# autequiv = {
#
# }
#
# for c in range(1, 6, 1):
#     col = "'Author " + str(c)
#     adf1 = df.groupby(col)[col].count().reset_index(name="count")
#     for a, b in adf1.itertuples(index=False):
#         if a.strip() != '':
#             newk = a.lower().strip()
#             # check equivalents keywords
#             if newk in autequiv:
#                 newk = autequiv[newk]
#             if newk in autdic:
#                 autdic[newk] += 1
#             else:
#                 autdic[newk] = 1
#
# with open(path_data + 'authors.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Author", "count"])
#     for k in autdic:
#        writer.writerow([k, autdic[k]])
#
# ################################################################################################# COUNTRY
# #Country
# coudic = {}
# couequiv = {
#
# }
#
# for c in range(1, 6, 1):
#     col = "Country " + str(c)
#     adf1 = df.groupby(col)[col].count().reset_index(name="count")
#     for a, b in adf1.itertuples(index=False):
#         if a.strip() != '':
#             newk = a.lower().strip()
#             # check equivalents keywords
#             if newk in couequiv:
#                 newk = couequiv[newk]
#             if newk in coudic:
#                 coudic[newk] += 1
#             else:
#                 coudic[newk] = 1
#
# # print (coudic)
# with open(path_data + 'countries.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Country", "count"])
#     for k in coudic:
#        writer.writerow([k, coudic[k]])
#
# ######################################################### - keywords
#
# kdf = pd.read_csv(path_source, usecols=['Keywords']).dropna()
#
# kw = ''
# kwdic = {}
# kwequiv ={
#     'search based software engineering': 'search-based software engineering',
#     'search based test data generation': 'search-based test data generation',
#     'next release': 'next release problem'
# }
#
# for k in kdf.get_values():
#     if k[0]:
#         kw += str(k[0].lower().replace(' and ', ', ')) + ', '
#
# keywords = re.split(r'[.,;]', kw)
# for k in keywords:
#     if k.strip() != '':
#         newk = k.lower().strip()
#         # check equivalents keywords
#         if newk in kwequiv:
#             newk = kwequiv[newk]
#         if newk in kwdic:
#             kwdic[newk] += 1
#         else:
#             kwdic[newk] = 1
# sorted_kwdic = sorted(kwdic)
# with open(path_data + 'keywords.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for k in sorted_kwdic:
#        writer.writerow([k, kwdic[k]])
# #########################################################
#
#
# #ES Area
# ydf1 = df.groupby("ES Area")["ES Area"].count().reset_index(name="count")
# ydf1.to_csv(path_data + "es_area.csv")
#
# # Task
# ydf1 = df.groupby("Task")["Task"].count().reset_index(name="count")
# ydf1.to_csv(path_data + "task.csv")
#
# # IC Techniques
# #########################################################
#
# ictdf = pd.read_csv(path_source, usecols=['IC Techniques']).dropna()
#
# ict = ''
# ictdic = {}
# ictequiv ={
#     'search based software engineering': 'search-based software engineering',
#     'search based test data generation': 'search-based test data generation',
#     'next release': 'next release problem'
# }
#
# for k in ictdf.get_values():
#     if k[0]:
#         ict += str(k[0].lower().replace(' and ', ', ')) + ', '
#
# ictechniques = re.split(r'[.,;]', ict)
# for k in ictechniques:
#     if k.strip() != '':
#         newk = k.lower().strip()
#         # check equivalents keywords
#         if newk in ictequiv:
#             newk = ictequiv[newk]
#         if newk in ictdic:
#             ictdic[newk] += 1
#         else:
#             ictdic[newk] = 1
# sorted_ictdic = sorted(ictdic)
# with open(path_data + 'ic_techniques.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for k in sorted_ictdic:
#        writer.writerow([k, ictdic[k]])
# #########################################################
#
# # Statistical Test
# #########################################################
#
# stdf = pd.read_csv(path_source, usecols=['Statistical Test']).dropna()
#
# st = ''
# stdic = {}
# stequiv ={
#     'search based software engineering': 'search-based software engineering',
#     'search based test data generation': 'search-based test data generation',
#     'next release': 'next release problem'
# }
#
# for k in stdf.get_values():
#     if k[0]:
#         st += str(k[0].lower().replace(' and ', ', ')) + ', '
#
# st = re.split(r'[.,;]', ict)
# for k in ictechniques:
#     if k.strip() != '':
#         newk = k.lower().strip()
#         # check equivalents keywords
#         if newk in ictequiv:
#             newk = ictequiv[newk]
#         if newk in ictdic:
#             ictdic[newk] += 1
#         else:
#             ictdic[newk] = 1
# sorted_ictdic = sorted(ictdic)
# with open(path_data + 'statistical_test.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for k in sorted_ictdic:
#        writer.writerow([k, ictdic[k]])
# #########################################################
#
#
# # Quality Indicators
# ydf1 = df.groupby("Quality Indicators")["Quality Indicators"].count().reset_index(name="count")
# ydf1.to_csv(path_data + "quality_indicators.csv")
#
# # Case Studies
# ydf1 = df.groupby("Case Studies")["Case Studies"].count().reset_index(name="count")
# ydf1.to_csv(path_data + "case_studies.csv")
#
# # Artifact
# ydf1 = df.groupby("Artifact")["Artifact"].count().reset_index(name="count")
# ydf1.to_csv(path_data + "artifact.csv")








# print('Time spent online per web site, per year')
# print(df.groupby([df.ts.dt.year, 'site']).agg({'duration': 'sum'}))




# # calculating stats
# stats = df.groupby([df.ts.dt.year, 'Year'], sort=True)['userid'] /
#           .count() /
#           .reset_index() /
#           .rename(columns={'userid':'visits'}) /
#
#
# stats = stats.set_index(stats.ts.astype(str) + ': ' + stats.site) /
#              .drop(['ts','site'], axis=1)

# # plot part
# fig = plt.figure(figsize=(16,9))
# ax = fig.add_subplot(111)
#
# title = 'site statistics (visitors)'
#
# stats.plot(kind='barh', ax=ax, title=title, color=['grey'], legend=None)
#
# [ax.annotate(str(visits), (stats.values.max()/2, i))
#  for i, visits in enumerate(stats['visits'].tolist())]
#
# plt.show()
# fig.savefig('stats.png',dpi=100,bbox='Tight')