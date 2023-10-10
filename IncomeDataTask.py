# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:35:13 2023
@author: Johnwesly
"""
import pandas as pd
heaad = ['age','workclass','fnlwgt','education','education-num','maritial-status','occupation','relationship','race','sex','capital-gain','capital-loss','hpw','country','income']
data=pd.read_csv(r"D:\AIML\incomedataset.csv",names=heaad)

labels=['workclass','education','maritial-status','occupation','relationship','race','sex','country','income']
for i in heaad:
    dicct=dict(data[i].value_counts())
    if " ?" in dicct:
        dl=list(dicct.keys())
        data[i].replace(' ?',dl[0],inplace=True)
from sklearn import preprocessing
le = preprocessing.LabelBinarizer()
for i in labels:
    data[i] = le.fit_transform(data[i])

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest, ypred)*100)












import pandas as pd
names=[]
for i in 'abcdefghijklmno':
    names.append(i)
data=pd.read_cvs(r"D:\AIML\incomedataset.csv",names=names)
data.head()
data.shape
data.isna().sum()
data['b'].value_count()
ata['b']=data['b'].replace(to_replace=' ?',value=' Private')
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in 'bdfghijn':
    data[i]=le.fit_transform(data[i])
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5,random_state=13)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score

print(accuracy_score(ytest, ypred)*100)