# Tromp Eğrisi Analizi

Python ile geliştirilmiş hidrosiklon Tromp Eğrisi ve performans analiz programıdır.

Program, elek analizi sonucunda elde edilen tane boyutu dağılımı ile hidrosiklonun üst akım (overflow) ve alt akım (underflow) verilerini kullanarak, farklı tane boyutlarının hangi oranda alt akıma geçtiğini analiz eder.

## Özellikler

- Excel dosyasından veri okuma
- Tane boyutu dağılımlarının işlenmesi
- Üst akım ve alt akım dağılımlarının beslemeye göre hesaplanması
- Tane boyutu sınıfları için geometrik ortalama hesaplanması
- Partition (%) değerlerinin hesaplanması
- PCHIP interpolasyonu ile Tromp Eğrisi oluşturulması
- D25, D50 ve D75 değerlerinin hesaplanması
- Imperfection değerinin hesaplanması
- Girilen herhangi bir Partition (%) değeri için karşılık gelen tane boyutunun bulunması
- Sonuçların grafik üzerinde gösterilmesi
- Tkinter tabanlı grafiksel kullanıcı arayüzü

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Tkinter
- Microsoft Excel

## Excel Dosyasının Hazırlanması

Program, verileri `Tromp Eğrisi.xlsx` dosyasından okur. Excel dosyası, Python dosyasıyla aynı klasörde bulunmalıdır.

### Tane Boyutu ve Akım Dağılımı Verileri

| Sütun | Açıklama |
|---|---|
| Boyut (-) | Tane boyutu sınıfının alt sınırı |
| Boyut (+) | Tane boyutu sınıfının üst sınırı |
| Beslenen Miktar (%) | Beslemedeki tane boyutu dağılımı |
| Üst Akım Miktar (%) | Üst akımdaki tane boyutu dağılımı |
| Alt Akım Miktar (%) | Alt akımdaki tane boyutu dağılımı |

### Toplam Akım Miktarları

| Alan | Açıklama |
|---|---|
| Üst Akım Toplam Miktar (%) | Üst akımın toplam beslemeye oranı |
| Alt Akım Toplam Miktar (%) | Alt akımın toplam beslemeye oranı |

Program, bu verileri kullanarak tane boyutu sınıflarının üst akım ve alt akımdaki miktarlarını besleme bazında hesaplar.

## Kurulum

### 1. Gerekli Kütüphaneleri Yükleme

Terminal veya Komut İstemi üzerinden aşağıdaki komutu çalıştırın:

```bash
pip install pandas numpy matplotlib scipy
