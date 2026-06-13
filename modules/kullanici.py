# src/modules/kullanici.py

class Kullanici:
    """Temel Kullanıcı Sınıfı (Base Class)"""
    def __init__(self, kullanici_id, isim):
        self.kullanici_id = kullanici_id
        self.isim = isim


class Uye(Kullanici):
    """Kullanici sınıfından Kalıtım (Inheritance) alan Üye Sınıfı""" [cite: 12]
    def __init__(self, kullanici_id, isim, uye_kart_no):
        # Üst sınıfın yapıcı metodunu (constructor) çağırıyoruz
        super().__init__(kullanici_id, isim)
        self.uye_kart_no = uye_kart_no
        self.alinan_kitaplar = []  

    def kitap_ekle(self, kitap_objesi):
        self.alinan_kitaplar.append(kitap_objesi)

    def kitap_cikar(self, kitap_objesi):
        if kitap_objesi in self.alinan_kitaplar:
            self.alinan_kitaplar.remove(kitap_objesi)