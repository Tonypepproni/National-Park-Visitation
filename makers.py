import pandas as pd
import folium

class maker_tools:
    def __init__(self):
        pass

    def iconMaker(self,color,icon,prefix):
        return folium.Icon(color=color,icon=icon,prefix=prefix)
    
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
    
    def marker_maker(self,group,color,icon,obj):
        folium.Marker(
                location=[obj.lat,obj.long],#locates long and lat from the data frame and displays it
                popup=folium.Popup(html=self.htmlMaker(obj),max_width=300),
                icon=self.iconMaker(color,icon,'fa')#creates a marker with this style
            ).add_to(group)

    def line_maker(self,obj,group):
        for i in range(0,len(obj.lat)):
            if i+1 >= len(obj.lat):
                point1=[obj.lat[i],obj.long[i]]
                point2=[obj.lat[0],obj.long[0]]
            else:
                point1=[obj.lat[i],obj.long[i]]
                point2=[obj.lat[i+1],obj.long[i+1]]

            folium.PolyLine(locations=[point1,point2 ], 
                            color='green', 
                            weight=5, 
                            opacity=0.8).add_to(group)





maker_tools=maker_tools()
