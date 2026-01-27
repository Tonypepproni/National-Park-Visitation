import pandas as pd
import folium

class maker_tools:
    def __init__(self):
        pass

    def iconMaker(self,color,icon,prefix):
        return folium.Icon(color=color,icon=icon,prefix=prefix)
    
    def popupMaker(self,df,i):
        return df.iloc[i]['name']
    
    def htmlMaker(self,df,i):
        marker_html = f"""
        <!DOCTYPE html>
        <html>
            <body><center>
                <h3>{df.iloc[i]['name']}</h3>
                <p>{df.iloc[i]['disp']}</p>
                <h3>Dates visted</h3>
                <p>{df.iloc[i]['dates']}</p>
            </center></body>
        </html>
        """
        return marker_html
    
    def marker_maker(self,df,group,color,img,i):
        folium.Marker(
                location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
                popup=folium.Popup(html=self.htmlMaker(df,i),max_width=300),
                icon=self.iconMaker(color,img,'fa')#creates a marker with this style
            ).add_to(group)
        
maker_tools=maker_tools()
