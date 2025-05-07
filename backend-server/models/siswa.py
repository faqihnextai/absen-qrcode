from db.databasesql import get_connection

def cari_siswa(barcode):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nama, barcode FROM siswa WHERE barcode = %s", (barcode,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "nama": row[0],
            "barcode": row[1]
        }
    return None

def siswa_sudah_absen(barcode, tanggal):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM absensi WHERE barcode = %s AND DATE(waktu) = %s", (barcode, tanggal))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0
