import pandas as pd
import numpy as np
import seaborn as sns

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

target = train['target']
train.drop(columns=['ID_code','target'],axis=1,inplace=True)

#Missing value in each column
train.isnull().sum().sum()
train.describe()
train.dtypes

#
e1 = sns.distplot(train['var_10'],rug=True)
