import pandas as pd

'''
for i in df2021.iloc[:,1:13]:
    print(f"The mean for {i} is {df2021[i].mean()}")
'''
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

    def indMean(self,df,month):
        self.mean={'mean':df[month].mean(),"month":month}



    def printSpefYearDF(self):
        print(self.spefYear)

    def printDF(self):
        print(self.df)

    def printIndMean(self):
        print(f"The mean visits for {self.mean['month']} is {self.mean['mean']}")

cedarBreaks=Park('data/CedarBreaks.csv')
cedarBreaks.spefYearDF(2021)
cedarBreaks.printSpefYearDF()
cedarBreaks.indMean(cedarBreaks.spefYear,"MAY")
cedarBreaks.printIndMean()
