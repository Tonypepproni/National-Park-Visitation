import pandas as pd
import folium

from makers import maker_tools
from mapObj import park, trip

df=pd.read_csv('info/parks.csv')
sites={}
in_n_out=[]

for i in range(0,len(df)):
    if df.iloc[i]['name'] not in sites and df.iloc[i]['name']!='In N Out Burger':
        sites[df.iloc[i]['name']]=park(df.iloc[i]['name'],df.iloc[i]['type'],df.iloc[i]['lat'],df.iloc[i]['long'],df.iloc[i]['dates'],df.iloc[i]['disp'])
    elif df.iloc[i]['name']=='In N Out Burger':
        in_n_out.append(park(df.iloc[i]['name'],df.iloc[i]['type'],df.iloc[i]['lat'],df.iloc[i]['long'],df.iloc[i]['dates'],df.iloc[i]['disp']))
    elif df.iloc[i]['name'] in sites:
        sites[df.iloc[i]['name']].add_date(df.iloc[i]['dates'])
    
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


npfg.add_to(m)
littlefg.add_to(m)
inoutfg.add_to(m)
airportfg.add_to(m)
triplinefg.add_to(m)

folium.LayerControl().add_to(m)

m.save("newMap.html")