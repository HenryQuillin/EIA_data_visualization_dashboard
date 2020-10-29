from urllib.request import urlretrieve as retrieve
url = 'https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip'

retrieve(url, 'data')

'''
url = 'https://www.eia.gov/electricity/data/eia860/xls/eia8602019.zip'

def download_eia_data(eia_csv_url):
    response = request.urlopen(eia_csv_url)
    csv_data = response.read()
    csv_data_str = str(csv_data)
    print(csv_data_str)

download_eia_data(url)


r = requests.get(url, allow_redirects=True)
print(r.headers.get('content-type'))

open('2019_data', 'wb').write(r.content)

print('hello')
'''
