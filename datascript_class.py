import requests as req
from urllib.request import urlretrieve as retrieve
import zipfile
# import pandas as pd
# import numpy as np
import os
import shutil

class GenerationData(object):
    def __init__(self, user=None, msg=None):
        self.url = 'https://www.eia.gov'
        self.eia_2018_location = '/electricity/data/eia860/archive/xls/eia8602018.zip'
        self.user = user
        self.print_user(msg)
        return

    def print_user(self, msg=''):
        print(f'{msg} {self.user}')
        return

    # download zip from website
    def get_zip(self,url, zip_file_name):
        retrieve(url, zip_file_name)

    # extract zip
    def extract_zip(self, zip_to_be_extracted, file_name):
        with zipfile.ZipFile(zip_to_be_extracted, 'r') as zip_ref:
            zip_ref.extractall(file_name)

