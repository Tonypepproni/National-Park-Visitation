import pandas as pd
import matplotlib.pyplot as plt

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

    def oneMonthStatsSpef(self,month):
        self.oneMeanSpef=self.spefYear[month].mean()
        self.oneMedianSpef=self.spefYear[month].median()
        self.oneSDSpef=self.spefYear[month].std()
        self.oneMinSpef=self.spefYear[month].min()
        self.oneMaxSpef=self.spefYear[month].max()
        self.oneRangeSpef=self.oneMaxSpef-self.oneMinSpef
        self.oneExSpef=self.spefYear[month].sum()
        
    def oneMonthStats(self,month):
        self.oneMean=self.df[month].mean()
        self.oneMedian=self.df[month].median()
        self.oneSD=self.df[month].std()
        self.oneMin=self.df[month].min()
        self.oneMax=self.df[month].max()
        self.oneRange=self.oneMax-self.oneMin
        self.oneEx=self.df[month].sum()

    def printSpefYearDF(self):
        print(self.spefYear)

    def printDF(self):
        print(self.df)

    def printOneMonthStatsSpef(self):
        print(f"Mean   {self.oneMeanSpef:,.3f}")
        print(f'Median {self.oneMedianSpef:,}')
        print(f"SD     {self.oneSDSpef:,.3f}")
        print(f"Min    {self.oneMinSpef:,}")
        print(f"Max    {self.oneMaxSpef:,}")
        print(f"Range  {self.oneRangeSpef:,}")
        print(f"∑(x)   {self.oneExSpef:,}")

    def printOneMonthStats(self):
        print(f"Mean   {self.oneMean:,.3f}")
        print(f'Median {self.oneMedian:,}')
        print(f"SD     {self.oneSD:,.3f}")
        print(f"Min    {self.oneMin:,}")
        print(f"Max    {self.oneMax:,}")
        print(f"Range  {self.oneRange:,}")
        print(f"∑(x)   {self.oneEx:,}")

cedarBreaks=Park('data/CedarBreaks.csv')
cedarBreaks.spefYearDF(2021)
cedarBreaks.printSpefYearDF()
cedarBreaks.oneMonthStatsSpef("MAY")
cedarBreaks.printOneMonthStatsSpef()
cedarBreaks.oneMonthStats("MAY")
cedarBreaks.printOneMonthStats()

cedarBreaks.df.loc[cedarBreaks.df["YEAR"]==2024,cedarBreaks.df.columns[2:13]].plot(kind="bar",width=1)
plt.show()