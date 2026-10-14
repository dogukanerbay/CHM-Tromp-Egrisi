Tromp Eğrisi Analizi

Python ile geliştirilmiş hidrosiklon sınıflandırma performansı ve Tromp Eğrisi analiz programıdır.

Program, elek analizi sonucunda elde edilen tane boyutu dağılımını ve hidrosiklonun üst akım (overflow) ile alt akım (underflow) verilerini kullanarak farklı tane boyutlarının hangi oranda alt akıma geçtiğini analiz eder.

Proje kapsamında Excel tabanlı veriler Python ile işlenerek tane boyutu–Partition ilişkisi oluşturulur. PCHIP interpolasyonu ile Tromp Eğrisi çizilir; D25, D50, D75 ve Imperfection gibi sınıflandırma performansı göstergeleri hesaplanır.

Özellikler

Excel dosyasından deneysel veri okuma

Tane boyutu dağılımlarının işlenmesi

Üst akım ve alt akım dağılımlarının besleme bazında hesaplanması

Tane boyutu sınıfları için geometrik ortalama hesaplanması

Partition (%) değerlerinin hesaplanması

PCHIP interpolasyonu ile Tromp Eğrisi oluşturulması

D25, D50 ve D75 değerlerinin hesaplanması

Imperfection değerinin hesaplanması

Kullanıcının girdiği herhangi bir Partition (%) değeri için karşılık gelen tane boyutunun bulunması

Deneysel verilerin ve hesaplanan sonuçların grafik üzerinde gösterilmesi

Tkinter tabanlı kullanıcı arayüzü

Kullanılan Teknolojiler

Python – Hesaplamalar ve uygulama mantığı

Pandas – Excel verilerinin okunması ve işlenmesi

NumPy – Sayısal hesaplamalar

Matplotlib – Tromp Eğrisi ve sonuç grafiklerinin oluşturulması

SciPy – PCHIP interpolasyonu ve eğri hesaplamaları

Tkinter – Grafiksel kullanıcı arayüzü

Excel – Deneysel verilerin saklanması

Excel Dosyasının Hazırlanması

Program, verileri Tromp Eğrisi.xlsx dosyasından okur. Excel dosyası, Python dosyasıyla aynı klasörde bulunmalıdır.

1. Tane Boyutu ve Akım Dağılımı Verileri

Excel tablosunda aşağıdaki sütunlar bulunmalıdır:

Sütun

Açıklama

Boyut (-)

Tane boyutu sınıfının alt sınırı

Boyut (+)

Tane boyutu sınıfının üst sınırı

Beslenen Miktar (%)

Beslemedeki tane boyutu sınıfının dağılımı

Üst Akım Miktar (%)

Üst akımdaki tane boyutu sınıfının dağılımı

Alt Akım Miktar (%)

Alt akımdaki tane boyutu sınıfının dağılımı

Tane boyutu dağılımlarının ve akım miktarlarının hangi temelde ifade edildiği tutarlı olmalıdır. Boyut değerleri için aynı ölçü birimi kullanılmalıdır.

2. Akımların Toplam Miktarları

Excel dosyasının H sütunundaki ilgili alanlarda akımların toplam beslemeye oranları bulunmalıdır.

Alan

Açıklama

Üst Akım Toplam Miktar (%)

Üst akımın toplam beslemeye oranı

Alt Akım Toplam Miktar (%)

Alt akımın toplam beslemeye oranı

Program, tane boyutu dağılımlarıyla akımların toplam miktarlarını birlikte kullanarak ilgili boyut sınıflarının besleme içerisindeki karşılıklarını hesaplar.

Programın Çalıştırılması

1. Dosyaları Hazırlama

Aşağıdaki dosyaların aynı klasörde bulunduğundan emin olun:

Tromp Eğrisi/
├── Tromp Eğrisi.py
├── Tromp Eğrisi.xlsx
└── README.md

2. Gerekli Kütüphaneleri Kurma

Terminal veya Komut İstemi üzerinden aşağıdaki komutu çalıştırın:

pip install pandas numpy matplotlib scipy

Tkinter, standart Python kurulumlarının çoğunda yerleşik olarak gelir.

3. Programı Çalıştırma

Terminal veya Komut İstemi üzerinden proje klasörüne gidin ve şu komutu çalıştırın:

python "Tromp Eğrisi.py"

Hesaplama Süreci

Program, Excel dosyasındaki verileri okuyarak aşağıdaki işlemleri gerçekleştirir:

Tane boyutu ve akım dağılımı verilerini alır.

Üst akım ve alt akımın tane boyutu dağılımlarını, toplam akım miktarlarını dikkate alarak besleme bazında değerlendirir.

Her tane boyutu sınıfı için geometrik ortalama boyutu hesaplar.

Her boyut sınıfının alt akıma geçiş oranını ifade eden Partition (%) değerlerini hesaplar.

Tane boyutu ile Partition (%) arasındaki ilişkiyi oluşturur.

PCHIP interpolasyonu kullanarak deneysel noktalar arasında bir Tromp Eğrisi oluşturur.

