import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import chi2 
from sklearn import preprocessing
from scipy import stats

df = pd.read_csv("Applicants.csv")
# features we want to look at
features = ["Income", "Lon","Lat","YOB","gender","Apl_Year"]
#x = features
x = df.loc[:,features].values
#standarize features
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
X = scaler.fit_transform(x)
#y = target
y = df.loc[:,['Accepted']].values

id = df.loc[:,["ID"]].values

print(df.head())

test = SelectKBest(score_func=chi2, k="all")
fit = test.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(features)
print(dfcolumns)
scores = pd.concat([dfcolumns, dfscores], axis=1)
scores.columns = ["features","scores"]
print(scores)

prob = []
for scores in range(len(y)):
    sc = 0
    for feature in range(len(features)):
        sc += X[scores][feature]*dfscores.values[feature]
    prob.append(sc)

dfprob = pd.DataFrame(prob)
probability = pd.concat([pd.DataFrame(id), pd.DataFrame(y), dfprob], axis=1)
probability.columns = ["ID","Accepted","Score"]
print(probability)
