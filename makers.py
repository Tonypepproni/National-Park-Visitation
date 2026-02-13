import pandas as pd
import folium
from folium import plugins
from abc import ABC,abstractclassmethod
from mapObj import park, trip
import random

class maker_tools(ABC):
    def make(self,obj,group):
        pass

class line(maker_tools):
    def make(self,obj,group):
        obj.cap()
        folium.plugins.AntPath(
            locations=obj.locations,dash_array=[20,30],color=obj.color
        ).add_to(group)
        

class icon(maker_tools):
    def __init__(self):
        pass

    def iconMaker(self,color,icon,prefix):
        return plugins.BeautifyIcon(
            background_color=color,
            border_color=color,
            text_color='white',
            icon=icon,
            prefix=prefix,
            icon_shape='marker',
            inner_icon_style='margin_top:0;'
        )
    
    def popupMaker(self,df,i):
        return df.iloc[i]['name']
    
    def htmlMaker(self,obj):
        marker_html = f"""
        <!DOCTYPE html>
        <html>
            <body><center>
                <h3>{obj.name}</h3>
                <p>{obj.disp}</p>
                <h3>Dates visted</h3>
                <p>{obj.date}</p>
            </center></body>
        </html>
        """
        return marker_html
    
    def make(self,obj,group):
        folium.Marker(
                location=[obj.lat,obj.long],#locates long and lat from the data frame and displays it
                popup=folium.Popup(html=self.htmlMaker(obj),max_width=300),
                icon=self.iconMaker(obj.color,obj.icon_type,'fa')#creates a marker with this style
            ).add_to(group)

class obj(maker_tools):
    colors=['red','blue','green','purple','pink','darkred','orange']
    def __init__(self):
        pass
    def make(self,df,sites,trips,in_n_out):
        for i in range(0,len(df)):
            row=df.iloc[i]
            if row['name'] not in sites and row['name']!='In N Out Burger':
                #checks if its a park site and adds it to sites dict
                sites[row['name']]=park(row['name'],row['type'],row['lat'],row['long'],row['dates'])

            elif row['name']=='In N Out Burger':
                #adds to in n out specific list
                in_n_out.append(park(row['name'],row['type'],row['lat'],row['long'],row['dates']))
            elif df.iloc[i]['name'] in sites:
                #if its already in sites it appends the date
                sites[row['name']].add_date(row['dates'])

            if (row['trip'] not in trips) and (not pd.isna(row['trip'])):
                color=obj.colors[random.randint(0,len(obj.colors)-1)]
                trips[row['trip']]=trip(row['trip'],41.0938684589138,-74.0152150078762,color)
                obj.colors.remove(color)
                
                trips[row['trip']].path_logic(row)

            elif (row['trip'] in trips) and (row['stay'] !=''):
                trips[row['trip']].path_logic(row)

line=line()
icon=icon()
obj=obj()
