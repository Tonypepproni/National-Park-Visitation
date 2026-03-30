import pandas as pd
import json

with open('info/parks.json','r') as f:
    raw_data = json.load(f)

df=pd.DataFrame(raw_data['map'])

print(df.head(10))