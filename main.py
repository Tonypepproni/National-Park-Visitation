import pandas as pd
import folium

from makers import line,icon,obj
from mapObj import park, trip

df=pd.read_csv('info/parks.csv')
sites={}
trips={}
in_n_out=[]


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

obj.make(df,sites,trips,in_n_out)

    
m = folium.Map(location=(40.70812490067838, -74.0015293469354), zoom_start=5, tiles="cartodb positron")

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