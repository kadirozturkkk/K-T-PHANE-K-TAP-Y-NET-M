# src/data/veri_yoneticisi.py
import json
import os

class VeriYoneticisi:
    def __init__(self, dosya_yolu="data/kitaplar.json"):
        self.dosya_yolu = dosya_yolu

    def veriyi_oku(self):
        """JSON dosyasındaki verileri okur (Hata yönetimi içerir)"""
        if not os.path.exists(self.dosya_yolu):
            return []
        
        # Hata Yönetimi: Dosya okuma esnasında oluşabilecek hatalara karşı try-except
        try:
            with open(self.dosya_yolu, "r", encoding="utf-8") as dosya:
                return json.load(dosya)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def veriyi_kaydet(self, veri_listesi):
        """Verileri JSON dosyasına güvenli bir şekilde yazar"""
        try:
            with open(self.dosya_yolu, "w", encoding="utf-8") as dosya:
                json.dump(veri_listesi, dosya, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Veri kaydedilirken hata oluştu: {e}")
            return False