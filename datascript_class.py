import requests as req
from urllib.request import urlretrieve as retrieve
import zipfile
# import pandas as pd
# import numpy as np
import os
# import shutil

class GetData(object):
    def __init__(self, page_url='https://www.eia.gov/electricity/data/eia860/', working_directory=None):
        self.page_url = page_url
        self.eia860_location = 'archive/xls/eia860'
        if working_directory is None:
            self.cwd = os.getcwd()
        else:
            self.cwd = working_directory


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


if __name__ == 'main':
    d = GetData()
    d.get_data(2014, 2015, 'EIA_data')


'''
Initialize with page_url 
Get zip method that uses page url and year 
Extract_zip method that inputs the file to be unzipped and the file name 
Get data that inputs year start and year end and file name

'''
'''
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602018.zip
https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602017.zip
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602015.zip
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602011.zip
'''