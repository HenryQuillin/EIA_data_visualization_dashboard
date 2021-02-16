import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.ticker as ticker
import plotly.express as px


# API Key from EIA
api_key = '3c109e8bc5897c4015d86e77e699ebc6'


# PADD Names to Label Columns
# Change to whatever column labels you want to use.
PADD_NAMES = ['PADD 1','PADD 2','PADD 3','PADD 4','PADD 5']
# Enter all your Series IDs here separated by commas
PADD_KEY = ['PET.MCRRIP12.M',
'PET.MCRRIP22.M',
'PET.MCRRIP32.M',
'PET.MCRRIP42.M',
'PET.MCRRIP52.M']
# Initialize list - this is the final list that you will store all the data from the json pull. Then you will use this list to concat into a pandas dataframe. 
final_data = []
# Choose start and end dates
startDate = '2009-01-01'
endDate = '2021-01-01'

# Pull in data via EIA API
for i in range(len(PADD_KEY)):
    url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=' + PADD_KEY[i]
    r = requests.get(url)
    json_data = r.json()
    
    if r.status_code == 200:
        print('Success!')
    else:
        print('Error')
    
    df = pd.DataFrame(json_data.get('series')[0].get('data'),
                      columns = ['Date', PADD_NAMES[i]])
    df.set_index('Date', drop=True, inplace=True)
    final_data.append(df) 





# Combine all the data into one dataframe
final_df = pd.concat(final_data, axis=1)


# Create date as datetype datatype
final_df['Year'] = final_df.index.astype(str).str[:4]
final_df['Month'] = final_df.index.astype(str).str[4:]
final_df['Day'] = 1
final_df['Date'] = pd.to_datetime(final_df[['Year','Month','Day']])
final_df.set_index('Date',drop=True,inplace=True)
final_df.sort_index(inplace=True)
final_df = final_df[startDate:endDate]
final_df = final_df.iloc[:,:5]


fig = px.line(final_df, title='Net generation')
fig.show()