import folium
import pandas as pd

df=pd.read_csv('info/parks.csv')

m = folium.Map(location=(40.002889953443024, -98.66778859149203), zoom_start=5, tiles="cartodb positron")
BattleOneLat=[41.0938684589138]
BigSummerLat=[41.0938684589138]
BattleTwoLat=[41.0938684589138]
DesLat=[41.0938684589138]
BattleOneLong=[-74.0152150078762]
BigSummerLong=[-74.0152150078762]
BattleTwoLong=[-74.0152150078762]
DesLong=[-74.0152150078762]

npfg=folium.FeatureGroup(name='National parks',show=True)
littlefg=folium.FeatureGroup(name="'small' parks",show=True)
inoutfg=folium.FeatureGroup(name='In n Out Locations',show=False)
airportfg=folium.FeatureGroup(name='Airports',show=True)
triplinefg=folium.FeatureGroup(name='Trip lines',show=False)

staylat=''

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

def marker_maker(df,group,color,img):
    folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=folium.Popup(html=htmlMaker(df,i),max_width=300),
            icon=iconMaker(color,img,'fa')#creates a marker with this style
        ).add_to(group)

def lineMaker(lat,long,color):
    for i in range(0,len(lat)):
        if i+1 >= len(lat):
            point1=[lat[i],long[i]]
            point2=[41.0938684589138,-74.0152150078762]
        else:
            point1=[lat[i],long[i]]
            point2=[lat[i+1],long[i+1]]
        line = folium.PolyLine(locations=[point1, point2], color=color, weight=5, opacity=0.8).add_to(triplinefg)

def tripapend(lat,long):
    if df.iloc[i]['trip'] == "BattleOne":
        BattleOneLat.append(lat)
        BattleOneLong.append(long)
    elif df.iloc[i]['trip'] == "BigSummer":
        BigSummerLat.append(lat)
        BigSummerLong.append(long)
    elif df.iloc[i]['trip'] == "BattleTwo":
        BattleTwoLat.append(lat)
        BattleTwoLong.append(long)
    elif df.iloc[i]['trip'] == "Des":
        DesLat.append(lat)
        DesLong.append(long)

for i in range(0,len(df)):
    if df.iloc[i]['type']=='NP':
        marker_maker(df,npfg,'green','tree')

    elif df.iloc[i]['type']=='NHP':
        marker_maker(df,littlefg,'purple','landmark')

    elif df.iloc[i]['type']=='NPres' or df.iloc[i]['type']=='NHRES':
        marker_maker(df,littlefg,'red','binoculars')
    elif df.iloc[i]['type']=='NHS':
        marker_maker(df,littlefg,'black','landmark-dome')

    elif df.iloc[i]['type']=='NM':
        marker_maker(df,littlefg,'lightred','monument')

    elif df.iloc[i]['type']=='NRA':
        marker_maker(df,littlefg,'darkpurple','compass')

    elif df.iloc[i]['type']=='NS':
        marker_maker(df,littlefg,'darkblue','water')

    elif df.iloc[i]['type']=='NL':
        marker_maker(df,littlefg,'lightblue','wind')

    elif df.iloc[i]['type']=='NMEM':
        marker_maker(df,littlefg,'darkred','archway')

    elif (df.iloc[i]['type']=='NMP') or (df.iloc[i]['type']=='NB') or (df.iloc[i]['type']=='NBP'):
        marker_maker(df,littlefg,'orange','person-rifle')

    elif df.iloc[i]['type']=='PARK':
        marker_maker(df,littlefg,'lightgreen','frog')

    elif df.iloc[i]['type']=='NMEMPWKY':
        marker_maker(df,littlefg,'gray','car')

    elif df.iloc[i]['type']=='AIRPORT':
        marker_maker(df,airportfg,'darkgreen','plane')
    elif df.iloc[i]['type']=='Bur':
        marker_maker(df,inoutfg,'pink','burger')

    if df.iloc[i]['trip'] != '':
        if df.iloc[i]['stay'] == '' or (df.iloc[i]['stay']=='through'):
            #print(df.iloc[i]['name'])
            staylat=''
            staylong=''
        elif df.iloc[i]['stay']=='through' '''and (staylat>0 or staylat!=0)''':
            print(df.iloc[i]['name'])
            tripapend(staylat,staylong)
            staylat=0
        elif (df.iloc[i]['stay'] == 'stay' and staylat == '') or (df.iloc[i]['stay'] == 'through'):
            #print(df.iloc[i]['name'])
            staylat=df.iloc[i]['lat']
            staylong=df.iloc[i]['long']
        elif (df.iloc[i]['stay'] == 'stay' and staylat>0)or(df.iloc[i]['stay'] == 'through' and staylat>0):
            
            tripapend(staylat,staylong)
            staylat=df.iloc[i]['lat']
            staylong=df.iloc[i]['long']
        

        tripapend(df.iloc[i]['lat'],df.iloc[i]['long'])

lineMaker(BattleOneLat,BattleOneLong,'blue')
lineMaker(BigSummerLat,BigSummerLong,'green')
lineMaker(BattleTwoLat,BattleTwoLong,'red')
lineMaker(DesLat,DesLong,'purple')


npfg.add_to(m)
littlefg.add_to(m)
inoutfg.add_to(m)
airportfg.add_to(m)
triplinefg.add_to(m)

folium.LayerControl().add_to(m)

m.save("footprint.html")