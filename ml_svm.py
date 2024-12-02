import pandas as pd
import numpy as np 
from sklearn import datasets 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC,SVR
from sklearn.metrics import classification_report, confusion_matrix,mean_squared_error,r2_score

df=pd.read_excel("encod_data_set_ml_son1.xlsx")
df.drop("Unnamed: 0", axis=1 , inplace=True)

bagımsız = df.drop(["fiyat"],axis=1)
bagımlı = df["fiyat"]

bagımsız_train, bagımsız_test, bagımlı_train, bagımlı_test = train_test_split(bagımsız,bagımlı,test_size=0.3, random_state=10)#1
scaler=StandardScaler()
bagımsız_train=scaler.fit_transform(bagımsız_train)
bagımsız_test=scaler.transform(bagımsız_test)

svm_model=SVR(kernel='linear',gamma='scale',C=10)
svm_model.fit(bagımsız_train,bagımlı_train)

tahmin=svm_model.predict(bagımsız_test)
print("Destek Vektör Makinesi")
print("Mean Squared Error:", mean_squared_error(bagımlı_test, tahmin))
print("r2 score",r2_score(bagımlı_test,tahmin))
print()

