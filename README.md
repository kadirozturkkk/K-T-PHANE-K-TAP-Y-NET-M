1. Proje Amacı
Bu sistem, kütüphane envanterinin yönetilmesini, kitapların ödünç alma ve iade süreçlerinin takip edilmesini sağlayan, web tabanlı bir yönetim yazılımıdır. Sistemin temel amacı, manuel kayıt tutma hatalarını minimize etmek ve koleksiyon durumunu anlık olarak görüntülemektir.

2. Fonksiyonel Gereksinimler
Sistem, kullanıcıların aşağıdaki işlevleri gerçekleştirmesine olanak tanır:

Kitap Kaydı (Create): Kullanıcı, yeni bir kitabın başlık, yazar ve ISBN bilgilerini sisteme girerek kayıt altına alabilmelidir.

Koleksiyon Görüntüleme (Read): Sistem, veritabanındaki tüm kitapları, yazarlarını, ISBN numaralarını ve mevcut durumlarını (Müsait veya Ödünçte) bir tablo yapısında listeleyebilmelidir.

Ödünç Alma İşlemi (Update): "Müsait" durumdaki bir kitap için ödünç alma işlemi başlatıldığında, sistem kitabın durumunu otomatik olarak "Ödünçte" olarak güncellemelidir.

İade Etme İşlemi (Update): "Ödünçte" durumundaki bir kitap için iade işlemi yapıldığında, sistem kitabın durumunu tekrar "Müsait" olarak güncellemelidir.

3. Fonksiyonel Olmayan Gereksinimler
Sistemin yüksek kaliteli bir kullanıcı deneyimi sunması için aşağıdaki kriterler hedeflenmiştir:

Kullanılabilirlik: Kullanıcı arayüzü, temel kütüphane işlemlerinin (ekle, ödünç al, iade et) tek tıkla yapılabileceği kadar yalın ve anlaşılır tasarlanmıştır.

Veri Kalıcılığı: Tüm kitap verileri JSON tabanlı bir veritabanında saklanmaktadır. Böylece uygulama kapatılıp açıldığında veriler kaybolmamakta, süreklilik korunmaktadır.

Taşınabilirlik: Uygulama, Python çalışma ortamına sahip olan tüm işletim sistemlerinde (Windows, Linux, macOS) ek bir konfigürasyon gerektirmeden çalışacak şekilde modüler yapıda geliştirilmiştir.

Performans: Sistem, veritabanı okuma ve yazma işlemlerini optimize ederek, kullanıcı etkileşimlerine 1 saniyenin altında geri bildirim verecek şekilde tasarlanmıştır.
