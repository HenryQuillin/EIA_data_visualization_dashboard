from urllib.request import urlretrieve as retrieve
import zipfile36 as zipfile
import pandas as pd

#download zip from website
def get_zip(url,zip_file_name):
    retrieve(url, zip_file_name)

#extract zip
def extract_zip(zip_to_be_extracted, file_name):
    with zipfile.ZipFile(zip_to_be_extracted, 'r') as zip_ref:
        zip_ref.extractall(file_name)

#download all zip files and extract them
def download_data(start_year, end_year):
    for year in range(start_year,end_year):
        year = str(year)
        looped_url = f'https://www.eia.gov/electricity/data/eia860/archive/xls/eia860{year}.zip'
        zip_name = year
        file_name = f'unzipped_{year}'
        get_zip(looped_url, zip_name)
        extract_zip(zip_name, file_name)

download_data(2002, 2019)
plant_df = pd.read_excel (r'C:\Users\henry\Desktop\Projects\internship_repo\unzipped_2018\2___Plant_Y2018.xlsx')
layout_df = pd.read_excel (r'C:\Users\henry\Desktop\Projects\internship_repo\unzipped_2018\LayoutY2018.xlsx')
print(plant_df.head(5))

