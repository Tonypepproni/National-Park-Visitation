import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

df=pd.read_csv('info/parks.csv')

my_list=df['name'].tolist()
print(my_list)

url='https://www.nps.gov/articles/000/historic-listing-of-nps-park-codes.htm'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text,'html.parser')

table=soup.find('table')
rows=table.find_all('tr')

parks={}



for row in rows[1:]:
    cells=row.find_all(['td','th'])
    if len(cells)>=2:
        name=cells[0].get_text(strip=True)
        code=cells[1].get_text(strip=True)
        if not code.startswith("See"):

            # Only include parks that are in your CSV
            if code in my_list:
                parks[code] = {
                    "name": name,
                    "code": code
                }

with open("info/parks_been.json",'w',encoding='utf-8') as f:
    json.dump(parks,f,indent=4)