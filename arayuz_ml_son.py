import numpy as np
import pandas as pd
from tkinter import *
import xgboost as xgb
from tkinter import messagebox 
from xgboost import XGBRegressor
from tkinter.ttk import Combobox
from sklearn.model_selection import train_test_split


df = pd.read_excel("encod_data_set_ml_son1.xlsx")
df.drop("Unnamed: 0", axis=1, inplace=True)  # Gereksiz sütunu sil
df_1 = df.copy()


A = df_1.drop(["fiyat"], axis=1)
B = df_1["fiyat"]

# Eğitim ve test verilerini ayırma
Atrain, Atest, Btrain, Btest = train_test_split(A, B, test_size=0.25, random_state=1)

xgb = XGBRegressor(colsample_bytree=0.2, learning_rate=0.15, max_depth=2, n_estimators=1000)#c4
model_xgb = xgb.fit(Atrain, Btrain)

# Test verisi ile tahmin yap
a = model_xgb.predict(Atest)  # Tahminler
pencere = Tk()
pencere.title("Araba Fiyat Tahmini")

pencere.configure(background='#f7da05')
pencere.geometry("1530x850")
pencere.state("normal")

model_degerleri = {
    "Series_1": 0, "Series_2": 1, "Series_3": 2, "Series_4": 3, "Series_5": 4, "Series_6": 5,
    "Series_7": 6, "A_Class": 7, "a1": 8, "a3": 9, "a4": 10, "a5": 11, "a6": 12, "a7": 13,
    "a8": 14, "Amarok": 15, "Arteon": 16, "Auris": 17, "Avensis": 18, "Aygo": 19, "B_Class": 20,
    "b_MAX": 21, "Beetle": 22, "C_Class": 23, "c_HR": 24, "c_MAX": 25, "cC": 26, "CL_Class": 27,
    "CLA_Class": 28, "CLC_Class": 29, "CLS_Class": 30, "Caddy": 31, "Camry": 32, "Caravelle": 33,
    "Citigo": 34, "Corolla": 35, "E_Class": 36, "EcoSport": 37, "Edge": 38, "Eos": 39,
    "Fabia": 40, "Fiesta": 41, "Focus": 42, "GL_Class": 43, "GLA_Class": 44, "GLB_Class": 45,
    "GLC_Class": 46, "GLE_Class": 47, "GLS_Class": 48, "gT86": 49, "Galaxy": 50, "Golf": 51,
    "Golf_SV": 52, "Grand_C_MAX": 53, "Grand_Tourneo_Connect": 54, "Hilux": 55, "i10": 56,
    "i20": 57, "i30": 58, "i800": 60, "iX20": 61, "iX35": 62, "Ioniq": 63, "Jetta": 64, "kA": 65,
    "Ka_plus": 66, "Kamiq": 67, "Karoq": 68, "Kodiaq": 69, "Kona": 70, "Kuga": 71,
    "Land_Cruiser": 72, "M_Class": 73, "m2": 74, "m3": 75, "m4": 76, "m5": 77, "m6": 78,
    "Mondeo": 79, "Mustang": 80, "Octavia": 81, "PROACE_VERSO": 82, "Passat": 83, "Polo": 84,
    "Prius": 85, "Puma": 86, "q2": 87, "q3": 88, "q5": 89, "q7": 90, "rAV4": 91, "rS3": 92,
    "rS4": 93, "rS5": 94, "Rapid": 95, "S_Class": 96, "s_MAX": 97, "s3": 98, "s4": 99, "s8": 100,
    "sL_CLASS": 101, "lK": 102, "sQ5": 103, "Santa_Fe": 104, "cala": 105, "Scirocco": 106,
    "Superb": 107, "T_Cross": 108, "T_Roc": 109, "tT": 110, "Tiguan": 111, "Tiguan_Allspace": 112,
    "Touareg": 113, "Touran": 114, "tourneo_Connect": 115, "Tourneo_Custom": 116,
    "Tucson": 117, "x_CLASS": 118, "x1": 119, "x2": 120, "x3": 121, "x4": 122, "x5": 123,
    "x6": 124, "Yaris": 125, "Yeti": 126, "Yeti_Outdoor": 127, "z4": 128, "i3": 129
}

