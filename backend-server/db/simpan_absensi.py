from db.databasesql import get_connection

def simpan_absensi(barcode, timestamp, device_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Cek apakah sudah absen hari ini
    query_check = """
        SELECT COUNT(*) FROM absensi_real_time
        WHERE barcode = %s AND DATE(timestamp) = CURDATE()
    """
    cursor.execute(query_check, (barcode,))
    sudah_ada = cursor.fetchone()[0]

    if sudah_ada:
        print("Siswa sudah absen hari ini")
    else:
        # Simpan absensi baru
        query_insert = """
            INSERT INTO absensi_real_time (barcode, timestamp, device_id)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query_insert, (barcode, timestamp, device_id))
        conn.commit()
        print("Absensi berhasil disimpan")

    cursor.close()
    conn.close()
