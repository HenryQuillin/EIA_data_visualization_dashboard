import requests as req
import zipfile


web = 'https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip'


def download_file():
    with req.get('https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip') as rq:
        with open('data.zip', 'wb') as file:
            file.write(rq.content)
# download_file()

def un_zip():
    zip_file = 'success_unzip'
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall(zip_file)
# un_zip()

