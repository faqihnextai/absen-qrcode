from flask import Blueprint, jsonify, request
from datetime import datetime, date
from db.simpan_absensi import simpan_absensi
from db.databasesql import get_connection

absensi_bp = Blueprint('absensi_api', __name__)

# POST: Simpan absensi
@absensi_bp.route('/api/scan', methods=['POST'])
def scan_absensi():
    data = request.get_json()
    barcode = data.get("barcode")
    device_id = data.get("device_id")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not barcode or not device_id:
        return jsonify({"status": "error", "message": "Data tidak lengkap"}), 400

    try:
        simpan_absensi(barcode, timestamp, device_id)
        return jsonify({"status": "success", "message": "Absensi berhasil disimpan"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# GET: Ambil absensi hari ini
@absensi_bp.route('/api/scan', methods=['GET'])
def absensi_hari_ini():
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()
    query = """
        SELECT s.nama, a.timestamp,
        CASE 
            WHEN TIME(a.timestamp) <= '07:15:00' THEN 'Tepat Waktu'
            ELSE 'Terlambat'
        END AS status
        FROM absensi_real_time a
        JOIN siswa s ON a.barcode = s.barcode
        WHERE DATE(a.timestamp) = %s
        ORDER BY a.timestamp ASC
    """
    cursor.execute(query, (today,))
    rows = cursor.fetchall()
    conn.close()

    result = [
        {
            "nama": row[0],
            "waktu_masuk": row[1][11:16],  # format HH:MM
            "status": row[2]
        }
        for row in rows
    ]

    return jsonify(result)
