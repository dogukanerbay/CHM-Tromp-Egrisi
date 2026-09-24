Tromp Eğrisi

Python ile geliştirilmiş hidrosiklon Tromp Eğrisi analiz programı. Program, elek analizi ve akım dağılımı verilerinden yararlanarak hidrosiklonun tane boyutuna bağlı ayırma davranışını analiz eder.

Program; Partition (dağılım/ayırma) eğrisi, d25, d50, d75, Imperfection (ayrım hassasiyeti) ve kullanıcı tarafından girilen herhangi bir D değeri için karşılık gelen tane boyutunu hesaplayabilir.

Özellikler
Excel dosyasından deneysel verileri okuma
Besleme, üst akım ve alt akım miktarlarını kullanarak hesaplama
Her tane boyutu aralığı için geometrik ortalama tane boyutu hesaplama
Partition (%) hesabı
PCHIP interpolasyonu ile düzgün Tromp eğrisi oluşturma
d25, d50 ve d75 hesaplama
Kullanıcı tarafından girilen herhangi bir D değeri için tane boyutu hesaplama
Imperfection hesabı
Imperfection değerine göre proje kapsamında ayırma yorumu
Deneysel noktaların Tromp eğrisi üzerinde gösterilmesi
Matplotlib ile grafik oluşturma
Tkinter ile basit kullanıcı arayüzü
Kullanılan Teknolojiler
Python
NumPy
Pandas
Matplotlib
SciPy
PchipInterpolator
Tkinter
Proje Akışı

Programın temel çalışma mantığı:

Excel Verileri
      ↓
Elek Analizi
      ↓
Üst Akım / Besleme Oranı
      ↓
Alt Akım / Besleme Oranı
      ↓
Partition (%)
      ↓
Tromp Eğrisi
      ↓
d25 - d50 - d75
      ↓
Imperfection
Excel Dosya Yapısı

Program Tromp Eğrisi.xlsx isimli Excel dosyasından veri okumaktadır.

A – Elek Analizi Tablosu
Boyut(-)	Boyut(+)	Beslenen Miktar (%)	Üst Akım Miktar (%)	Alt Akım Miktar (%)
0.725	0.500	15.5	0.0	24.5
0.500	0.425	14.1	1.2	22.2
0.425	0.300	12.7	3.2	18.1
...	...	...	...	...
H – Akım Miktarları
Besleme Toplam Miktarı (%)	Üst Akım Toplam Miktarı (%)	Alt Akım Toplam Miktarı (%)
100	36.5	63.5

Program Excel dosyasını şu şekilde okumaktadır:

elek = pd.read_excel(dosya_adi, usecols="A:E")
malzemeler = pd.read_excel(dosya_adi, usecols="H:J")
Hesaplamalar
1. Üst Akımın Beslemeye Oranı

Her tane boyutu fraksiyonu için üst akıma giden miktar:

[
U_i =
\frac{u_i \times U}{100}
]

Burada:

(u_i): ilgili tane boyutunun üst akımdaki yüzdesi
(U): toplam üst akım miktarı

Python:

ust_akımın_beslemeye_oranı = (
    elek["Üst Akım Miktar (%)"]
    * malzemeler["Üst Akım Toplam Miktar (%)"].iloc[0]
    / 100
)
2. Alt Akımın Beslemeye Oranı

Her tane boyutu fraksiyonu için alt akıma giden miktar:

[
L_i =
\frac{l_i \times L}{100}
]

Python:

alt_akımın_beslemeye_oranı = (
    elek["Alt Akım Miktar (%)"]
    * malzemeler["Alt Akım Toplam Miktar (%)"].iloc[0]
    / 100
)
3. Geometrik Ortalama Tane Boyutu

Her elek aralığı için temsilci tane boyutu geometrik ortalama ile hesaplanmaktadır:

[
d_i = \sqrt{d_{(-)}d_{(+)}}
]

Python:

geometrik_ort_boyut = np.sqrt(
    elek["Boyut(-)"] * elek["Boyut(+)"]
)

elek["Geometrik Ortalama Boyut"] = geometrik_ort_boyut
4. Partition Hesabı

Tromp eğrisinin temel parametresi olan Partition değeri:

[
P_i =
\frac{L_i}
{U_i + L_i}
\times100
]

şeklinde hesaplanmaktadır.

Python:

elek["Partition (%)"] = (
    elek["Alt Akımın Beslemeye Oranı"]
    /
    (
        elek["Üst Akımın Beslemeye Oranı"]
        + elek["Alt Akımın Beslemeye Oranı"]
    )
    * 100
)

Partition değeri, belirli bir tane boyutundaki malzemenin alt akıma gitme eğilimini gösterir.

Tromp Eğrisi

Deneysel verilerden elde edilen noktaların arasındaki eğriyi daha düzgün göstermek amacıyla PchipInterpolator kullanılmaktadır.

