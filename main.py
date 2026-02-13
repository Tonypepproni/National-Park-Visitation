import pandas as pd
import folium

from folium.plugins.treelayercontrol import TreeLayerControl

from makers import line,icon,obj
from mapObj import park, trip

df=pd.read_csv('info/parks.csv')
dfn=pd.read_csv('info/native_sites.csv')
sites={}
trips={}
in_n_out=[]


npfg=folium.FeatureGroup(name='National parks',show=True)
littlefg=folium.FeatureGroup(name="'small' parks",show=True)
inoutfg=folium.FeatureGroup(name='In n Out Locations',show=False)
airportfg=folium.FeatureGroup(name='Airports',show=True)
triplinefg=folium.FeatureGroup(name='Trip lines',show=False)
nativeSitesfg=folium.FeatureGroup(name='Native American Sites',show=False)

groups={
'npfg':npfg,
'littlefg':littlefg,
'inoutfg':inoutfg,
'airportfg':airportfg,
'triplinefg':triplinefg,
'nativeSitesfg':nativeSitesfg
}

obj.make(df,sites,trips,in_n_out)
obj.make(dfn,sites,trips,in_n_out)

    
m = folium.Map(location=(40.002889953443024, -98.66778859149203), zoom_start=5, tiles="cartodb positron")

for key in sites:
    icon.make(sites[key],groups[sites[key].group])
    


for i in in_n_out:
    icon.make(i,groups[i.group])

for keys in trips:
    line.make(trips[keys],groups['triplinefg'])

npfg.add_to(m)
littlefg.add_to(m)
nativeSitesfg.add_to(m)
inoutfg.add_to(m)
airportfg.add_to(m)
triplinefg.add_to(m)

folium.LayerControl().add_to(m)

m.save("index.html")