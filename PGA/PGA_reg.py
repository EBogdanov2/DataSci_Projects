import numpy as np 
import pandas as pd 

from sklearn import linear_model
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

train = pd.read_csv('train.csv')  

def regtransform(df):
    df.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
    df.drop(["a"], axis=1, inplace=True)  
    del df['player_name']
    del df['tournament'] 

    df = df.apply(lambda x: x/100 if x.name not in ['Official Money - (MONEY)'] else x)
    df = df.dropna()
    return df

df_train = regtransform(train)

X = df_train.loc[:, df_train.columns != 'Official Money - (MONEY)'] 
y = df_train['Official Money - (MONEY)']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
lm = linear_model.LinearRegression()
model= lm.fit(X_train, y_train)
predictions = lm.predict(X_test) 

coefs = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("Score:", model.score(X_test, y_test))
print(coefs)