def model_kontrol():
    global model
    kontrol=0
    mod=model_kutu1.get()
    print(mod)
    kontrol = model_degerleri.get(mod)
    if kontrol!=0:
        model=model_degerleri.get(mod)
        print(model)
        mesaj()
        
    else:
        olumsuz()
def mesaj():
    messagebox.showinfo(title="Başarılı", message="Seçim başarılı")
def olumsuz():
    messagebox.showwarning(title="Dikkat", message="Seçim Yapmadınız")
def model_yapılandır():
    global model_kutu1
    model_label1 = Label(text = "Araç Modelini Seçiniz", font="helvetica 12",borderwidth=6)
    model_label1.place(x = 350, y = 250)
    model_kutu1 = Combobox(pencere, values = modeler )
    model_kutu1.place(x = 350, y = 300)
    model_buton1 = Button(pencere, text = "Seç", command = model_kontrol, font="helvetica 12",borderwidth=6)
    #print(model)
    model_buton1.place(x = 350, y = 350)
def marka_düzenle():
    global marka 
    global modeler
    marka_deger = marka_kutu.get()
    #if marka_deger=="": marka_deger="Audi" 
    if(marka_deger == "Audi"):
        marka = 0
        modeler = ["a3", "q3", "a1", "a4", "q2", "a5", "a6", "q5", "tT", "q7", "a7", "a8", "s3", "rS3", "sQ5", "rS4", "s4", "s8", "rS5"]
        mesaj()
        model_yapılandır()
    elif(marka_deger == "Bmw"):
        marka = 1
        modeler = [
        "Series_3", "Series_1", "Series_2", "Series_5", "Series_4", "x1", "x3", "x2", "x5", "x4", "z4", "Series_6", "Series_7", "i3", "x6", "m4", 
         "m3", "m6", "m5", "m2"]
        mesaj()
        model_yapılandır()
    elif(marka_deger == "Ford"):
        marka = 2
        modeler = [
    "Fiesta", "Focus", "Kuga", "EcoSport", "Ka_plus", "c_MAX","Mondeo", "b_MAX", "s_MAX", "Grand_C_MAX", "Galaxy", "Edge","kA", "Puma", "Tourneo_Custom", "Grand_Tourneo_Connect", "tourneo_Connect", "Mustang"
]
        mesaj()
        model_yapılandır()
        
    elif(marka_deger == "Hundai"):
        marka = 3
        modeler = [
    "Tucson", "i10", "i30", "i20", "Kona", "Ioniq",
    "Santa_Fe", "iX20", "iX35", "i800"
]
        model_yapılandır()
        mesaj()
    elif(marka_deger == "Mercedes-Benz"):
        marka = 4
        modeler = [
    "C_Class", "A_Class", "E_Class", "GLA_Class", "GLC_Class",
    "B_Class", "CL_Class", "GLE_Class", "sL_CLASS", "CLS_Class",
    "GL_Class", "CLA_Class", "slK", "M_Class", "S_Class",
    "x_CLASS", "GLB_Class", "GLS_Class", "CLC_Class"
]
        mesaj()
        model_yapılandır()
        
    elif(marka_deger == "Skoda"):
        marka = 5
        modeler = [
    "Fabia", "Octavia", "Superb", "Kodiaq", "Citigo", "Yeti_Outdoor",
    "Karoq", "scala", "Rapid", "Kamiq", "Yeti"
]
        mesaj()
        model_yapılandır()
        
    elif(marka_deger == "Toyota"):
        marka = 6
        modeler = [
    "Yaris", "Aygo", "Auris", "c_HR", "rAV4", "Corolla",
    "Prius", "Avensis", "Hilux", "gT86", "Land_Cruiser", "Camry"
]
        mesaj()
        model_yapılandır()
        
    elif(marka_deger == "Volkswagen"):
        marka = 7
        modeler = [
    "Golf", "Polo", "Tiguan", "Passat", "T_Roc", "Touran", "T_Cross",
    "Golf_SV", "Scirocco", "Arteon", "Touareg", "Tiguan_Allspace", 
    "cC", "Amarok", "Caddy", "Jetta", "Caravelle", "Eos"
]
        mesaj()
        model_yapılandır()
        
    else:
        olumsuz()
