# -*- coding: utf-8 -*-
import pandas as pd
#s= pd.Series()
#s


##Array to series
import numpy as np
data = np.array(['a','b','c','d'])
data = pd.DataFrame()
#print(data)


data = pd.DataFrame([1,3,2,4,5,6])
#print(data)

data = [["rikki",10],["sahil",12],["navdeep",40]]


data = pd.DataFrame(data,columns=["name","age"], dtype=float)
#print(data)


data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
#print(df)


data = {"a1":{'a':1,'b':1},"c1":{'c':11,'dd':12,'w':4}}
#print(pd.DataFrame(data, index=["www","eee"]))

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
#print(df)


df['three']=pd.Series([11,2,3,4], index=['a', 'b', 'c', 'd'])

#print(df['two'] + df['three'])



d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

#print(d)
#df = pd.DataFrame(d)

#print(df.loc['b'])

data = [[1, 2], [3, 4]]
print(type(data))












