import folium
import pandas as pd

df=pd.read_csv('info/parks.csv')

m = folium.Map(location=(41.087564845018235, -74.0133280647248), zoom_start=7, tiles="cartodb positron")
BattleOneLat=[41.0938684589138]
BigSummerLat=[41.0938684589138]
BattleTwoLat=[41.0938684589138]
BattleOneLong=[-74.0152150078762]
BigSummerLong=[-74.0152150078762]
BattleTwoLong=[-74.0152150078762]

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

def lineMaker(lat,long,color):
    for i in range(0,len(lat)):
        if i+1 >= len(lat):
            point1=[lat[i],long[i]]
            point2=[41.0938684589138,-74.0152150078762]
        else:
            point1=[lat[i],long[i]]
            point2=[lat[i+1],long[i+1]]
        line = folium.PolyLine(locations=[point1, point2], color=color, weight=5, opacity=0.8).add_to(m)


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
    elif df.iloc[i]['type']=='NPres' or df.iloc[i]['type']=='NHRES':
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
    elif df.iloc[i]['type']=='NMEMPWKY':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('gray','car','fa')
        ).add_to(m)
    elif df.iloc[i]['type']=='OTHERPARK':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker('cadetblue','person-hiking','fa')
        ).add_to(m)

    if df.iloc[i]['trip'] != '':
        if df.iloc[i]['trip'] == "BattleOne":
            BattleOneLat.append(df.iloc[i]['lat'])
            BattleOneLong.append(df.iloc[i]['long'])
        elif df.iloc[i]['trip'] == "BigSummer":
            BigSummerLat.append(df.iloc[i]['lat'])
            BigSummerLong.append(df.iloc[i]['long'])
        elif df.iloc[i]['trip'] == "BattleTwo":
            BattleTwoLat.append(df.iloc[i]['lat'])
            BattleTwoLong.append(df.iloc[i]['long'])

lineMaker(BattleOneLat,BattleOneLong,'blue')
lineMaker(BigSummerLat,BigSummerLong,'green')
lineMaker(BattleTwoLat,BattleTwoLong,'red')

m.save("footprint.html")