import mysql.connector
from mysql.connector import Error

# Konfigurasi koneksi database
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",         # Ganti sesuai password MySQL
    "database": "absensi"   # Ganti sesuai nama database
}

def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print("❌ Gagal koneksi ke database:", e)
        return None

def save_barcode(device_id, barcode, kelas):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO barcodes (device_id, barcode, kelas) VALUES (%s, %s)"
            cursor.execute(sql, (device_id, barcode, kelas))
            conn.commit()
            print("✅ Barcode berhasil disimpan ke MySQL.")
        except Error as e:
            print("❌ Error saat menyimpan barcode:", e)
        finally:
            cursor.close()
            conn.close()
