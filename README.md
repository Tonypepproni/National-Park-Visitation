This tool allows the easy creation of a map that can be published with github pages to show off all the national parks a user has been to. 

HOW TO USE

step 1: install all the requirments (using a venv is reccommended)

step 2: Creating the csv

  create a csv called "parks.csv"

  give it the columns: name,type,lat,long,dates,trip,stay
    name: the name of the park
    type: the parks designation (np or nm etc.)
    lat: the latitude
    long: longitutde
    dates: dates visited
    trip: the name of the trip it was visited on (can be blank)
    stay: if you visited (visit), drove through (through) or stayed there (stay)

  Populate the csv with parks that you have been too. Note multiple dates cannot be comma seperated, also for trip pathing it only works if you enter the same park twice in the csv.

  Valid types are:
    National Park: NP
    National Historical Park: NHP
    National Preserve: NPres
    National Historic Reserve: NHRES
    National Historic Site: NHS
    National Monument: NM
    National Recration Area: NRA
    National Seashore: NS
    National Lakeshore: NL
    National Memorial: NMEM
    National Military Park: NMP
    National Battlefield: NB
    National Battlefield Park: NBP
    Park: Park (catch all for any without a type)
    National Memorial Parkway: NMEMPWKY
    Airport: AIRPORT
    In n Out Burger: Bur

step 3: run main.py and your map should be generated at index.html
