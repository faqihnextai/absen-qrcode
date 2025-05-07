from db.databasesql import get_connection

def simpan_absensi(barcode, waktu, device_id, kelas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO absensi (barcode, waktu, device_id) VALUES (%s, %s, %s, %s)", (barcode, waktu, device_id, kelas))
    conn.commit()
    conn.close()

