Tromp Eğrisi

Python ile geliştirilmiş hidrosiklon Tromp Eğrisi ve performans analiz programıdır.

Program, elek analizi sonucunda elde edilen tane boyutu dağılımı ile hidrosiklonun üst akım ve alt akım dağılımlarını kullanarak, farklı tane boyutlarının hangi oranda alt akıma geçtiğini analiz eder.

Özellikler
Excel dosyasından veri okuma
Tane boyutu dağılımlarının işlenmesi
Üst akım ve alt akım dağılımlarının beslemeye göre hesaplanması
Tane boyutları için geometrik ortalama hesaplanması
Partition (%) değerlerinin hesaplanması
Tromp Eğrisi oluşturulması
PCHIP interpolasyonu ile eğrinin oluşturulması
D25, D50 ve D75 değerlerinin hesaplanması
Imperfection değerinin hesaplanması
Girilen herhangi bir D değeri için karşılık gelen tane boyutunun bulunması
Sonuçların grafik ve Tkinter arayüzü üzerinden gösterilmesi
Kullanılan Teknolojiler
Python
Pandas
NumPy
Matplotlib
SciPy
Tkinter
Excel
Excel Dosyasının Hazırlanması

Program verileri Tromp Eğrisi.xlsx dosyasından okur.

A sütunları

Bu bölümde elek analizi ve akım dağılımına ait veriler bulunur.

Sütun	Açıklama
Boyut(-)	Tane boyutu sınırı
Boyut(+)	Tane boyutu sınırı
Beslenen Miktar (%)	Beslemedeki tane boyutu dağılımı
Üst Akım Miktar (%)	Üst akımdaki tane boyutu dağılımı
Alt Akım Miktar (%)	Alt akımdaki tane boyutu dağılımı
H sütunları

Akımların toplam miktarlarını içerir.

Sütun	Açıklama
Üst Akım Toplam Miktar (%)	Üst akımın toplam beslemeye oranı
Alt Akım Toplam Miktar (%)	Alt akımın toplam beslemeye oranı

Program bu verileri kullanarak tane boyutu sınıflarının toplam besleme içerisindeki karşılıklarını hesaplar.

Program Nasıl Kullanılır?
1. Excel dosyasını hazırla

Tromp Eğrisi.xlsx dosyasını programla aynı klasöre koy.

Excel içerisindeki A ve H sütunlarına gerekli verileri gir.

2. Programı çalıştır

Terminal veya Komut İstemi üzerinden:

python "Tromp Eğrisi.py"
3. Tromp Eğrisini incele

Program Excel verilerini okuyarak:

Geometrik ortalama tane boyutlarını oluşturur.
Üst ve alt akım dağılımlarını beslemeye göre hesaplar.
Partition (%) değerlerini oluşturur.
Tane boyutu – Partition (%) ilişkisini kullanarak Tromp Eğrisini oluşturur.

Program tarafından oluşturulan hesaplama sütunları:

Üst Akımın Beslemeye Oranı
Alt Akımın Beslemeye Oranı
Geometrik Ortalama Boyut
Partition (%)

Bu sütunlar Excel'de önceden bulunmak zorunda değildir; Python kodu tarafından oluşturulur.

Tromp Eğrisi

Grafikte:

X ekseni: Geometrik ortalama tane boyutu
Y ekseni: Partition (%)

Eğri, deneysel veriler arasındaki geçişi göstermek amacıyla PCHIP interpolasyonu kullanılarak oluşturulur.

Programın oluşturduğu 1000 noktalı hesaplama aralığı, mevcut deneysel verilerin minimum ve maksimum tane boyutu arasında oluşturulur. Veri aralığının dışına ekstrapolasyon yapılmaz.

D25, D50 ve D75

Program Tromp Eğrisi üzerinden:

D25: Partition = %25
D50: Partition = %50
D75: Partition = %75

noktalarına karşılık gelen tane boyutlarını hesaplar.

Ayrıca kullanıcı arayüzden farklı bir Partition (%) değeri girerek o değere karşılık gelen tane boyutunu sorgulayabilir.

Örneğin:

D50 = 0.85 mm

sonucu, Tromp Eğrisi üzerinde Partition değerinin %50 olduğu noktadaki yaklaşık tane boyutunu ifade eder.

Imperfection

Program, D25, D50 ve D75 değerlerini kullanarak Imperfection değerini hesaplar.

Imperfection, hidrosiklonun tane boyutuna bağlı ayırma davranışını değerlendirmek için kullanılan bir performans göstergesidir.

Program ayrıca hesaplanan değere göre proje içerisinde tanımlanan yorum aralığını gösterir.

Grafik

Program aşağıdaki bilgileri aynı grafik üzerinde gösterir:

Deneysel veri noktaları
Tromp Eğrisi
D25
D50
D75

Bu sayede hidrosiklonun tane boyutuna bağlı ayırma davranışı görsel olarak incelenebilir.

Projenin Kullanım Amacı

Bu proje, cevher hazırlama mühendisliğinde hidrosiklon sınıflandırma performansının tane boyutuna bağlı olarak incelenmesini Python kullanılarak gerçekleştirmeyi amaçlamaktadır.

Proje kapsamında Excel tabanlı deneysel veriler Python ile işlenerek, mühendislik açısından anlamlı sınıflandırma göstergelerine dönüştürülmektedir.

Proje Yapısı
Tromp Eğrisi/
│
├── Tromp Eğrisi.py
└── Tromp Eğrisi.xlsx
Geliştirici

Doğukan Erbay
