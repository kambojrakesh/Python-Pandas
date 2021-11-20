# -*- coding: utf-8 -*-
import pandas as pd
#s= pd.Series()
#s


##Array to series
import numpy as np
data = np.array(['a','b','c','d'])
#print(data)
#print(pd.Series(data))
#print(pd.Series(data, index=[1,3,4,7]))


##Dictionary to series
data = {'a':1, 'b':11, 'c':90}
#print(type(data))
#print(pd.Series(data))


##Scaler to series
data = pd.Series(5, index=[1,2,3,4])
#print(data)


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
#print(s['d'])

#print(s[:2])
#print(s[2:])
#print("-------------",s[-5])

#print(s[0:2])
#print(s[['a','c','d']])



d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
data = pd.DataFrame(d)

#print(data.describe())

data = np.random.randn(4,3,2)
#print (data)


def adder(ele1,ele2):
   #print(ele1)
   return ele1+ele2

df = pd.DataFrame([[1,2,4],[4,6,10]],columns=['col1','col2','col3'])
#print(df)

#df=df.pipe(adder,2000)
#print(df)
df = df.apply(lambda x: x.max() - x.min())
print(df)


