#from sklearn.preprocessing import normalize
from sklearn import preprocessing
import scipy.stats as st
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv(r'D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\Normalization and Standardization\Normalised Data.csv') # In place of "D:\Engineering\Sem - 3\Statistics for Data Science\SDS Project\cleaned-without missing.csv", add the directory of the file youre running
df.drop('Unnamed: 0',axis = 1, inplace = True)

def normalise(data):
    from sklearn.preprocessing import MinMaxScaler
    data=np.array(data)
    scale = MinMaxScaler()
    normalized = preprocessing.normalize(data.reshape(-1,1))
    scaled=scale.fit_transform(normalized)
    sns.distplot(scaled)
    print(scaled.mean())
    print(scaled.var())        # For printing individial normal means and variance, include this and comment me,va
    global me,va
    me=scaled.mean()
    va=scaled.var()
    return scaled

#normalise(df['st_teff'])                       # For individual column normalisation
#st.probplot(df['st_teff'],plot=plt)            # For individual graphs replace 'st_teff with any other column
       
lst=list(df.columns)
nmv={}
for i in lst:
    normalise(df[i])        # Normalised mean and variance
    x=[me,va]
    nmv[i]=x
    
df2=pd.DataFrame(nmv)

#df2.plot(x =0, y=1, kind = 'scatter') # Use scatter, box, hist, line // df2 for mean and normal, change to df fo dataset

for i in lst:
    st.probplot(df[i],plot=plt)

#lst2=list(df2.columns)
#for i in lst2:
#    st.probplot(df2[i],plot=plt)
            