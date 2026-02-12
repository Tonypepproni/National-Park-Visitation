class park:

    type_map = {
    'NP': ('green', 'tree', 'npfg'),
    'NHP': ('purple', 'landmark', 'littlefg'),
    'NPres': ('red', 'binoculars', 'littlefg'),
    'NHRES': ('red', 'binoculars', 'littlefg'),
    'NHS': ('black', 'landmark-dome', 'littlefg'),
    'NM': ('#FF8E7F', 'monument', 'littlefg'),
    'NRA': ('#5B396B', 'compass', 'littlefg'),
    'NS': ('darkblue', 'water', 'littlefg'),
    'NL': ('lightblue', 'water', 'littlefg'),
    'NMEM': ('darkred', 'archway', 'littlefg'),
    'NMP': ('orange', 'person-military-rifle', 'littlefg'),
    'NB': ('orange', 'person-rifle', 'littlefg'),
    'NBP': ('orange', 'person-military-pointing', 'littlefg'),
    'PARK': ('lightgreen', 'frog', 'littlefg'),
    'NMEMPWKY': ('gray', 'car', 'littlefg'),
    'AIRPORT': ('darkgreen', 'plane', 'airportfg'),
    'Bur':('pink','burger','inoutfg'),
    'petroglyph':('#7D2929','wave-square','nativeSitesfg'),
    'quarry':('#C56C39','hill-rockslide','nativeSitesfg'),
    'mound':('#694C38','mound','nativeSitesfg'),
    'greatwork':('#F8F8F6','connectdevelop','nativeSitesfg')
    }

    def __init__(self,name,type,lat,long,date,disp):
        self.name=name
        self.type=type
        self.lat=lat
        self.long=long
        self.date=date
        self.disp=disp
        self.add_three()


    def add_date(self,date):
        self.date = self.date + ', ' + date

    def add_three(self):
        self.color,self.icon_type,self.group=park.type_map[self.type]

class trip:
    def __init__(self,trip_name,start_lat,start_long,color):
        self.name=trip_name
        self.lat=[start_lat]
        self.long=[start_long]
        self.color=color
        self.coords=[0,0]
    
    
    def add_loc(self,lat,long):
        self.lat.append(lat)
        self.long.append(long)

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
