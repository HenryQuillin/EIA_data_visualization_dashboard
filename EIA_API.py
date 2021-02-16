import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.ticker as ticker
import plotly.express as px


# API Key from EIA
api_key = '3c109e8bc5897c4015d86e77e699ebc6'



# column labels 
PADD_NAMES = ['NATURAL GAS','COAL','PETROLIUM']
# Enter all your Series IDs here separated by commas
PADD_KEY = ['EMISS.CO2-TOTV-TT-NG-US.A','EMISS.CO2-TOTV-TT-CO-US.A','EMISS.CO2-TOTV-TT-PE-US.A']
#list to concat into a pandas dataframe
final_data = []


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
final_df = final_df.sort_index(ascending=True)



print(final_df.head())
fig = px.line(final_df,title='Total carbon dioxide emissions in the United States (million metric tons CO2)')
fig.show()