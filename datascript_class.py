import requests as req
from urllib.request import urlretrieve as retrieve
import zipfile
import pandas as pd
from pathlib import Path
# import numpy as np
import os
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


    # download zip from website
    def get_zip(self, start_year, end_year, zip_name):
        for year in range(start_year, end_year):
            year = str(year)
            looped_url = f'{self.page_url}{self.eia860_location}{year}.zip'
            retrieve(looped_url, f'{zip_name}_{year}')

    # extract zip
    def extract_zip(self, start_year, end_year, zip_name):
        for year in range(start_year, end_year):
            year = str(year)
            with zipfile.ZipFile(f'{zip_name}_{year}', 'r') as zip_ref:
                zip_ref.extractall(f'{zip_name}_{year}_unzipped')

    # download zip and extract zip 
    def get_data(self, start_year, end_year, zip_name): 
        self.get_zip(start_year, end_year, zip_name)
        self.extract_zip(start_year, end_year, zip_name)


    def load_data(self, year):
        file_location = self.cwd / f"EIA_data_2017_unzipped/2___Plant_Y{year}.xlsx"
        self.df = pd.read_excel(file_location, skiprows=1)
        self.df = self.df[['Plant Name', 'Latitude', 'Longitude']]

        print(self.df.head(3))

    def save_data(self, year, file_type='csv'):
        new_header = self.df.iloc[0]  # grab the first row for the header
        self.df = self.df[1:]  # take the data less the header row
        self.df.columns = new_header  # set the header row as the df header
        #self.df.drop(self.df.columns[[2,4,5,6,7,8][11:]], axis=1)
        if file_type == 'json' or file_type == 'JSON':
            self.df.to_json(self.cwd / f"df_csv/df_{year}.json")
        else:
            self.df.to_csv(self.cwd / f"df_csv/df_{year}.csv")
        print(self.df.head(10))
        # df[[


if __name__ == 'main':
    pass
d = GetData()
#d.get_data(2017, 2018, 'EIA_data')
d.load_data('2017')
d.save_data('2017', 'csv')

