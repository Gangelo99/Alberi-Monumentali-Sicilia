### This file create the histogram with the first 10 highest trees

#Import packages
from module.most_height import provincia_list, high_list, name_trees_list
from module.font import font_labels, font_title
import matplotlib.pyplot as plt

plt.bar(name_trees_list,high_list)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i] + 0.2 ,y[i], ha = 'center')


addlabels(provincia_list, high_list)
plt.xlabel('TIPOLOGIA ALBERO E COMUNE', fontdict=font_labels)
plt.ylabel('ALTEZZA (metri)', fontdict=font_labels)

# plt.savefig("histogram_2.jpg") #Uncomment this to save the histogram in jpg
plt.title('GLI ALBERI MONUMETALI PRESENTI\nIN SICILIA PIÙ ALTI', fontdict= font_title)

plt.show()