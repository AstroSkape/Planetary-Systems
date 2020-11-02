from sklearn import preprocessing
#import numpy as np
import pandas as pd

df = pd.read_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\Normalization and Standardization\Mean and Variance.csv')

a=list(df.columns)
a.remove('Unnamed: 0')

df2=df.transpose()
df2.drop(["Unnamed: 0"], inplace = True)

normalized = preprocessing.normalize(df2)
df3=normalized.transpose()
df3=pd.DataFrame(df3)

x=0
for i in a:
    df3.rename(columns={x:i}, inplace=True)
    x=x+1
df3.rename(index={0:'Normalized Mean'}, inplace=True)
df3.rename(index={1:'Normalized Variance'}, inplace=True)
df3.to_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\Normalization and Standardization\Mean and Variance - Normalized.csv') #inplace of "D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv", add the directory of the folder you want ot save the CSV in

df3.to_csv('Mean and Variance.csv',mode = 'a', header = False) #Writing to same s=csv file