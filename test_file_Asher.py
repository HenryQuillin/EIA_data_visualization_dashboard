import pandas as pd

print(
    r'''
    This is henry making a change 
                                  .-.
     (___________________________()6 `-,
     (   ______________________   /''"`
     //\\                      //\\
     "" ""                     "" ""
    '''
)

data_frame = pd.DataFrame(
    {'Countires': ['Poland', 'Mexico', 'Iceland'],
    'Cities': ['Warsaw', 'Mexico City', 'Reykjavik'],}

)
print(data_frame)

df = pd.read_excel (r'C:\Users\ramen\Downloads\InternshipData.xlsx')
print(df)

electricity = pd.read_excel (r'C:\Users\ramen\Downloads\eia8602019\1___Utility_Y2019.xlsx')
print(electricity)

