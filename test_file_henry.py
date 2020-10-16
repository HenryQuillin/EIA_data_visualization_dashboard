print('hello world')
print("this is Henry's code")
print("Change Test")
print("Asher made a change")

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.head(3))

#Read column
print(df.columns)

# Read each column
print(df['Name'][0:4])