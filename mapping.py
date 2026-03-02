import openrouteservice
from openrouteservice import convert

client = openrouteservice.Client(key='eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjhiYjI5MjdhYmRhMTRlODQ5ZGIxNWNjYzAyZDVmNTg1IiwiaCI6Im11cm11cjY0In0=')


cords = [
    (-85.3436311713325,35.010826835294615),
    (-85.70685294623361,32.429875301973574)
]

route=client.directions(cords)

duration=route['routes'][0]['summary']['duration']/60

print(f'Driving time: {duration:.1f}')