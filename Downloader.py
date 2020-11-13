import requests as req
import zipfile
import pandas as pd


web = 'https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip'


def download_file(url, filename):
    with req.get(url) as rq:
        with open(filename, 'wb') as file:
            file.write(rq.content)
download_file(web, 'general_data.zip')

def un_zip(new_file):
    zip_file = new_file
    with zipfile.ZipFile('general_data.zip', 'r') as zip_ref:
        zip_ref.extractall(zip_file)
un_zip('general_data_folder')

def data_frame():
    df = pd.read_excel (r'C:\Users\ramen\PycharmProjects\pythonProject\internship_repo\success_unzip\1___Utility_Y2019.xlsx')
    print(df)
data_frame()


