#This file calculate the total number of Tree in a province

#Import Packages
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#input the .csv file
input_file = "alberi-monumentali-sicilia.csv"
data = pd.read_csv(input_file)
df = pd.DataFrame(data, columns=['PROVINCIA', 'COMUNE','PROGR'])
# df = pd.DataFrame(data)

#Groupby, count and sortvalues
group_provincia = df.groupby('PROVINCIA') #Group the database by the "Provincia"
group_provincia = group_provincia['PROVINCIA'] #Convert DataFrameGroupScalar to SeriesGroupBy
group_provincia = group_provincia.count().sort_values(ascending= False) #Counting the total number of trees in a Provincia and sort the values 

#Create the lists of the province and obtain the list of the total number of trees 
provincia_list = group_provincia.index.to_list() # Obtain a list of the names of various province
total_number_list = group_provincia.values.tolist()

print(group_provincia)


plt.bar(provincia_list, total_number_list)

x = provincia_list
y = total_number_list

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i] + 0.2 ,y[i], ha = 'center')

addlabels(provincia_list, total_number_list)


plt.show()



