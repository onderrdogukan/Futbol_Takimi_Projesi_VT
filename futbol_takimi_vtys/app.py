import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL bağlantı ayarları
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # MySQL kullanıcı adı
app.config['MYSQL_PASSWORD'] = '070718417Dk.'  # MySQL Şifre
app.config['MYSQL_DB'] = 'futbol_takimi'  # Veritabanı adı

mysql = MySQL(app) # MySQL'i başlatma

# Ana sayfa (veritabanından çekilen oyuncu listesi)
@app.route('/')
def index():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM oyuncular")
    oyuncular = cur.fetchall()
    return render_template('index.html', oyuncular=oyuncular)

# Yeni futbolcu ekleme
@app.route('/futbolcu_ekle', methods=['POST'])
def futbolcu_ekle():
    forma_no = int(request.form['forma_no'])  # Forma numarasını alıyoruz ve int'e dönüştürüyoruz
    ad = request.form['ad']
    soyad = request.form['soyad']
    pozisyon = request.form['pozisyon']
    dogum_tarihi = request.form['dogum_tarihi']
    uyruk = request.form['uyruk']
    maas = request.form['maas']
    piyasa_degeri = request.form['piyasa_degeri']
    
    # Forma numarasının 99'dan büyük olup olmadığını kontrol et
    if forma_no > 99 :
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM oyuncular WHERE forma_no = %s", (forma_no,))
        oyuncular = cur.fetchall()
        return render_template('index.html', error="Forma numarası 99'dan büyük olamaz!", oyuncular=oyuncular)  # type: ignore

    # Veritabanına kaydetme işlemi
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO oyuncular (forma_no, ad, soyad, pozisyon, dogum_tarihi, uyruk,maas,piyasa_degeri) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                (forma_no, ad, soyad, pozisyon, dogum_tarihi, uyruk,maas,piyasa_degeri))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('index'))  # Ana sayfaya yönlendirme


# Oyuncu silme
@app.route('/futbolcu_sil/<int:id>', methods=['GET'])
def futbolcu_sil(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM oyuncular WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('index'))

# Oyuncu güncelleme
@app.route('/futbolcu_guncelle/<int:id>', methods=['POST'])
def futbolcu_guncelle(id):
    forma_no = int(request.form['forma_no'])  # Forma numarasını alıyoruz ve int'e dönüştürüyoruz
    ad = request.form['ad']
    soyad = request.form['soyad']
    pozisyon = request.form['pozisyon']
    dogum_tarihi = request.form['dogum_tarihi']
    uyruk = request.form['uyruk']
    maas = request.form['maas']
    piyasa_degeri = request.form['piyasa_degeri']

    
    
    # Forma numarasının 99'dan büyük olup olmadığını kontrol et
    if forma_no > 99:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM oyuncular WHERE forma_no = %s", (forma_no,))
        oyuncular = cur.fetchall()
        return render_template('index.html', error="Forma numarası 99'dan büyük olamaz!", oyuncular=oyuncular)  # type: ignore

    # Veritabanına kaydetme işlemi
    cur = mysql.connection.cursor()
    cur.execute("UPDATE oyuncular SET ad = %s, soyad = %s, pozisyon = %s, dogum_tarihi = %s, uyruk = %s , maas = %s , piyasa_degeri = %s WHERE id = %s", 
                    (ad,soyad,pozisyon,dogum_tarihi,uyruk,maas,piyasa_degeri,id))

    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('index'))  # Ana sayfaya yönlendirme


if __name__ == "__main__":
    # Uygulama başladığında tarayıcıyı açmak için
    webbrowser.open('http://127.0.0.1:5000/')  # Tarayıcıda açılacak URL
    app.run(debug=False)
