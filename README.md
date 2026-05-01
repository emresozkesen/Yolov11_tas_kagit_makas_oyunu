YOLOv11 ile Taş-Kağıt-Makas Oyunu
Bu proje, BTK Akademi'deki "YOLOv11 ile Bilgisayarlı Görü Pratikleri" eğitimi kapsamında öğrendiğim bilgilerle geliştirdiğim bir uygulamadır. Sistem, bilgisayar kamerası üzerinden el hareketlerinizi (Taş, Kağıt, Makas) gerçek zamanlı olarak algılar ve bilgisayarın rastgele seçimiyle karşılaştırarak skoru hesaplar.

🚀 Proje Özellikleri
Gerçek Zamanlı Algılama: YOLOv11 mimarisi kullanılarak yüksek doğrulukta el hareketi tespiti yapılır.  

Oyun Mekaniği: Kullanıcı ve bilgisayar arasında otomatik skor takibi ve kazanan belirleme sistemi mevcuttur.

Görsel Bilgi Paneli: Ekran üzerinde anlık skor, bilgisayar hamlesi ve oyun arası bekleme süresi gösterilir.

Ayna Efekti: Kullanıcı deneyimini iyileştirmek için kamera görüntüsü yatay olarak çevrilmiştir (cv2.flip).  

Hızlı Kontroller: Klavye kısayolları ile skor sıfırlama ve çıkış imkanı sunar.

  
Kontroller
'q' Tuşu: Oyunu kapatır.

'r' Tuşu: Skoru sıfırlar (Sen: 0, PC: 0).

Elinizi Gösterin: Kameraya elinizi gösterdiğinizde sistem otomatik olarak hamlenizi algılar.

⚙️ Teknik Detaylar
Model: best.pt (Eğitilmiş YOLOv11 ağırlık dosyası).  

Eşik Değeri: %60 (0.60) üzerindeki tahminler geçerli kabul edilir.

Kütüphaneler: ultralytics, opencv-python, numpy.

Zamanlama: Hamleler arasında 2 saniyelik bekleme süresi (cooldown) bulunur.
