import pandas as pd
import folium

from makers import maker_tools
from mapObj import park, trip

df=pd.read_csv('info/parks.csv')
sites={}
trips={}
in_n_out=[]
coords=[0,0]

for i in range(0,len(df)):
    if df.iloc[i]['name'] not in sites and df.iloc[i]['name']!='In N Out Burger':
        #checks if its a park site and adds it to sites dict
        sites[df.iloc[i]['name']]=park(df.iloc[i]['name'],df.iloc[i]['type'],df.iloc[i]['lat'],df.iloc[i]['long'],df.iloc[i]['dates'],df.iloc[i]['disp'])
    elif df.iloc[i]['name']=='In N Out Burger':
        #adds to in n out specific list
        in_n_out.append(park(df.iloc[i]['name'],df.iloc[i]['type'],df.iloc[i]['lat'],df.iloc[i]['long'],df.iloc[i]['dates'],df.iloc[i]['disp']))
    elif df.iloc[i]['name'] in sites:
        #if its already in sites it appends the date
        sites[df.iloc[i]['name']].add_date(df.iloc[i]['dates'])

    if (df.iloc[i]['trip'] not in trips) and (not pd.isna(df.iloc[i]['trip'])):
        trips[df.iloc[i]['trip']]=trip(df.iloc[i]['trip'],41.0938684589138,-74.0152150078762)
    elif (df.iloc[i]['trip'] in trips) and (df.iloc[i]['stay'] !=''):
        if df.iloc[i]['stay'] =='stay' and (coords[0]==0):
            coords[0] = df.iloc[i]['lat']
            coords[1] = df.iloc[i]['long']
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])
        elif df.iloc[i]['stay'] =='through' and (coords[0]!=0):
            coords[0]=0
            coords[1]=0
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])
        elif df.iloc[i]['stay'] =='through' and (coords[0]==0):
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])
        elif df.iloc[i]['stay'] =='visit':
            trips[df.iloc[i]['trip']].add_loc(df.iloc[i]['lat'],df.iloc[i]['long'])


    
m = folium.Map(location=(40.002889953443024, -98.66778859149203), zoom_start=5, tiles="cartodb positron")

npfg=folium.FeatureGroup(name='National parks',show=True)
littlefg=folium.FeatureGroup(name="'small' parks",show=True)
inoutfg=folium.FeatureGroup(name='In n Out Locations',show=False)
airportfg=folium.FeatureGroup(name='Airports',show=True)
triplinefg=folium.FeatureGroup(name='Trip lines',show=False)

for key in sites:
    if sites[key].type=='NP':
        maker_tools.marker_maker(npfg,'green','tree',sites[key])

    elif sites[key].type=='NHP':
        maker_tools.marker_maker(littlefg,'purple','landmark',sites[key])

    elif sites[key].type=='NPres' or df.iloc[i]['type']=='NHRES':
        maker_tools.marker_maker(littlefg,'red','binoculars',sites[key])

    elif sites[key].type=='NHS':
        maker_tools.marker_maker(littlefg,'black','landmark-dome',sites[key])

    elif sites[key].type=='NM':
        maker_tools.marker_maker(littlefg,'lightred','monument',sites[key])

    elif sites[key].type=='NRA':
        maker_tools.marker_maker(littlefg,'darkpurple','compass',sites[key])

    elif sites[key].type=='NS':
        maker_tools.marker_maker(littlefg,'darkblue','water',sites[key])

    elif sites[key].type=='NL':
        maker_tools.marker_maker(littlefg,'lightblue','wind',sites[key])

    elif sites[key].type=='NMEM':
        maker_tools.marker_maker(littlefg,'darkred','archway',sites[key])

    elif (sites[key].type=='NMP') or (sites[key].type=='NB') or (sites[key].type=='NBP'):
        maker_tools.marker_maker(littlefg,'orange','person-rifle',sites[key])

    elif sites[key].type=='PARK':
        maker_tools.marker_maker(littlefg,'lightgreen','frog',sites[key])

    elif sites[key].type=='NMEMPWKY':
        maker_tools.marker_maker(littlefg,'gray','car',sites[key])

    elif sites[key].type=='AIRPORT':
        maker_tools.marker_maker(airportfg,'darkgreen','plane',sites[key])


for i in in_n_out:
    maker_tools.marker_maker(inoutfg,'pink','burger',i)

maker_tools.line_maker(trips['BattleOne'],triplinefg)
    



npfg.add_to(m)
littlefg.add_to(m)
inoutfg.add_to(m)
airportfg.add_to(m)
triplinefg.add_to(m)

folium.LayerControl().add_to(m)

m.save("newMap.html")