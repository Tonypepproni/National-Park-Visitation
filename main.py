import pandas as pd
import folium
import random

from makers import line,icon
from mapObj import park, trip

df=pd.read_csv('info/parks.csv')
sites={}
trips={}
in_n_out=[]
colors=['red','blue','green','purple','pink','darkred','orange']
npfg=folium.FeatureGroup(name='National parks',show=True)
littlefg=folium.FeatureGroup(name="'small' parks",show=True)
inoutfg=folium.FeatureGroup(name='In n Out Locations',show=False)
airportfg=folium.FeatureGroup(name='Airports',show=True)
triplinefg=folium.FeatureGroup(name='Trip lines',show=False)

groups={
'npfg':npfg,
'littlefg':littlefg,
'inoutfg':inoutfg,
'airportfg':airportfg,
'triplinefg':triplinefg
}


for i in range(0,len(df)):
    row=df.iloc[i]
    if row['name'] not in sites and row['name']!='In N Out Burger':
        #checks if its a park site and adds it to sites dict
        sites[row['name']]=park(row['name'],row['type'],row['lat'],row['long'],row['dates'],row['disp'])

    elif row['name']=='In N Out Burger':
        #adds to in n out specific list
        in_n_out.append(park(row['name'],row['type'],row['lat'],row['long'],row['dates'],row['disp']))
    elif df.iloc[i]['name'] in sites:
        #if its already in sites it appends the date
        sites[row['name']].add_date(row['dates'])

    if (row['trip'] not in trips) and (not pd.isna(row['trip'])):
        color=colors[random.randint(0,len(colors)-1)]
        trips[row['trip']]=trip(row['trip'],41.0938684589138,-74.0152150078762,color)
        colors.remove(color)
        
        trips[row['trip']].path_logic(row)

    elif (row['trip'] in trips) and (row['stay'] !=''):
        trips[row['trip']].path_logic(row)

    
m = folium.Map(location=(40.002889953443024, -98.66778859149203), zoom_start=5, tiles="cartodb positron")

for key in sites:
    icon.make(sites[key],groups[sites[key].group])
    


for i in in_n_out:
    icon.make(i,groups[i.group])

for keys in trips:
    line.make(trips[keys],groups['triplinefg'])

npfg.add_to(m)
littlefg.add_to(m)
inoutfg.add_to(m)
airportfg.add_to(m)
triplinefg.add_to(m)

folium.LayerControl().add_to(m)

m.save("index.html")