D25, D50 ve D75 değerlerini hesaplar.

D25, D50 ve D75 değerlerini kullanarak Imperfection değerini hesaplar.

Program Tarafından Oluşturulan Hesaplama Sütunları

Bu sütunların Excel dosyasında önceden bulunması gerekmez. İlgili hesaplamalar Python kodu tarafından yapılır.

Hesaplama Sütunu

Açıklama

Üst Akımın Beslemeye Oranı

İlgili tane boyutu sınıfındaki üst akım miktarının besleme ile karşılaştırılması

Alt Akımın Beslemeye Oranı

İlgili tane boyutu sınıfındaki alt akım miktarının besleme ile karşılaştırılması

Geometrik Ortalama Boyut

Tane boyutu sınıfının alt ve üst sınırlarından hesaplanan temsilî boyut

Partition (%)

İlgili tane boyutu sınıfının alt akıma geçiş oranı

Geometrik ortalama tane boyutu aşağıdaki şekilde hesaplanır:

[
d_g=\sqrt{d_{-}\times d_{+}}
]

Burada (d_{-}) tane boyutu sınıfının alt sınırını, (d_{+}) ise üst sınırını ifade eder.

Tromp Eğrisi

Tromp Eğrisi, hidrosiklonun farklı tane boyutlarını alt ve üst akımlar arasında nasıl ayırdığını gösterir.

Grafikte:

X ekseni: Geometrik ortalama tane boyutu

Y ekseni: Partition (%)

Deneysel noktalar: Hesaplanan Partition değerleri

Tromp Eğrisi: PCHIP interpolasyonu ile oluşturulan eğri

PCHIP interpolasyonu, deneysel noktalar arasında yumuşak bir geçiş oluşturarak eğrinin incelenmesini sağlar.

Grafik için 1000 noktalı bir hesaplama aralığı oluşturulur. Bu aralık, mevcut deneysel verilerin minimum ve maksimum tane boyutları arasında kalır. Veri aralığının dışına ekstrapolasyon yapılmaz.

D25, D50 ve D75

Tromp Eğrisi üzerinden belirli Partition değerlerine karşılık gelen tane boyutları hesaplanır.

Parametre

Açıklama

D25

Partition değerinin %25 olduğu tane boyutu

D50

Partition değerinin %50 olduğu tane boyutu

D75

Partition değerinin %75 olduğu tane boyutu

D50, hidrosiklon performansını değerlendirirken kullanılan temel göstergelerden biridir. Eğri üzerindeki Partition değerinin %50 olduğu tane boyutunu ifade eder.

Örneğin, programın D50 = 0.85 mm sonucu vermesi, hesaplanan Tromp Eğrisi üzerinde %50 Partition değerine karşılık gelen tane boyutunun yaklaşık 0,85 mm olduğu anlamına gelir.

Kullanıcı arayüz üzerinden farklı bir Partition (%) değeri girerek ilgili tane boyutunu da sorgulayabilir.

Imperfection

Imperfection, hidrosiklonun tane boyutuna bağlı ayırma keskinliğini değerlendirmek için kullanılan bir göstergedir.

Program, D25, D50 ve D75 değerleri üzerinden aşağıdaki bağıntıyı kullanarak Imperfection değerini hesaplar:

[
I=\frac{D_{75}-D_{25}}{2D_{50}}
]

Genel olarak daha düşük Imperfection değeri, daha keskin bir boyut bazlı ayırmaya işaret eder.

Program ayrıca hesaplanan Imperfection değerini proje içerisinde tanımlanan yorum aralıklarına göre değerlendirir. Bu yorum aralıkları, uygulamada kullanılan kriterlere göre ele alınmalıdır.

Grafik ve Kullanıcı Arayüzü

Programın oluşturduğu grafik üzerinde aşağıdaki bilgiler birlikte gösterilir:

Deneysel Partition noktaları

PCHIP ile oluşturulan Tromp Eğrisi

D25 noktası

D50 noktası

D75 noktası

Tkinter arayüzü üzerinden hesaplama sonuçları görüntülenebilir ve kullanıcı tarafından girilen Partition değerine karşılık gelen tane boyutu sorgulanabilir.

Projenin Kullanım Amacı

Bu proje, cevher hazırlama mühendisliğinde hidrosiklon sınıflandırma performansının tane boyutuna bağlı olarak incelenmesini amaçlamaktadır.

Excel tabanlı deneysel verilerin Python ile işlenmesi sayesinde, tane boyutu dağılımları ve akım miktarları mühendislik açısından anlamlı sınıflandırma performansı göstergelerine dönüştürülür.

Proje; veri işleme, sayısal hesaplama, interpolasyon ve grafik oluşturma yöntemlerinin cevher hazırlama uygulamalarında kullanımını göstermektedir.

Proje Yapısı

Tromp Eğrisi/
├── Tromp Eğrisi.py
├── Tromp Eğrisi.xlsx
└── README.md

Geliştirici

Doğukan Erbay
