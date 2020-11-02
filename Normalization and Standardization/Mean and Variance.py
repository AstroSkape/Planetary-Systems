import pandas as pd

df = pd.read_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv') #inplace of "D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv", add the directory of the file youre running
df.fillna(0,inplace=True)
print (df)

lst=list(df.columns)
mean_and_variance = {}
for i in lst:
    if (df[i].dtypes==float):
        me=df.mean()[i]
        va=df.var()[i]
        a=[round(me,5),round(va,5)]
        mean_and_variance[i]=a
print(mean_and_variance)

df2=pd.DataFrame(mean_and_variance)
df2.rename(index={0:'Mean'}, inplace=True)
df2.rename(index={1:'Variance'}, inplace=True)
df2.to_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\Normalization and Standardization\Mean and Variance.csv') #inplace of "D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv", add the directory of the folder you want ot save the CSV in
