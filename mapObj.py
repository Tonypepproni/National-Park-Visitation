class park:
    def __init__(self,name,type,lat,long,date,disp):
        self.name=name
        self.type=type
        self.lat=lat
        self.long=long
        self.date=date
        self.disp=disp

    def add_date(self,date):
        self.date = self.date + ', ' + date

class trip:
    def __init__(self,trip_name,start_lat,start_long,color):
        self.name=trip_name
        self.lat=[start_lat]
        self.long=[start_long]
        self.color=color
    
    
    def add_loc(self,lat,long):
        self.lat.append(lat)
        self.long.append(long)
