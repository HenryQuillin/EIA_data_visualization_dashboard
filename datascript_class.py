import requests as req
from urllib.request import urlretrieve as retrieve
import zipfile
import pandas as pd
from pathlib import Path
import numpy as np
import os
import plotly.express as px
import dash
# import shutil

class GetData(object):
    def __init__(self, page_url='https://www.eia.gov/electricity/data/eia860/', working_directory=None):
        self.page_url = page_url
        self.eia860_location = 'archive/xls/eia860'
        if working_directory is None:
            self.cwd = Path(os.getcwd())
        else:
            self.cwd = working_directory
        self.df = None
        self.file_name = 'EIA'



    # download zip from website
    def get_zip(self, start_year, end_year, zip_name):
        for year in range(start_year, end_year):
            year = str(year)
            looped_url = f'{self.page_url}{self.eia860_location}{year}.zip'
            with req.get(looped_url) as rq:
                with open(f'data/{zip_name}_{year}', 'wb') as file:
                    file.write(rq.content)


    # extract zip
    def extract_zip(self, start_year, end_year, zip_name):
        self.file_name = zip_name
        for year in range(start_year, end_year):
            year = str(year)
            with zipfile.ZipFile(f'data/{self.file_name}_{year}', 'r') as zip_ref:
                zip_ref.extractall(f'data/{self.file_name}_{year}_unzipped')

    # download zip and extract zip 
    def get_data(self, start_year, end_year, zip_name='EIA'): 
        self.file_name = zip_name
        self.get_zip(start_year, end_year, self.file_name)
        self.extract_zip(start_year, end_year, self.file_name)


    def load_data(self, start_year, end_year):
        for year in range(start_year, end_year):
            file_location = self.cwd / 'data' / f"{self.file_name}_{year}_unzipped/2___Plant_Y{year}.xlsx"
            self.df = pd.read_excel(file_location, skiprows=1)

            self.df = self.df[['Plant Name', 'Latitude', 'Longitude']]
            #self.df = self.df[['Plant Name','Longitude','Latitude']]
            self.df = self.df.set_index('Plant Name')

    def save_data(self, start_year, end_year, file_type='csv'):
        for year in range(start_year, end_year):
            if file_type == 'json' or file_type == 'JSON':
                self.df.to_json(self.cwd / 'data' f"df_{year}.json")
            else:
                self.df.to_csv(self.cwd / 'data' / f"df_{year}.csv")

    # Puts it all together 
    def get_data_to_csv(self, start_year, end_year, file_name='EIA', file_type='csv'):
        if os.path.isfile(self.cwd / 'data') == True: 
            os.mkdir(self.cwd / 'data') 
        d.get_data(start_year,end_year,file_name)
        d.load_data(start_year,end_year)
        d.save_data(start_year,end_year,file_type)



if __name__ == 'main':
    pass

d = GetData()
d.get_data(2001,2020)

'''
plotly_data = pd.read_csv(d.cwd / 'data' / 'df_2018.csv')

fig = px.scatter_mapbox(plotly_data, lat="Latitude", lon="Longitude", hover_name="Plant Name", color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
 '''
'''
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
'''
# testing 
