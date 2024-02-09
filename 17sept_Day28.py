'''import seaborn as sns
fmri=sns.load_dataset("fmri")
print(fmri)'''
import pandas as pd
link="C:\\Users\\I-Net Computer\\Downloads\\1_Data_Preprocessing.csv"
df=pd.read_csv(link)
print(df)
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
print(x)
print(y)
#Missing
from sklearn.impute import SimpleImputer
import numpy as np
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)
#Handling Categorical Values
print("Before Handling: \n",x[:,0])
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
lc=LabelEncoder()
x[:,0]=lc.fit_transform(x[:,0])
print("After Encoding:\n",x[:,0])
from sklearn.compose import  ColumnTransformer
trans=ColumnTransformer([('one_hot_encoder' ,OneHotEncoder(),[0])],remainder="passthrough")
x=trans.fit_transform(x)
x=x[:,1:]#encoded column 1 delete
print(x)

#Break it into train and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

#Scaling
from sklearn.preprocessing import  StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
print("X_train:\n",x_train)
print("X_test:\n",x_test)
print("y_train:\n",y_train)
print("y_test:\n",y_test)
