import numpy as np
import pandas as pd
from tkinter import *

import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

dosya_adi = "Tromp Eğrisi.xlsx"
elek = pd.read_excel(dosya_adi,usecols="A:E")
malzemeler = pd.read_excel(dosya_adi,usecols="H:J")
malzemeler = malzemeler.dropna()

print(elek.head())
print(malzemeler.head())

ust_akımın_beslemeye_oranı = elek["Üst Akım Miktar (%)"]* malzemeler["Üst Akım Toplam Miktar (%)"].iloc[0]/ 100
alt_akımın_beslemeye_oranı = elek["Alt Akım Miktar (%)"]* malzemeler["Alt Akım Toplam Miktar (%)"].iloc[0]/ 100

elek["Üst Akımın Beslemeye Oranı"] = ust_akımın_beslemeye_oranı
elek["Alt Akımın Beslemeye Oranı"] = alt_akımın_beslemeye_oranı

geometrik_ort_boyut =np.sqrt((elek["Boyut(-)"] * elek["Boyut(+)"]))
elek["Geometrik Ortalama Boyut"] = geometrik_ort_boyut

elek["Partition (%)"] = (elek["Alt Akımın Beslemeye Oranı"] / (elek["Üst Akımın Beslemeye Oranı"] + elek["Alt Akımın Beslemeye Oranı"]) * 100)

print(elek.head())

veri = elek.sort_values("Geometrik Ortalama Boyut")
x = veri["Geometrik Ortalama Boyut"].to_numpy()
y = veri["Partition (%)"].to_numpy()


x_eksen = np.linspace(x.min(), x.max(), 1000)
f_tromp = PchipInterpolator(x, y)
y_eksen = f_tromp(x_eksen)

y_eksen_sinir = np.clip(y_eksen, 0, 100)


def dxx_hesapla(yuzde):
    return np.interp(yuzde, y_eksen_sinir, x_eksen)

def imperfection_hesapla():
    return (d75 - d25) / (2 * d50)

def imperfection_yorumla(I):

    if I < 0.4:
        return "İyi ayırma"
    elif I < 0.6:
        return "Orta seviyede ayırma"
    elif I < 0.8:
        return "Zayıf seviyede ayırma"

    else:
        return "Çok zayıf ayırma"



d25 = dxx_hesapla(25)
d50 = dxx_hesapla(50)
d75 = dxx_hesapla(75)
imperfection = imperfection_hesapla()
imperfection_yorum = imperfection_yorumla(imperfection)


print(f"d25 = {d25:.3f} mm")
print("d50 =", d50, "mm")
print("d75 =", d75, "mm")
print("I = ", imperfection)

plt.plot(x_eksen, y_eksen_sinir, linewidth=2)

plt.plot(x, y, "o", markersize=5)

def cizgi_ciz(x,y):
    plt.axhline(x, linestyle="--", linewidth=1)
    plt.axvline(y, linestyle="--", linewidth=1)

cizgi_ciz(25,d25)
cizgi_ciz(50,d50)
cizgi_ciz(75,d75)

window = Tk()
window.title("Tromp Eğrisi")
window.minsize(500,550)
window.config(bg="white")
window.config(pady=30,padx=30)

baslik=Label(window,text="Tromp Eğrisi",font=("Arial",12,"bold"))
baslik.grid(row=1,column=2,columnspan=2,pady=15)

d_degeri_label = Label(window,text="D değeri giriniz",font=("Arial",12))
d_degeri_label.grid(row=2,column=1,pady=15)

d_degeri_entry = Entry(window,width=50,font=("Arial",12))
d_degeri_entry.grid(row=2,column=2,pady=15)


def hesapla():
    try:
        yuzde = float(d_degeri_entry.get())
        if yuzde < 0 or yuzde > 100:
            sonuc_label.config(text="Lütfen 0-100 arasında bir değer girin.")
            return

        d_degeri = dxx_hesapla(yuzde)

        sonuc_label.config(
            text=f"D{yuzde:.0f} = {d_degeri:.2f} mm\n"
                f"D25 = {d25:.2f} mm\n"
                f"D50 = {d50:.2f} mm\n"
                f"D75 = {d75:.2f} mm\n"
                f"Imperfection: {imperfection:.2f}\n"
                f"{imperfection_yorum}",
            font=("Arial", 12)
        )

    except ValueError:
        sonuc_label.config(text="Lütfen geçerli bir sayı girin.")
        return

hesapla_button = Button(window,text="Hesapla",command=hesapla)
hesapla_button.grid(row=3,column=2,pady=15)

sonuc_label = Label(window,text="----------",font=("Arial",12))
sonuc_label.grid(row=4,column=1,pady=15,columnspan=3)

plt.show(block=False)
window.mainloop()