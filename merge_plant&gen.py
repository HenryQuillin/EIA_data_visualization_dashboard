import pandas as pd 

#create plant datafram 
plant_df = pd.read_excel('C:\\Users\\henry\\Desktop\\Projects\\internship_repo\\data\\EIA_2018_unzipped\\2___Plant_Y2018.xlsx', nrows=50, skiprows=1)
plant_df = plant_df[['Utility ID','Plant Code', 'Plant Name', 'Latitude', 'Longitude', 'Transmission or Distribution System Owner']]
print(plant_df.head())

#create generator dataframe
gen_df = pd.read_excel('C:\\Users\\henry\\Desktop\\Projects\\internship_repo\\data\\EIA_2018_unzipped\\3_1_Generator_Y2018.xlsx', nrows=50, skiprows=1)
gen_df = gen_df[['Utility ID','Plant Code', 'Plant Name', 'Technology', 'Prime Mover', 'Operating Year',]]
print(gen_df.head())

#merge both dataframes on 'plant code' 
merged_df = pd.merge(gen_df, plant_df)
print('---------------')
print(merged_df.head())



