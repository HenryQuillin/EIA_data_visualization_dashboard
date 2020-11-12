import requests as req
from urllib.request import urlretrieve as retrieve
import zipfile
# import pandas as pd
# import numpy as np
# import os
# import shutil

class GetData(object):
    def __init__(self, page_url='https://www.eia.gov/electricity/data/eia860/'):
        self.page_url = page_url
        self.eia860_location = 'archive/xls/eia860'
    '''
    def loop_url(start_year, end_year):
        for year in range(start_year, end_year):
            year = str(year)
            looped_url = f'{self.page_url}{self.eia860_location}{year}.zip'
            zip_name = year
            file_name = f'unzipped_{year}'
            get_zip(looped_url, zip_name)

    '''
    # download zip from website
    def get_zip(self, start_year, end_year, zip_name):
        for year in range(start_year, end_year):
            year = str(year)
            looped_url = f'{self.page_url}{self.eia860_location}{year}.zip'
            retrieve(looped_url, f'{zip_name}_{year}')

    # extract zip
    def extract_zip(self, start_year, end_year, zip_name, file_name):
        for year in range(start_year, end_year):
            year = str(year)
            with zipfile.ZipFile(f'{zip_name}_{year}', 'r') as zip_ref:
                zip_ref.extractall(f'{file_name}_{year}')

    def get_data(self, page_url): 
        pass

d = GetData()
#d.get_zip(2015,2018, 'testing')
d.extract_zip(2015,2018, 'testing','testing_unzipped')
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