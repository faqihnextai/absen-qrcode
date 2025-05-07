import json
from barcode_generator import generate_barcode_png
import os
import sys
from mysql.connector.errors import IntegrityError  # Tambahkan ini
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from db.databasesql import get_connection  # pastikan file ini sudah disiapkan koneksi MySQL-nya

def tambah_siswa(nama, barcode_data_json, kelas):
    conn = get_connection()
    cursor = conn.cursor()

    try:
    # Simpan ke database MySQL
        query = "INSERT INTO siswa (nama, barcode, kelas) VALUES (%s, %s, %s)"
        cursor.execute(query, (nama, barcode_data_json, kelas))
        conn.commit()
        print(f"✅ Data siswa '{nama}' berhasil ditambahkan.")
    except IntegrityError:
        print("⚠️ Barcode sudah ada di database.")
        return
    finally:
        cursor.close()
        conn.close()

    # Generate barcode image
    filepath = generate_barcode_png(barcode_data_json, nama, kelas)
    print(f"✅ Barcode PNG disimpan di: {filepath}")

if __name__ == "__main__":
    nama = input("Masukkan nama siswa: ")
    nis = input("Masukkan kode barcode (NISN atau kode unik): ")
    kelas = input("Masukkan kelas siswa: ")

    # Buat barcode dalam bentuk JSON string
    barcode_dict = {
        "nis": nis,
        "kelas": kelas
    }
    barcode_json = json.dumps(barcode_dict)

    # Simpan dan buat barcode
    tambah_siswa(nama, barcode_json, kelas)
    print("✅ Siswa berhasil ditambahkan.")
    
