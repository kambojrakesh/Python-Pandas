# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:30:31 2021

@author: Vikki
"""
import pandas as pd

df = pd.read_csv("E:/learning/AI1/python/Python-Pandas/1.0 Introduction/temperature.csv")

print(df['AverageTemperatureFahr'].max())

print(df['year'][df['month']==1])


print(df['AverageTemperatureFahr'].mean())

print(df['AverageTemperatureUncertaintyFahr'])
df.fillna(0.0000, inplace=True)
print(df['AverageTemperatureUncertaintyFahr'])