def km_düzenle():
    global km
    net_km = int(km_entry.get())
    if(net_km > 0):
        km = net_km
        mesaj()
        print(net_km)
    else:
        olumsuz()
def yıl_düzenle():
    global yıl
    yıl_deger = yıl_kutu.get()
    if(yıl_deger == "2023"):
        yıl = 19
        mesaj()
    elif(yıl_deger == "2022"):
        yıl = 18
        mesaj()
    elif(yıl_deger == "2021"):
        yıl = 17
        mesaj()
    elif(yıl_deger == "2020"):
        yıl = 16
        mesaj()
    elif(yıl_deger == "2019"):
        yıl = 15
        mesaj()
    elif(yıl_deger == "2018"):
        yıl = 14
        mesaj()
    elif(yıl_deger == "2017"):
        yıl = 13
        mesaj()
    elif(yıl_deger == "2016"):
        yıl = 12
        mesaj()
    elif(yıl_deger == "2015"):
        yıl = 11
        mesaj()
    elif(yıl_deger == "2014"):
        yıl = 10
        mesaj()
    elif(yıl_deger == "2013"):
        yıl = 9
        mesaj()
    elif(yıl_deger == "2012"):
        yıl = 8
        mesaj()
    elif(yıl_deger == "2011"):
        yıl = 7
        mesaj()
    elif(yıl_deger == "2010"):
        yıl = 6
        mesaj()
    elif(yıl_deger == "2009"):
        yıl = 5
        mesaj()
    elif(yıl_deger == "2008"):
        yıl = 4
        mesaj()
    elif(yıl_deger == "2007"):
        yıl = 3
        mesaj()
    elif(yıl_deger == "2006"):
        yıl = 2
        mesaj()
    elif(yıl_deger == "2005"):
        yıl = 1
        mesaj()
    elif(yıl_deger == "2004"):
        yıl = 0
        mesaj()
    else:
        olumsuz()       
def renk_düzenle():
    global renk
    renk_deger = renkler_kutu.get()
    if(renk_deger == "Bej"):
        renk = 0
        mesaj()
    elif(renk_deger == "Beyaz"):
        renk = 1
        mesaj()
    elif(renk_deger == "Bordo"):
        renk = 2
        mesaj()
    elif(renk_deger == "Füme"):
        renk = 3
        mesaj()
    elif(renk_deger == "Gri"):
        renk = 4
        mesaj()
    elif(renk_deger == "Gümüş_gri"):
        renk = 5
        mesaj()
    elif(renk_deger == "Kahverengi"):
        renk = 6
        mesaj()
    elif(renk_deger == "Kırmızı"):
        renk = 7
        mesaj()
    elif(renk_deger == "Lacivert"):
        renk = 8
        mesaj()
    elif(renk_deger == "Mavi"):
        renk = 9
        mesaj()
    elif(renk_deger == "Mor"):
        renk = 10
        mesaj()
    elif(renk_deger == "Sarı"):
        renk = 11
        mesaj()
    elif(renk_deger == "Siyah"):
        renk = 12
        mesaj()
    elif(renk_deger == "Turuncu"):
        renk = 13
        mesaj()
    elif(renk_deger == "Yeşil"):
        renk = 14
        mesaj()
    elif(renk_deger == "Şampanya"):
        renk = 15
        mesaj()
    else:
        olumsuz()       
