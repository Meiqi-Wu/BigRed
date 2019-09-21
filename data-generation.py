#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:12:06 2019

@author: wumeiqi
"""

import pandas as pd
import numpy as np
import random
#%%
df = pd.DataFrame()
nrow = 5000
df['YOB'] = np.random.choice(range(1910, 2017), size=nrow, replace=True)
df['Income'] = np.random.choice(range(1000, 10001), size=nrow, replace=True)
df['Lon'] = np.random.choice(random.sample(range(-100, -80),10), size=nrow, replace=True)
df['Lat'] = np.random.choice(random.sample(range(20, 50),10), size=nrow, replace=True)
df['Apl_Year'] = np.random.choice(range(2016, 2019), size = nrow, replace=True)
df['gender']=np.random.choice(range(0, 2), size=nrow, replace=True)
df['Accepted'] = False
#%%
def sigmoid(x):
    sigm = 1. / (1. + np.exp(-x))
    return sigm

#%%
index1 = df.query('YOB<=1970 & YOB>=1910').index
YOB = df.iloc[index1, 0]
YOB = (YOB-np.mean(YOB))/np.std(YOB)
Income = df.iloc[index1, 1]
Income = (Income-np.mean(Income))/np.std(Income)
Lon = df.iloc[index1, 2]
Lon = (Lon-np.mean(Lon))/np.std(Lon)
Lat = df.iloc[index1, 3]
Lat = (Lat-np.mean(Lat))/np.std(Lat)
Apl_Year = df.iloc[index1, 4]
Apl_Year = (Apl_Year-np.mean(Apl_Year))/np.std(Apl_Year)
gender = df.iloc[index1, 5]
gender = (gender-np.mean(gender))/np.std(gender)

Z1 = -0.7*YOB+(-0.7)*Income+0.04*Lat+0.04*Lon-0.02*Apl_Year+0.1285*gender+np.random.normal(size=len(index1))
A1= sigmoid(Z1)
df.iloc[index1, 6] = A1>=0.5


index2 = df.query('YOB<=2001 & YOB>1970').index
YOB = df.iloc[index2, 0]
YOB = (YOB-np.mean(YOB))/np.std(YOB)
Income = df.iloc[index2, 1]
Income = (Income-np.mean(Income))/np.std(Income)
Lon = df.iloc[index2, 2]
Lon = (Lon-np.mean(Lon))/np.std(Lon)
Lat = df.iloc[index2, 3]
Lat = (Lat-np.mean(Lat))/np.std(Lat)
Apl_Year = df.iloc[index2, 4]
Apl_Year = (Apl_Year-np.mean(Apl_Year))/np.std(Apl_Year)
gender = df.iloc[index2, 5]
gender = (gender-np.mean(gender))/np.std(gender)

Z2 = (-0.7)*Income+0.04*Lat+0.04*Lon-0.02*Apl_Year+0.1285*gender+np.random.normal(size=len(index2))
A2= sigmoid(Z2)
df.iloc[index2, 6] = A2>=0.5

index3 = df.query('YOB<=2017 & YOB>2001').index
YOB = df.iloc[index3, 0]
YOB = (YOB-np.mean(YOB))/np.std(YOB)
Income = df.iloc[index3, 1]
Income = (Income-np.mean(Income))/np.std(Income)
Lon = df.iloc[index3, 2]
Lon = (Lon-np.mean(Lon))/np.std(Lon)
Lat = df.iloc[index3, 3]
Lat = (Lat-np.mean(Lat))/np.std(Lat)
Apl_Year = df.iloc[index3, 4]
Apl_Year = (Apl_Year-np.mean(Apl_Year))/np.std(Apl_Year)
gender = df.iloc[index3, 5]
gender = (gender-np.mean(gender))/np.std(gender)

Z3 = 0.7*YOB+(-0.7)*Income+0.04*Lat+0.04*Lon-0.02*Apl_Year+0.1285*gender+np.random.normal(size=len(index3))
A3= sigmoid(Z3)
df.iloc[index3, 6] = A3>=0.5

#%%
df.to_csv('Applicants.csv')