import requests as req
import zipfile
import pandas as pd

web = 'https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip'

class DataSnatch(object):

    def __init__(self, url, filename, new_file, dataframe, filetype):
        self.url = url
        self.filename = filename
        self.new_file = new_file
        self.dataframe = dataframe
        self.filetype = filetype

    #Method for downloading the zipfile off the website
    def download(self):
        with req.get(self.url) as rq:
            with open(self.filename, 'wb') as file:
                file.write(rq.content)

    #Method for unzipping the downloaded file
    def un_zip(self):
        with zipfile.ZipFile(self.filename, 'r') as zip_ref:
            zip_ref.extractall(self.new_file)

    #Method for loading the data needed into a dataframe
    def load_data(self):
        self.dataframe = pd.read_excel(r'C:\Users\ramen\PycharmProjects\pythonProject\internship_repo\new_zip\2___Plant_Y2019.xlsx', skiprows=1)
        self.dataframe = self.dataframe[['Plant Name', 'Latitude', 'Longitude']]

    #Method for saving the necessary components of the data into a JSON or CSV file.
    def save_data(self):
        if self.filetype == 'JSON':
            self.dataframe.to_json(r'C:\Users\ramen\Desktop\2___Plant_Y2019.json')
        if self.filetype == 'csv':
            self.dataframe.to_csv(r'C:\Users\ramen\Desktop\2___Plant_Y2019.csv')
data = DataSnatch(web, 'general_data.zip', 'new_zip', 'df', 'csv')
# data.download()
# data.un_zip()
# data.load_data()
data.save_data()