def vites_düzenle():
    global vites
    vites_deger = vites_kutu.get()
    if(vites_deger == "Otomatik"):
        vites = 0
        mesaj()
    elif(vites_deger == "Manuel"):
        vites = 1
        mesaj()
    elif(vites_deger == "Diğer"):
        vites = 2
        mesaj()
    elif(vites_deger == "Yarı-otomatik"):
        vites = 3
        mesaj()
    else:
        olumsuz() 
def yakıt_düzenle():
    global yakıt
    yakıt_deger = yakıt_kutu.get()
    if(yakıt_deger == "Dizel"):
        yakıt = 0
        mesaj()
    elif(yakıt_deger == "Elektirik"):
        yakıt = 1
        mesaj()
    elif(yakıt_deger == "Hybrid"):
        yakıt = 2
        mesaj()
    elif(yakıt_deger == "Benzin"):
        yakıt = 4
        mesaj()
    else:
        olumsuz()
def motor_düzenle():
    global motor
    motor_ent = (motor_hacmi_kutu.get())
    print(motor_ent)
    if(motor_ent =="0.0-1.0"):
        motor = 1
        print(motor)
        mesaj()
    elif(motor_ent=="1.0-1.5"):
        motor=2
        mesaj()
    elif(motor_ent=="1.5-2.0"):
        motor=3
        mesaj()
    elif(motor_ent=="2.0-2.5"):
        motor=4
        mesaj()
    elif(motor_ent=="2.5-3.0"):
        motor=5
        mesaj()
    else:
        olumsuz()
def hasar_düzenle():
    global hasar
    hasar_deger = hasar_kutu.get()
    if(hasar_deger == "Evet"):
        hasar = 0
        mesaj()
    elif(hasar_deger == "Hayır"):
        hasar = 1
        mesaj()

    else:
        olumsuz()

baslık_label = Label(pencere, text = "ARAÇ FİYAT TAHMİNİ", font="helvetica 50",borderwidth=20, padx = 435, pady = 30,background = "#90cdf4")        
baslık_label.place(x = 10 ,y = 20)
marka_label = Label(text = "Araç Markası", font="helvetica 12",borderwidth=6)
marka_label.place(x = 150, y = 250)
marka=0
markalar = ["Audi","Bmw","Ford","Hundai","Mercedes-Benz","Skoda","Toyota","Volkswagen"]
marka_kutu = Combobox(pencere, values = markalar)
marka_kutu.place(x = 150,y = 300)
marka_buton = Button(pencere, text = "Seç", command = marka_düzenle, font="helvetica 12",borderwidth=6)
marka_buton.place(x = 150, y = 350)

model_label = Label(text = "Araç Modelini Seçiniz", font="helvetica 12",borderwidth=6)
model_label.place(x = 350, y = 250)
modeler="önce-marka-seç"
model_kutu = Combobox(pencere, values = modeler )
model_kutu.place(x = 350, y = 300)
model_buton = Button(pencere, text = "Seç", command = model_kontrol, font="helvetica 12",borderwidth=6)
model_buton.place(x = 350, y = 350)

