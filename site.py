class park:
    def __init__(self,name,type,lat,long,date):
        self.name=name
        self.type=type
        self.lat=lat
        self.long=long
        self.date=date

    def add_date(self,date):
        self.date = self.date + ', ' + date