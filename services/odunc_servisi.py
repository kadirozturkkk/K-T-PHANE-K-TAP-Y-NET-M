from src.repositories.veritabani import Veritabani

class KutuphaneServisi:
    def __init__(self):
        self.veritabani = Veritabani()

    def tum_kitaplari_getir(self):
        return self.veritabani.verileri_oku()

    def yeni_kitap_ekle(self, baslik, yazar, isbn):
        kitaplar = self.tum_kitaplari_getir()
        yeni_kitap = {"baslik": baslik, "yazar": yazar, "isbn": isbn, "odunc_verildi_mi": False}
        kitaplar.append(yeni_kitap)
        self.veritabani.verileri_yaz(kitaplar)

    def kitap_odunc_ver(self, isbn):
        kitaplar = self.tum_kitaplari_getir()
        for k in kitaplar:
            if k.get("isbn") == isbn:
                k["odunc_verildi_mi"] = True
        self.veritabani.verileri_yaz(kitaplar)

    def kitap_iade_et(self, isbn):
        kitaplar = self.tum_kitaplari_getir()
        for k in kitaplar:
            if k.get("isbn") == isbn:
                k["odunc_verildi_mi"] = False
        self.veritabani.verileri_yaz(kitaplar)