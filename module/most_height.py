#This file find the most height tree present in the database

from input_database import pd, data

df = pd.DataFrame(data, columns = ['COMUNE', 'ALTEZZA (m)','SPECIE NOME VOLGARE'])

# most_height = df.groupby('COMUNE')
# most_height = most_height['ALTEZZA (m)']
# most_height = most_height.max()

# print(most_height)

most_height = df.groupby('COMUNE').max().sort_values(by= ['ALTEZZA (m)'],ascending= False)

print(most_height)