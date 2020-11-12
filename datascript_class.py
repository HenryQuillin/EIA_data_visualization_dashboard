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


    # download zip from website
    def get_zip(self, year, zip_file_name):
        retrieve(f'{self.page_url}{self.eia860_location}{year}.zip', f'{zip_file_name}_{year}')

    # extract zip
    def extract_zip(self, zip_to_be_extracted, file_name):
        with zipfile.ZipFile(zip_to_be_extracted, 'r') as zip_ref:
            zip_ref.extractall(file_name)


    # def get_data(self, page_url, year): 

'''
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602018.zip
https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602017.zip
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602015.zip
https://www.eia.gov/electricity/data/eia860/archive/xls/eia8602011.zip
'''