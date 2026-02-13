class park:

    type_map = {
    'NP': ('green', 'tree', 'npfg','National Park'),
    'NHP': ('purple', 'landmark', 'littlefg','National Historical Park'),
    'NPres': ('red', 'binoculars', 'littlefg','National Preserve'),
    'NHRES': ('red', 'binoculars', 'littlefg','National Historic Reserve'),
    'NHS': ('black', 'landmark-dome', 'littlefg','National Historic Site'),
    'NM': ('#FF8E7F', 'monument', 'littlefg','National Monument'),
    'NRA': ('#5B396B', 'compass', 'littlefg','National Recreation Area'),
    'NS': ('darkblue', 'water', 'littlefg','National Seashore'),
    'NL': ('lightblue', 'water', 'littlefg','National Lakeshore'),
    'NMEM': ('darkred', 'archway', 'littlefg','National Memorial'),
    'NMP': ('orange', 'person-military-rifle', 'littlefg','National Military Park'),
    'NB': ('orange', 'person-rifle', 'littlefg','National Battle Field'),
    'NBP': ('orange', 'person-military-pointing', 'littlefg','National Battle Field Park'),
    'PARK': ('lightgreen', 'frog', 'littlefg','Park'),
    'NMEMPWKY': ('gray', 'car', 'littlefg','National Memorial Parkway'),
    'AIRPORT': ('darkgreen', 'plane', 'airportfg','Burger King'),
    'Bur':('pink','burger','inoutfg','In N Out'),
    'petroglyph':('#7D2929','wave-square','nativeSitesfg','Petroglyphs'),
    'quarry':('#C56C39','hill-rockslide','nativeSitesfg','Rock Formations or Quarry'),
    'mound':('#694C38','mound','nativeSitesfg','Mound'),
    'greatwork':('#F8F8F6','connectdevelop','nativeSitesfg','Great Works')
    }

    def __init__(self,name,type,lat,long,date):
        self.name=name
        self.type=type
        self.lat=lat
        self.long=long
        self.date=date
        self.mapping()


    def add_date(self,date):
        self.date = self.date + ', ' + date

    def mapping(self):
        self.color,self.icon_type,self.group,self.disp=park.type_map[self.type]

class trip:
    def __init__(self,trip_name,start_lat,start_long,color):
        self.name=trip_name
        self.locations=[
            [start_lat,start_long]
        ]
        self.start=[start_lat,start_long]
        self.lat=[start_lat]
        self.long=[start_long]
        self.color=color
        self.coords=[0,0]
    
    
    def add_loc(self,lat,long):
        self.locations.append([lat,long])

    def cap(self):
        self.add_loc(self.start[0],self.start[1])

    def path_logic(self,row):
        if row['stay'] =='stay' and (self.coords[0]==0):
                self.coords[0] = row['lat']
                self.coords[1] = row['long']
                self.add_loc(row['lat'],row['long'])

        elif row['stay'] =='through':
            self.coords[0]=0
            self.coords[1]=0
            self.add_loc(row['lat'],row['long'])

        elif row['stay'] =='visit':
            self.add_loc(row['lat'],row['long'])

        elif row['stay'] == 'stay':
            self.add_loc(self.coords[0],self.coords[1])
            self.coords[0] = row['lat']
            self.coords[1] = row['long']
            self.add_loc(row['lat'],row['long'])
