#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:59:43 2019

@author: wumeiqi
"""



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#%%
df = pd.read_csv('Applicants.csv')
#%% Distribution of Age of Applicant
mpl.rcParams['figure.figsize'] = 6,5
Age = 2019 - df.YOB
sns.distplot(Age, bins=20)
plt.title('Age Distribution',size = 20)
plt.xlabel('Age', size = 20)
plt.show()
# plt.savefig('Age_distribution.png')
#%% Acceptance v.s age
plt.rcParams['figure.figsize'] = 15, 5
mpl.rcParams['font.size'] = 10.0
age = 2019-df['YOB']
accept = df['Accepted']

x = pd.crosstab(age, df['Accepted'])
x.div(x.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True,color=['red','yellow'])
plt.title('Acceptance vs age', fontweight = 30, fontsize = 20)
plt.xlabel('Age', fontsize = 20)
plt.legend(loc="upper right")
plt.show()

#%% Pie chart of gender
labels = ['male', 'female']
sizes = [df[df['gender']==0].shape[0], df[df['gender']==1].shape[0]]
fig1, ax1 = plt.subplots()
mpl.rcParams['figure.figsize'] = 8,7
mpl.rcParams['font.size'] = 20.0
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.title('Percentage of Females and Males ',size = 20)
plt.show()

#%% Acceptance v.s gender
plt.rcParams['figure.figsize'] = 6,5
gender2 = df['gender']
gender2[gender2==1]='Female'
gender2[gender2==0]='Male'
x = pd.crosstab(gender2, df['Accepted'])
x.div(x.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True,color=['red','yellow'])
plt.title('Acceptance vs gender', fontweight = 30, fontsize = 20)
plt.legend(loc="upper right")
plt.show()


#%% Acceptance v.s Location
plt.rcParams['figure.figsize'] = 6,5 
x = pd.crosstab(df['Lon_lat'], df['Accepted'])
x.div(x.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True,color=['red','yellow'])
plt.title('Acceptance vs gender', fontweight = 30, fontsize = 20)
#plt.legend(loc="upper right")
plt.xlabel('Longitude, Latitude')
plt.show()

#%% Age v.s. Income
mpl.rcParams['figure.figsize'] = 6, 5
index1 = df.query('Accepted==True').index
index1 = np.random.choice(index1, size=int(len(index1)/10))
age1 = 2019-df.iloc[index1, 1]
Income1 = df.iloc[index1, 2]
l1 = plt.scatter(age1, Income1, color='Red')


index2 = df.query('Accepted==False').index
index2 = np.random.choice(index2, size=int(len(index2)/10))
age2 = 2019-df.iloc[index2, 1]
Income2 = df.iloc[index2, 2]
l2 = plt.scatter(age2, Income2, color='Blue')

plt.legend((l1, l2), ('Accepted', 'Not accepted'),loc='upper left')
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()





