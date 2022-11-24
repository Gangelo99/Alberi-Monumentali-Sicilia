#This file calculate the total number of Tree in a province

###Import Packages
import pandas as pd

###Input the .csv file
input_file = "alberi-monumentali-sicilia.csv"
data = pd.read_csv(input_file)
df = pd.DataFrame(data, columns=['PROVINCIA', 'COMUNE', 'PROGR'])

### Groupby, count and sortvalues
group_provincia = df.groupby('PROVINCIA') #Group the database by the "Provincia"
group_provincia = group_provincia['PROVINCIA'] #Convert DataFrameGroupScalar to SeriesGroupBy
group_provincia = group_provincia.count().sort_values(ascending= False) #Counting the total number of trees in a Provincia and sort the values 

### Create the lists of the province and obtain the list of the total number of trees 
global provincia_list
provincia_list = group_provincia.index.to_list() # Obtain a list of the names of various province

global total_number_list
total_number_list = group_provincia.values.tolist() #Obtain the list of the sum of the trees present in each province
