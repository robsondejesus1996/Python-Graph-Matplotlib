import numpy as np
import matplotlib.pyplot as plt

#https://matplotlib.org/examples/api/barchart_demo.html

N = 10
men_means = (91.7, 82.5, 84, 90.2, 70.2, 87, 85, 80.4, 83.3, 81.1)
women_means = (8.3, 17.5, 16, 9.8, 29.8, 13, 15, 19.6, 16.7, 18.9)

ind = np.arange(N)    # the x locations for the groups
width = 0.9       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='lightblue')
rects2 = ax.bar(ind, women_means, width, bottom=men_means, color=(1.0,0.5,0.62))#'hotpink')

ax.set_ylabel('%')
plt.xticks(ind, ('2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'))



val_men = [22, 33, 42, 46, 33, 40, 32, 37, 15, 30]

val_women = [2, 7, 8, 5, 14, 6, 8, 9, 3, 7]


ax.legend((rects2[0], rects1[0]), ('Female', 'Male'), loc=4)

# Text on the top of each barplot
def autolabel_men(rects):
    """
    Attach a text label above each bar displaying its height
    """
    i = 0
    for barra in rects:
        height = barra.get_height()
        print height
        ax.text(barra.get_x() + barra.get_width()/2., 40,
                '%.1f' % float(height) + '%\n' +
                '(%d)' % int(val_men[i]),
                ha='center', va='bottom')
        i += 1

def autolabel_women(rects):
    """
    Attach a text label above each bar displaying its height
    """
    i = 0
    for barra in rects:
        height = barra.get_height()

        ax.text(barra.get_x() + barra.get_width()/2., 91.5,
                '%.1f' % float(height) + '%\n' +
                '(%d)' % int(val_women[i]),
                ha='center', va='bottom')
        i += 1
# Adjust the margins
# plt.subplots_adjust(bottom=0.2, top=0.98)

autolabel_men(rects1)
autolabel_women(rects2)

# plt.show()
plt.savefig('gender.png')
plt.close()