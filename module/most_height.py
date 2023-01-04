#This file find the most height tree present in the database

from .input_database import pd, data

df = pd.DataFrame(data, columns = ['COMUNE', 'ALTEZZA (m)','SPECIE NOME VOLGARE'])

most_height = df.groupby('COMUNE').max().sort_values(by= ['ALTEZZA (m)'],ascending= False)

provincia_list = most_height.index.to_list() #Obtain a list of the names of various province
high_list = most_height['ALTEZZA (m)'].values.tolist()
name_trees_list = most_height['SPECIE NOME VOLGARE'].values.tolist()

# print(most_height)

# print("LISTA ROBE:\n")
# print(provincia_list)

# print("LISTA ROBE:\n")
# print(high_list)

# print("LISTA ROBE:\n")
# print(name_trees_list)