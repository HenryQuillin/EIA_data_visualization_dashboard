import pandas as pd
print('hello world')
print("this is Henry's code")
print("Change Test")
print("Asher made a change")



df = pd.read_csv('pokemon_data.csv')

print(df.head(3))

#Read column
print(df.columns)

# Read each column
print(df[['Name','Type 1','HP']][0:4])

# Print specific location
print(df.iloc[1])

# Iterate through every row
for index,row in df.iterrows():
    print(index, row['Name'])