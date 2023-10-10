import pandas as pd
data=pd.read_csv(r"D:\AIML\data3.csv")
print(data["Year"].value_counts())
data.shape    #it will give no.of.rows and no.of.col
data.size     #it will give rows*clos
data.ndim     #
data.head()   #print 5 rows from head
a=data.head(10) #prints 10 rows from head
data.tail()   #print 5 rows from head
data.tail(10) #print 10 rows from head
data.columns  #it will heder column
data['Title'] #it will give complete column
data['Revenue (Millions)'].max()
data['Revenue (Millions)'].min()
data['Revenue (Millions)'].mean()
data.describe()
#mean, mode, standerd deviation ,variance
data['Year']
data['Year'].unique()
data['Year'].value_counts()
data.isna().sum()
data.dropna(inplace=True)
data.shape
data.drop(['Revenue (Millions)','Metascore'],axis=1,inplace=True)
data.shape
data=pd.read_csv(r"D:\AIML\data3.csv")
data.shape
data=data._append(data)
data.shape
data=pd.concat([data,data])
data[data['Year']==2016].count()
data[data['Revenue (Millions)']>250]
m=data[(data['Year']==2016) & (data['Revenue (Millions)']>200)]
m=data[(data['Year']==2016) | (data['Revenue (Millions)']>200)]
data.iloc[530,1]
data.iloc[0:2,0:2]