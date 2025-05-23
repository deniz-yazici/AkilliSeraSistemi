Akıllı Sera Ortam Kontrol Sistemi
Bu proje, seracılık faaliyetlerinde sıcaklık, nem ve toprak koşullarını izleyerek, sulama süresi ve fan gücü gibi parametreleri otomatik olarak kontrol eden bulanık mantık tabanlı bir sistemdir.

Modern tarım teknolojilerini yapay zeka ile birleştirerek, hem verimliliği artırmak, hem de enerji–su tasarrufu sağlamak hedeflenmiştir.

Amaç
Bitki türüne ve çevresel koşullara göre kararlar veren bir sistem tasarlamak
Klasik sabit eşiklere dayanan kontrol yöntemlerini aşarak daha akıllı bir algoritma üretmek
Kullanıcı dostu ve görsel olarak şık bir arayüz sunmak

Kullanılan Teknolojiler
Teknoloji	Açıklama
Python 3.10+	Ana yazılım dili
scikit-fuzzy	Bulanık mantık modelleme
Tkinter	Grafiksel kullanıcı arayüzü (GUI)
Matplotlib	Grafiksel çıktı (bar chart) gösterimi
NumPy, SciPy	Sayısal işlemler
Girdi Değişkenleri
Girdi	Aralık	Açıklama
Hava Sıcaklığı	10 – 45 °C	Sera içi sıcaklık
Nem Oranı	20 – 100 %	Havanın bağıl nemi
Toprak Nemliliği	0 – 100 %	Toprağın su oranı
Saat	0 – 24	Günün saat dilimi
Bitki Türü	1 = Kaktüs
2 = Domates
3 = Marul	Bitki türüne göre ihtiyaçlar farklıdır
Çıktı Değişkenleri
Çıktı	Aralık	Açıklama
Sulama Süresi	0 – 30 dk	Sulama sisteminin çalışacağı süre
Fan Gücü	0 – 100 %	Havalandırma sisteminin çalışma gücü
Kural Tabanı (Fuzzy Logic)
Bu sistemde, sıcaklık, nem, toprak ve bitki türüne göre 10 adet çok kriterli bulanık mantık kuralı uygulanmaktadır.
Örnek:

Kural:
Eğer sıcaklık "yüksek" VE nem "düşük" ise
sulama süresi "uzun" VE fan gücü "yüksek"

Tüm üyelik fonksiyonları üçgen (trimf) olarak tanımlanmıştır.

Arayüz Özellikleri
Kullanıcı dostu Tkinter GUI
Kaydırıcılar ve açılır kutular ile veri girişi
Hesap sonrası grafik ile görsel analiz
Anlık geri bildirim: Sulama ve fan sonuçları
Görsel arayüz ekran görüntüsü

Kurulum
Python 3.10+ sisteminize kurulu olmalı.
Gerekli kütüphaneleri yüklemek için:
pip install -r requirements.txt
