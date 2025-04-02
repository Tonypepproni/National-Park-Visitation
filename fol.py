import folium
import pandas as pd

df=pd.read_csv('info/parks.csv')

m = folium.Map(location=(41.087564845018235, -74.0133280647248), zoom_start=7, tiles="cartodb positron")

def iconMaker(color,icon,prefix):
    return folium.Icon(color=color,icon=icon,prefix=prefix)

def popupMaker(df,i):
    return df.iloc[i]['name']

def htmlMaker(df,i):
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
    

for i in range(0,len(df)):
    if df.iloc[i]['type']=='NP':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('green','tree','fa')#creates a marker with this style
        ).add_to(m)

    elif df.iloc[i]['type']=='NHP':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('purple','landmark','fa')#creates a marker with this style
        ).add_to(m)
    elif df.iloc[i]['type']=='NPres':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('red','binoculars','fa')#creates a marker with this style
        ).add_to(m)
    elif df.iloc[i]['type']=='NHS':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('black','landmark-dome','fa')#creates a marker with this style
        ).add_to(m)
    elif df.iloc[i]['type']=='NM':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('lightred','monument','fa')#creates a marker with this style
        ).add_to(m)
    elif df.iloc[i]['type']=='NRA':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('darkpurple','compass','fa')
        ).add_to(m)
    elif df.iloc[i]['type']=='NS':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('darkblue','water','fa')
        ).add_to(m)
    elif df.iloc[i]['type']=='NL':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('lightblue','wind','fa')
        ).add_to(m)
    elif df.iloc[i]['type']=='NMEM':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('darkred','archway','fa')
        ).add_to(m)
    elif (df.iloc[i]['type']=='NMP') or (df.iloc[i]['type']=='NB') or (df.iloc[i]['type']=='NBP'):
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('orange','parachute-box','fa')
        ).add_to(m)
    elif df.iloc[i]['type']=='PARK':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('lightgreen','frog','fa')
        ).add_to(m)
    

m.save("footprint.html")