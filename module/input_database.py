import pandas as pd

input_file = "../database/alberi-monumentali-sicilia.csv"
data = pd.read_csv(input_file)

data['ALTEZZA (m)'] = data['ALTEZZA (m)'].astype(int) #Convert the ALTEZZA column from string to int

# check_type = data.dtypes
# print(check_type)