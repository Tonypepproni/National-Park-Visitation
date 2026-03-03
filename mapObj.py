class park:

    type_map = {
        'NP': ('#00A36C', 'tree', 'npfg','National Park'),
        'NHP': ('#7D3C98', 'landmark', 'littlefg','National Historical Park'),
        'NPres': ('#cd853f', 'binoculars', 'littlefg','National Preserve'),
        'NHRES': ('#cd853f', 'binoculars', 'littlefg','National Historic Reserve'),
        'NHS': ('#D2042D', 'landmark-dome', 'littlefg','National Historic Site'),
        'NM': ('#FFC000', 'monument', 'littlefg','National Monument'),
        'NRA': ('#FF5F1F', 'compass', 'littlefg','National Recreation Area'),
        'NS': ('#0047AB', 'water', 'littlefg','National Seashore'),
        'NL': ('lightblue', 'water', 'littlefg','National Lakeshore'),
        'NMEM': ('#5C4A72', 'archway', 'littlefg','National Memorial'),
        'NMP': ('#8A3B12', 'person-military-rifle', 'littlefg','National Military Park'),
        'NB': ('#C04E37', 'person-rifle', 'littlefg','National Battle Field'),
        'NBP': ('#B02B3B', 'person-military-pointing', 'littlefg','National Battle Field Park'),
        'PARK': ('#50C878', 'frog', 'littlefg','Park'),
        'NMEMPWKY': ('#848884', 'car', 'littlefg','National Memorial Parkway'),
        'AIRPORT': ('#AFAFAF', 'plane', 'airportfg','Burger King'),
        'Bur':('pink','burger','inoutfg','In N Out')
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
