import folium
import requests
import pandas as pd

API_KEY='s5MDecR4Q6MnPKTtuae3IuFf2wo3OgCOo7cHdYJk'
SITE_CODE=''



no=['AIRP',"INOB","NONE"]

df=pd.read_csv('info/parks.csv')

m = folium.Map(location=(40.002889953443024, -98.66778859149203), zoom_start=5, tiles="cartodb positron")



for SITE_CODE in df['code'].unique():

    if SITE_CODE in no:
        continue

    url = f"https://developer.nps.gov/api/v1/mapdata/parkboundaries/{SITE_CODE}?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        continue

    try:
        geo_data = response.json()
    except:
        continue

    if not geo_data.get("features"):
        continue

    geo = geo_data["features"][0]["geometry"]
    geom_type = geo["type"]
    coordinates = geo["coordinates"]

    if geom_type == "Polygon":
        polygons = [coordinates]
    elif geom_type == "MultiPolygon":
        polygons = coordinates
    else:
        continue

    for polygon in polygons:
        for ring in polygon:
            latlngs = [[lat, lng] for lng, lat in ring]

            folium.Polygon(
                locations=latlngs,
                color="blue",
                weight=2,
                fill=True,
                fill_opacity=0.4
            ).add_to(m)

m.save('park_map.html')

print("Map saved as park_map.html")