class trip:
    def __init__(self,trip_name,start_lat,start_long):
        self.trip_name=trip_name
        self.lat=[start_lat]
        self.long=[start_long]
    
    
    def add_loc(self,lat,long):
        self.lat.append(lat)
        self.long.append(long)