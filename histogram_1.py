# This file create the histogram with the total number of trees present in every province

#Import packages
from module.sum_trees_province import provincia_list, total_number_list
from module.font import font_labels, font_title
# import matplotlib
import matplotlib.pyplot as plt


plt.bar(provincia_list, total_number_list)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i] + 0.2 ,y[i], ha = 'center')


addlabels(provincia_list, total_number_list)
plt.xlabel('COMUNI', fontdict=font_labels)
plt.ylabel('TOTALE ALBERI', fontdict=font_labels)
plt.title('TOTALE DI ALBERI MONUMENTALI\n PRESENTI NELLE VARIE PROVINCE', fontdict= font_title)

plt.show()



