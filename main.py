import pandas as pd
import folium

from makers import line,icon,objPark

from makers import obj

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
city=folium.FeatureGroup(name='Cities',show=False)
campgroundfg=folium.FeatureGroup(name="Campgrounds",show=False)
gardenandzoofg=folium.FeatureGroup(name="Gardens, Zoos, Aquariums", show=False)


groups={
'npfg':npfg,
'littlefg':littlefg,
'inoutfg':inoutfg,
'airportfg':airportfg,
'triplinefg':triplinefg,
'city':city,
'campgroundfg':campgroundfg,
"gardenandzoofg":gardenandzoofg
}

objPark.make(df,sites,trips,in_n_out)
    
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
city.add_to(m)
campgroundfg.add_to(m)
gardenandzoofg.add_to(m)

folium.LayerControl().add_to(m)

m.save("index.html")

'''coObj=obj(42.36593547920669, -71.00937673924525)

dfc=pd.read_csv('info/co.csv')

sitesc={}
tripc={}

city=folium.FeatureGroup(name='Cities',show=True)
airportfg=folium.FeatureGroup(name='Airports',show=True)
nature=folium.FeatureGroup(name='Nature Place',show=True)
triplinecfg=folium.FeatureGroup(name='Trip lines',show=True)

groupsc={
'city':city,
'airportfg':airportfg,
'nature':nature,
'triplinecfg':triplinecfg
}

coObj.make(dfc,sites=sitesc,trips=tripc)
    
mc = folium.Map(location=(34.42660027781548, -41.54689363489738), zoom_start=3, tiles="cartodb positron")

for key in sitesc:
    icon.make(sitesc[key],groupsc[sitesc[key].group])

for keys in tripc:
    line.make(tripc[keys],groupsc['triplinecfg'])

city.add_to(mc)
airportfg.add_to(mc)
nature.add_to(mc)
triplinecfg.add_to(mc)

folium.LayerControl().add_to(mc)

mc.save("countires.html")'''