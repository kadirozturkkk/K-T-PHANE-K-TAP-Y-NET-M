from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import sys
from datetime import datetime

# ====================== YOL DÜZELTMELERİ ======================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

# Veritabanı yolu
DB_PATH = os.path.join(BASE_DIR, 'data', 'kutuphane.db')

# ====================== VERİTABANI ======================
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('''
        CREATE TABLE IF NOT EXISTS kitaplar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT NOT NULL,
            yazar TEXT NOT NULL,
            isbn TEXT,
            odunc_verildi_mi BOOLEAN DEFAULT 0,
            odunc_tarihi TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ====================== ROUTE'LAR ======================
@app.route('/')
def index():
    conn = get_db()
    kitaplar = conn.execute("SELECT * FROM kitaplar ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('index.html', kitaplar=kitaplar)

@app.route('/kitap_ekle', methods=['POST'])
def kitap_ekle():
    baslik = request.form.get('baslik')
    yazar = request.form.get('yazar')
    isbn = request.form.get('isbn')

    if baslik and yazar:
        conn = get_db()
        conn.execute('''
            INSERT INTO kitaplar (baslik, yazar, isbn, odunc_verildi_mi)
            VALUES (?, ?, ?, ?)
        ''', (baslik, yazar, isbn, False))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/odunc_ver/<int:kitap_id>', methods=['POST'])
def odunc_ver(kitap_id):
    conn = get_db()
    conn.execute("UPDATE kitaplar SET odunc_verildi_mi = 1, odunc_tarihi = ? WHERE id = ?", 
                 (datetime.now().strftime("%Y-%m-%d %H:%M"), kitap_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/iade_et/<int:kitap_id>', methods=['POST'])
def iade_et(kitap_id):
    conn = get_db()
    conn.execute("UPDATE kitaplar SET odunc_verildi_mi = 0, odunc_tarihi = NULL WHERE id = ?", (kitap_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/sil/<int:kitap_id>', methods=['POST'])
def sil(kitap_id):
    conn = get_db()
    conn.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/duzenle/<int:kitap_id>', methods=['GET'])
def duzenle_get(kitap_id):
    conn = get_db()
    kitap = conn.execute("SELECT * FROM kitaplar WHERE id = ?", (kitap_id,)).fetchone()
    conn.close()
    return render_template('duzenle.html', kitap=kitap)

@app.route('/duzenle/<int:kitap_id>', methods=['POST'])
def duzenle_post(kitap_id):
    baslik = request.form.get('baslik')
    yazar = request.form.get('yazar')
    isbn = request.form.get('isbn')

    if baslik and yazar:
        conn = get_db()
        conn.execute("""
            UPDATE kitaplar 
            SET baslik = ?, yazar = ?, isbn = ?
            WHERE id = ?
        """, (baslik, yazar, isbn, kitap_id))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# ====================== BAŞLAT ======================
if __name__ == '__main__':
    init_db()
    print("🚀 Kütüphane sistemi çalışıyor...")
    print("🌐 http://127.0.0.1:5000")
    app.run(debug=True)