from sklearn import preprocessing
import pandas as pd

df = pd.read_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv') # In place of "D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv", add the directory of the file youre running
df.drop('Unnamed: 0',axis = 1, inplace = True)
df.fillna(0,inplace=True)

lst=list(df.columns)
for i in lst:
    if (df[i].dtypes!=float):
        df.drop(i,axis=1, inplace= True)

lst=list(df.columns)

normalized = preprocessing.normalize(df)
df2 = pd.DataFrame(normalized)

x=0
for i in lst:
    df2.rename(columns={x:i}, inplace=True)
    x=x+1
    
df2.to_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\Normalization and Standardization\Normalised Data.csv')

#mv = {}
#for i in lst:
#    me=df2.mean()[i]
#    va=df2.var()[i]
#    a=[round(me,5),round(va,5)]       # THIS IS FOR FINDING NORMALISED MEAN AND VARIANCE (NOT REQUIRED)
#    mv[i]=a
#  
#df3=pd.DataFrame(mv)