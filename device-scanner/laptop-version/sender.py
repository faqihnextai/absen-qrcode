import requests
import json
import mysql.connector
from datetime import datetime

# Load config
with open('config.json') as f:
    config = json.load(f)

# Simpan juga ke MySQL lokal
def save_to_mysql(device_id, barcode, kelas):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="absensi"
        )
        cursor = conn.cursor()
        query = "INSERT INTO barcodes (device_id, barcode, waktu, kelas) VALUES (%s, %s, %s, %s)"
        values = (device_id, barcode, datetime.now(), kelas)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Data juga disimpan ke MySQL lokal.")
    except mysql.connector.Error as err:
        print(f"⚠️ Error MySQL:", err)

# Fungsi utama kirim barcode
def send_barcode(barcode_data):
    try:
        # Ambil kelas dari database berdasarkan barcode
        barcode = barcode_data  # langsung dari kamera
        kelas = get_kelas_from_db(barcode)

        payload = {
            "device_id": config["device_id"],
            "barcode": barcode
        }

        response = requests.post(config["server_url"], json=payload)
        if response.status_code == 200:
            print("✅ Data berhasil dikirim.")
        else:
            print(f"❌ Gagal kirim. Status Code: {response.status_code}")

        save_to_mysql(config["device_id"], barcode, kelas)

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error saat kirim:", e)

    # Simpan juga ke database lokal
    # save_to_mysql(config["device_id"], barcode_data )
def get_kelas_from_db(barcode):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="absensi"
        )
        cursor = conn.cursor()
        query = "SELECT kelas FROM siswa WHERE nis = %s"
        cursor.execute(query, (barcode,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] if result else "UNKNOWN"
    except mysql.connector.Error as err:
        print("⚠️ Gagal ambil kelas:", err)
        return "UNKNOWN"
