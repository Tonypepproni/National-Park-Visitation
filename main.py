import pandas as pd
import folium
import random

from makers import line,icon
from mapObj import park, trip

df=pd.read_csv('info/parks.csv')
sites={}
trips={}
in_n_out=[]
coords=[0,0]
colors=['red','blue','green','purple','pink','darkred']

npfg=folium.FeatureGroup(name='National parks',show=True)
littlefg=folium.FeatureGroup(name="'small' parks",show=True)
inoutfg=folium.FeatureGroup(name='In n Out Locations',show=False)
airportfg=folium.FeatureGroup(name='Airports',show=True)
triplinefg=folium.FeatureGroup(name='Trip lines',show=False)

type_map = {
    'NP': ('green', 'tree', npfg),
    'NHP': ('purple', 'landmark', littlefg),
    'NPres': ('red', 'binoculars', littlefg),
    'NHRES': ('red', 'binoculars', littlefg),
    'NHS': ('black', 'landmark-dome', littlefg),
    'NM': ('lightred', 'monument', littlefg),
    'NRA': ('darkpurple', 'compass', littlefg),
    'NS': ('darkblue', 'water', littlefg),
    'NL': ('lightblue', 'water', littlefg),
    'NMEM': ('darkred', 'archway', littlefg),
    'NMP': ('orange', 'person-rifle', littlefg),
    'NB': ('orange', 'person-rifle', littlefg),
    'NBP': ('orange', 'person-rifle', littlefg),
    'PARK': ('lightgreen', 'frog', littlefg),
    'NMEMPWKY': ('gray', 'car', littlefg),
    'AIRPORT': ('darkgreen', 'plane', airportfg),
    'Bur':('pink','burger',inoutfg)
}


for i in range(0,len(df)):
    if df.iloc[i]['name'] not in sites and df.iloc[i]['name']!='In N Out Burger':
        #checks if its a park site and adds it to sites dict
        sites[df.iloc[i]['name']]=park(df.iloc[i]['name'],df.iloc[i]['type'],df.iloc[i]['lat'],df.iloc[i]['long'],df.iloc[i]['dates'],df.iloc[i]['disp'])
        
        
    elif df.iloc[i]['name']=='In N Out Burger':
        #adds to in n out specific list
        in_n_out.append(park(df.iloc[i]['name'],df.iloc[i]['type'],df.iloc[i]['lat'],df.iloc[i]['long'],df.iloc[i]['dates'],df.iloc[i]['disp']))
        in_n_out[-1].add_three(inoutfg,'pink','burger')
    elif df.iloc[i]['name'] in sites:
        #if its already in sites it appends the date
        sites[df.iloc[i]['name']].add_date(df.iloc[i]['dates'])

    if (df.iloc[i]['trip'] not in trips) and (not pd.isna(df.iloc[i]['trip'])):
        color=colors[random.randint(0,len(colors))-1]
        trips[df.iloc[i]['trip']]=trip(df.iloc[i]['trip'],41.0938684589138,-74.0152150078762,color)
        colors.remove(color)
        
        if df.iloc[i]['stay'] =='stay' and (coords[0]==0):
            coords[0] = df.iloc[i]['lat']
            coords[1] = df.iloc[i]['long']
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

        elif df.iloc[i]['stay'] =='through':
            coords[0]=0
            coords[1]=0
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

        elif df.iloc[i]['stay'] =='visit':
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

        elif df.iloc[i]['stay'] == 'stay':
            trips[df.iloc[i]['trip']].add_loc(coords[0],coords[1])
            coords[0] = df.iloc[i]['lat']
            coords[1] = df.iloc[i]['long']
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

    elif (df.iloc[i]['trip'] in trips) and (df.iloc[i]['stay'] !=''):
        if df.iloc[i]['stay'] =='stay' and (coords[0]==0):
            coords[0] = df.iloc[i]['lat']
            coords[1] = df.iloc[i]['long']
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

        elif df.iloc[i]['stay'] =='through':
            coords[0]=0
            coords[1]=0
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

        elif df.iloc[i]['stay'] =='visit':
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])

        elif df.iloc[i]['stay'] == 'stay':
            trips[df.iloc[i]['trip']].add_loc(coords[0],coords[1])
            coords[0] = df.iloc[i]['lat']
            coords[1] = df.iloc[i]['long']
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])


    
m = folium.Map(location=(40.002889953443024, -98.66778859149203), zoom_start=5, tiles="cartodb positron")

for key in sites:
    if sites[key].type in type_map:
        color,icon_type,group=type_map[sites[key].type]
        icon.make(group,color,icon_type,sites[key])
    


for i in in_n_out:
    if i.type in type_map:
         color,icon_type,group=type_map[i.type]
    icon.make(group,color,icon_type,i)

for keys in trips:
    line.make(trips[keys],triplinefg)

npfg.add_to(m)
littlefg.add_to(m)
inoutfg.add_to(m)
airportfg.add_to(m)
triplinefg.add_to(m)

folium.LayerControl().add_to(m)

m.save("newMap.html")