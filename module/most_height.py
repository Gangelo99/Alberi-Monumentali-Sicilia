#This file find the most height tree present in the database

from .input_database import pd, data
max = 5 #MAx number of trees

#Input the CSV file
df = pd.DataFrame(data, columns = ['COMUNE', 'ALTEZZA (m)','SPECIE NOME VOLGARE'])

#Group by COMUNE and search the highest value of the trees present in each city, sorting them
most_height = df.groupby('COMUNE').max().sort_values(by= ['ALTEZZA (m)'],ascending= False)

provincia_list = most_height.index.to_list() #Get a list of the names of various province
high_list = most_height['ALTEZZA (m)'].values.tolist() #Get a list of the height of trees
name_trees_list = most_height['SPECIE NOME VOLGARE'].values.tolist() #Get the name of the trees

provincia_list = provincia_list[:max]
high_list = high_list[:max]
name_trees_list = name_trees_list[:max]

max_length = 13 #Max length of text for represent histogram

#This for cycle slice the names of the trees and the names of city
for i in range(max):
    if (len(provincia_list[i]) > max_length - 2) and (len(name_trees_list[i]) > max_length):
        name_trees_list[i] = name_trees_list[i][:max_length] + "." + " (" + provincia_list[i][:max_length] + "." + ") "
    
    elif len(provincia_list[i]) > max_length:
        name_trees_list[i] = name_trees_list[i] + " (" + provincia_list[i][:max_length] + "." + ") "
    
    elif len(name_trees_list[i]) > max_length:
        name_trees_list[i] = name_trees_list[i][:max_length] + "." + " (" + provincia_list[i] + ") "
    
    else:
        name_trees_list[i] = name_trees_list[i] + " (" + provincia_list[i] + ") "