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
        self.df = pd.read_excel(file_location)

        print(self.df.head(3))

    def save_data(self, year, file_type='csv'):
        self.df.to_csv(self.cwd / f"df_csv/df_{year}.{file_type}")

        pass


if __name__ == 'main':
    pass
d = GetData()
#d.get_data(2017, 2018, 'EIA_data')
d.load_data('2017')
d.save_data('2017')

