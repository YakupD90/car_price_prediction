
import pandas as pd
import xgboost  as xgb
from xgboost import XGBRegressor
import numpy as np
from sklearn import model_selection
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
from sklearn.model_selection import train_test_split,GridSearchCV,cross_val_score

df = pd.read_excel("encod_data_set_ml_son1.xlsx")
df.drop("Unnamed: 0", axis=1, inplace=True)#etiketde gelen sutunu sil
df_1=df.copy()
#print(df_1)

#değişkenler
A=df_1.drop(["fiyat"], axis=1)
B=df_1["fiyat"]

#eğitim vr test
Atrain, Atest, Btrain, Btest=train_test_split(A,B, test_size=0.3, random_state=1)
xgb=XGBRegressor(colsample_bytree=0.2, learning_rate=0.09, max_depth=3, n_estimators=100)
model_xgb=xgb.fit(Atrain,Btrain)
#yazdır
a=model_xgb.predict(Atest)#thm
"""

#                        marka, model, yıl, vites,   km,   yakıt, motor, hasar, renk
custom_input = np.array([[ 0,     9,    20,   0,    88000,   0,     2,     1,     3]])

# Ensure the custom input is in the same format as the training data
custom_input = custom_input.reshape(1, -1)

# Predict using the custom input
custom_prediction = model_xgb.predict(custom_input)

"""

b=Btest
"""
tahmin=[]
gercek=[]
hata_gercek=[]
hata_tahmin=[]

for i in a:
    tahmin.append(int(i))
#print("tahmin",tahmin)

for i in b:
    gercek.append(int(i))
#print("gerçek",gercek)

count=0
for i in range(len(gercek)):
     alt_sinir=gercek[i]-gercek[i]*10/100
     ust_sinir=gercek[i]+gercek[i]*10/100

     if tahmin[i] <= ust_sinir and tahmin[i] >= alt_sinir:
         count=count+1

     else:
         hata_gercek.append(gercek[i])
         hata_tahmin.append(tahmin[i])

         """

#print("\n Tahmin edilen ",len(tahmin)," adet aracın fiyatından \n",count," tanesinin fiyatını +-%25 sapma ile doğru buldu \n Geriye kalan ",len(tahmin)-count," sapmanın üzerinde\n")
#print(hata_gercek)
#print(hata_tahmin)
print("XGBoost")
print("Mean Squared Error:", mean_squared_error(b, a))
print("R2 Score:", r2_score(b, a))
print()

