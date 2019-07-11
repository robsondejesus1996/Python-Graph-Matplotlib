import numpy as np
import matplotlib.pyplot as plt

#https://matplotlib.org/examples/api/barchart_demo.html

N = 11
#valores
fv = [2,	1,	3,	3,	0,	2,	0,	2,	3,	1]

#percentuais
up = np.array([91.67,	87.50,	86.00,	84.31,	95.74,	76.09,	95.00,	93.48,	66.67,	91.89,	87.72])
ip = np.array([0,	5,	8,	5.88,	4.26,	6.52,	2.50,	0,	0,	5.41,	4.26])
fp = np.array([8.33,	2.5,	6,	5.88,	0,	4.35,	0,	4.35,	16.7,	2.7,	4.26])
uip = (0,	5,	0,	3.92,	0,	10.87,	2.50,	2.17,	11.11,	0.00,	3.26)
ufp = (0, 0,	0,	0,	0,	2.17,	0,	0,	5.56,	0,	0.50)


ind = np.arange(N)    # the x locations for the groups
width = 0.6       # the width of the bars

fig, ax = plt.subplots()
uf = ax.bar(ind, ufp, width, bottom=up+ip+fp+uip, color='c')
ui = ax.bar(ind, uip, width, bottom=up+ip+fp, color='gold')
f = ax.bar(ind, fp, width, bottom=up+ip, color='yellowgreen')
i = ax.bar(ind, ip, width, bottom=up, color='tomato')
u = ax.bar(ind, up, width, color='royalblue')

ax.set_ylabel('%')
plt.xticks(ind, ('2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', 'All'))

ax.legend((u[0], i[0], f[0], ui[0], uf[0]), ('University', 'Industry', 'Foundation', 'University-Industry', 'University-Foundation'), loc=4)
# ax.legend((u[0], i[0], f[0]), ('University', 'Industry', 'Foundation'), loc=4)
# # Text on the top of each barplot
# def autolabel_men(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     i = 0
#     for barra in rects:
#         height = barra.get_height()
#         ax.text(barra.get_x() + barra.get_width()/2., 40,
#                 '%d' % int(height) + '%\n' +
#                 '(%d)' % int(val_men[i]),
#                 ha='center', va='bottom')
#         i += 1
#
# def autolabel_women(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     i = 0
#     for barra in rects:
#         height = barra.get_height()
#
#         ax.text(barra.get_x() + barra.get_width()/2., 91.5,
#                 '%d' % int(height) + '%\n' +
#                 '(%d)' % int(val_women[i]),
#                 ha='center', va='bottom')
#         i += 1
# # Adjust the margins
# # plt.subplots_adjust(bottom=0.2, top=0.98)
#
#
#
# autolabel_men(rects1)
# autolabel_women(rects2)

# plt.show()
plt.savefig('industry.png')
plt.close()