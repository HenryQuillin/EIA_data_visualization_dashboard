import scipy as scipy
import pandas as pd
import numpy as np



def load_data(file, name1, name2, name3):
    gen_data = pd.read_excel(file, sheet_name=name1)
    wind_data = pd.read_excel(file, sheet_name=name2)
    mw_data = pd.read_excel(file, sheet_name=name3)
    return (gen_data, wind_data, mw_data);
gen_data, wind_data, mw_data = load_data("/Users/asherforman/PycharmProjects/Beginning-Commands/project_data_for_Asher.xlsx", 'gen_data', 'wind_data', 'mw_data')

data_1 = pd.merge(gen_data[['iso_name','gen_pw_label','station_code','distance_mi']], wind_data[['station_id','location','code','observation_date','hour','wind_speed_avg']],how="inner",left_on=['station_code'],right_on=['code'])
data_2 = pd.merge(data_1, mw_data, how="inner", left_on=['observation_date', 'hour', 'gen_pw_label'], right_on=['publishDate', 'publishHour', 'pwLabel'])
data_3 = data_2[['observation_date', 'hour', 'wind_speed_avg', 'pwGenMW']]

def create_wind_gen_dataset():

    gen_data, wind_data, mw_data = load_data("/Users/asherforman/PycharmProjects/Beginning-Commands/project_data_for_Asher.xlsx", 'gen_data', 'wind_data','mw_data')



    return(data_3)

def linear_regression():

    data =create_wind_gen_dataset()


    return(results)

if __name__ == '__main__':

    gen_data, wind_data, mw_data = load_data("/Users/asherforman/PycharmProjects/Beginning-Commands/project_data_for_Asher.xlsx", 'gen_data', 'wind_data', 'mw_data')

plt.scatter(data_5['wind_speed_avg'],data_5['pwGenMW'])

import matplotlib as plt
import matplotlib.pyplot as plt

plt.scatter(data_3['wind_speed_avg'],data_3['pwGenMW'])

data_4 = data_2[['observation_date', 'hour', 'wind_speed_avg', 'pwGenMW','pwLabel']]
data_4[:5]

data_5 = data_4[data_4['pwLabel']=='ADAMS_G ADAMS__1_UNIT']
plt.scatter(data_5['wind_speed_avg'],data_3['pwGenMW'])

plt.scatter(data_5['wind_speed_avg'],data_5['pwGenMW'])

import numpy as np
units = np.unique(data_4['pwLabel'])
plt.scatter(data_4.loc[data_4['pwLabel']==units[0], 'wind_speed_avg'],data_4.loc[data_4['pwLabel']==units[0],'pwGenMW'])


u=2; plt.scatter(data_4.loc[data_4['pwLabel']==units[u], 'wind_speed_avg'],data_4.loc[data_4['pwLabel']==units[u],'pwGenMW'])
u=3; plt.scatter(data_4.loc[data_4['pwLabel']==units[u], 'wind_speed_avg'],data_4.loc[data_4['pwLabel']==units[u],'pwGenMW'])
for u in range(4,5):
    plt.scatter(data_4.loc[data_4['pwLabel'] == units[u], 'wind_speed_avg'],
                data_4.loc[data_4['pwLabel'] == units[u], 'pwGenMW'])

from scipy import stats
import numpy as np
u=4
x = data_4.loc[data_4['pwLabel'] == units[u], 'wind_speed_avg']
y = data_4.loc[data_4['pwLabel'] == units[u], 'pwGenMW']
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)