veri = elek.sort_values("Geometrik Ortalama Boyut")

x = veri["Geometrik Ortalama Boyut"].to_numpy()
y = veri["Partition (%)"].to_numpy()

x_eksen = np.linspace(x.min(), x.max(), 1000)

f_tromp = PchipInterpolator(x, y)
y_eksen = f_tromp(x_eksen)

y_eksen_sinir = np.clip(y_eksen, 0, 100)

Burada:

X ekseni: Tane boyutu (mm)
Y ekseni: Partition (%)

Deneysel noktalar ayrıca grafik üzerinde gösterilmektedir.

d25, d50 ve d75

Tromp eğrisi üzerinden belirli Partition değerlerine karşılık gelen tane boyutları hesaplanır:

d25: Partition = %25
d50: Partition = %50
d75: Partition = %75

Programda:

d25 = dxx_hesapla(25)
d50 = dxx_hesapla(50)
d75 = dxx_hesapla(75)

şeklinde hesaplanmaktadır.

Bu değerler, ayırmanın tane boyutuna bağlı olarak nasıl gerçekleştiğinin değerlendirilmesinde kullanılır.

Imperfection

Programda ayrım hassasiyetini ifade etmek için:

[
I =
\frac{d_{75}-d_{25}}
{2d_{50}}
]

formülü kullanılmaktadır.

Python:

def imperfection_hesapla():
    return (d75 - d25) / (2 * d50)

Imperfection değeri, d25 ile d75 arasındaki ayırma bölgesinin d50'ye göre genişliğini ifade eder.

Not: Imperfection için farklı kaynaklarda farklı tanımlar ve değerlendirme yaklaşımları bulunabilir. Bu projede yukarıdaki formül kullanılmıştır.

Imperfection Yorumu

Projede sonuçları kolay yorumlamak amacıyla aşağıdaki eşikler kullanılmıştır:

def imperfection_yorumla(I):

    if I < 0.4:
        return "İyi ayırma"
    elif I < 0.6:
        return "Orta seviyede ayırma"
    elif I < 0.8:
        return "Zayıf seviyede ayırma"
    else:
        return "Çok zayıf ayırma"

Bu sınıflandırma projenin yorumlama yaklaşımıdır ve evrensel bir standart olarak değerlendirilmemelidir.

Kullanıcı Arayüzü

Program Tkinter kullanılarak basit bir grafik arayüzüne sahiptir.

Kullanıcı:

D değerini girer.
Hesapla butonuna basar.
Girilen Partition değerine karşılık gelen tane boyutu hesaplanır.
Aynı ekranda d25, d50, d75 ve Imperfection sonuçları gösterilir.

Örnek:

D değeri giriniz: 50

D50 = 0.12 mm
D25 = 0.07 mm
D50 = 0.12 mm
D75 = 0.23 mm
Imperfection: 0.64
Zayıf seviyede ayırma
Kurulum

Python'un bilgisayarınızda kurulu olması gerekir.

Gerekli kütüphaneleri yüklemek için:

pip install numpy pandas matplotlib scipy

tkinter Python'un standart kütüphanelerinden biridir. Windows üzerinde Python kurulumu ile birlikte kullanılabilir.

Çalıştırma

Excel dosyasını Python dosyası ile aynı klasöre koyun:

Proje/
│
├── Tromp Eğrisi.py
└── Tromp Eğrisi.xlsx

Ardından:

python "Tromp Eğrisi.py"

komutuyla programı çalıştırabilirsiniz.

Örnek Çıktılar

Program aşağıdaki parametreleri üretir:

d25
d50
d75
Imperfection

Ayrıca Tromp eğrisi üzerinde:

deneysel noktalar,
d25 çizgisi,
d50 çizgisi,
d75 çizgisi

gösterilmektedir.

Projenin Amacı

Bu proje, cevher hazırlama ve hidrosiklon performans analizinde kullanılan Tromp eğrisi yaklaşımının Python ile uygulanmasını amaçlamaktadır.

Proje kapsamında:

deneysel tane boyutu verilerinin işlenmesi,
akım dağılımlarının hesaplanması,
partition değerlerinin belirlenmesi,
Tromp eğrisinin oluşturulması,
kesim boyutlarının hesaplanması,
ayrım hassasiyetinin değerlendirilmesi

otomatik hale getirilmiştir.

Gelecekte Eklenebilecek Özellikler
Logaritmik tane boyutu ekseni
Su/katı oranı hesabı
Su bypassı (short-circuit) düzeltmesi
Düzeltilmiş Tromp eğrisi
d50'nin otomatik gösterimi
Grafik üzerinde d25, d50 ve d75 etiketleri
Excel'e sonuçların geri kaydedilmesi
Sonuç raporu oluşturma
Tkinter arayüzünde grafik gösterimi
Geliştirici

Doğukan Erbay
