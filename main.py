import pandas as pd

class Park:
    def __init__(self,data):
        self.data=data

        #Creates data frame upon init
        self.df=pd.read_csv(self.data, header=2)
        self.df.columns=self.df.columns.str.strip().str.upper()
        self.df.iloc[:,1:14]=self.df.iloc[:,1:14].replace(",","",regex=True)
        for col in self.df.columns[1:14]:
            self.df[col]=pd.to_numeric(self.df[col],errors="coerce")

    def spefYearDF(self,year):
        self.spefYear=self.df[self.df["YEAR"]>=year]

    def oneMonthStats(self,month):
        self.oneMean=self.spefYear[month].mean()
        self.oneVar=self.spefYear[month].var()
        self.oneMin=self.spefYear[month].min()
        self.oneMax=self.spefYear[month].max()



    def printSpefYearDF(self):
        print(self.spefYear)

    def printDF(self):
        print(self.df)

    def printOneMonthStats(self):
        print(f"The mean is {self.oneMean:,.3f} and the var is {self.oneVar:,.3f}")
        print(f"{self.oneMin:,} {self.oneMax:,}")

cedarBreaks=Park('data/CedarBreaks.csv')
cedarBreaks.spefYearDF(2021)
cedarBreaks.printSpefYearDF()
cedarBreaks.oneMonthStats("MAY")
cedarBreaks.printOneMonthStats()