yıl_label = Label(text = "Araç Yılı Seçiniz", font="helvetica 12",borderwidth=6)
yıl_label.place(x = 575, y = 250)
yıllar = ["2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
yıl_kutu = Combobox(pencere, values = yıllar)
yıl_kutu.place(x = 575, y = 300)
yıl_buton = Button(pencere, text = "Seç", command = yıl_düzenle, font="helvetica 12",borderwidth=6)
yıl_buton.place(x = 575, y = 350)

vites_label = Label(text = "Vites Tipi Seçiniz", font="helvetica 12",borderwidth=6)
vites_label.place(x = 775, y = 250)
vitesler = ["Manuel","Otomatik","Yarı-otomatik","Diğer"]
vites_kutu = Combobox(pencere, values = vitesler)
vites_kutu.place(x = 775, y = 300)
vites_buton = Button(pencere, text = "Seç", command = vites_düzenle, font="helvetica 12",borderwidth=6)
vites_buton.place(x = 775, y = 350)

yakıt_label = Label(pencere, text = "Yakıt Tipi Seçiniz", font="helvetica 12",borderwidth=6)
yakıt_label.place(x = 150, y = 450)
yakıtlar = ["Dizel","Benzin","Elektirik","Hybrid"]
yakıt_kutu = Combobox(pencere, values = yakıtlar)
yakıt_kutu.place(x = 150, y = 500)
yakıt_buton = Button(pencere, text = "Seç", command = yakıt_düzenle, font="helvetica 12",borderwidth=6)
yakıt_buton.place(x = 150, y = 550)

renk_label = Label(text = "Renk Seçiniz", font="helvetica 12",borderwidth=6)
renk_label.place(x = 350, y = 450)
renkler = ["Bej","Beyaz","Füme","Gri","Günüş_gri","Kahverengi","Kırmızı","Lacivert","Mavi","Mor","Sarı","Siyah","Turuncu","Yeşil","Şampanya"]
renkler_kutu = Combobox(pencere, values = renkler)
renkler_kutu.place(x = 350, y = 500)
renkler_buton = Button(pencere, text = "Seç", command = renk_düzenle, font="helvetica 12",borderwidth=6)
renkler_buton.place(x = 350, y = 550)

km_label = Label(text = "Km'yi Giriniz", font="helvetica 12",borderwidth=6)
km_label.place(x = 1000, y = 250)
km_entry = Entry()
km_entry.place(x = 1000, y = 300)
km_buton = Button(pencere, text = "Seç", command = km_düzenle, font="helvetica 12",borderwidth=6)
km_buton.place(x = 1000, y = 350)

motor_hacmi_label = Label(pencere, text = "Motorun Hacmini Girin", font="helvetica 12",borderwidth=6)
motor_hacmi_label.place(x = 1200, y = 250)
motorlar  = ["0.0-1.0","1.0-1.5","1.5-2.0","2.0-2.5","2.5-3.0"]
motor_hacmi_kutu = Combobox(pencere, values = motorlar)
motor_hacmi_kutu.place(x = 1200, y = 300)
motor_hacmi_buton = Button(pencere, text = "Seç", command = motor_düzenle, font="helvetica 12",borderwidth=6)
motor_hacmi_buton.place(x = 1200, y = 350)

hasar_label = Label(text = "Hasar Kaydı Varmı", font="helvetica 12",borderwidth=6)
hasar_label.place(x = 150, y = 650)
hasarler  = ["Evet","Hayır"]
hasar_kutu = Combobox(pencere, values = hasarler)
hasar_kutu.place(x = 150, y = 700)
hasar_buton = Button(pencere, text = "Seç", command = hasar_düzenle, font="helvetica 12",borderwidth=6)
hasar_buton.place(x = 150, y = 750)

def hesapla():
    global custom_prediction
    yeni_veri = np.array([[marka,model,yıl,vites,km ,yakıt,motor,hasar,renk]])
    # Özel girdiyi uygun formata getir (1, -1)
    yeni_veri = yeni_veri.reshape(1, 9)
    print(yeni_veri)
    # Özel girdiyi kullanarak tahmin yap
    custom_prediction = model_xgb.predict(yeni_veri)
    print("Özel girdinin tahmini:", custom_prediction)
    s1 = Label(pencere, text= custom_prediction, font="helvetica 12",borderwidth=6, padx = 200, pady = 40)
    s1.place(x = 540, y = 650)
    print()
    
    

    
custom_prediction=0
hesapla_buton = Button(pencere, text = "HESAPLA", command = hesapla, font="helvetica 15",borderwidth=60, padx = 100, pady = 40, background = "#fffffc")
hesapla_buton.place(x =550, y = 420)

s1 = Label(pencere, text= custom_prediction, font="helvetica 12",borderwidth=6, padx = 200, pady = 40)
s1.place(x = 540, y = 650)#s2 üstüne yazmak için


mainloop()
