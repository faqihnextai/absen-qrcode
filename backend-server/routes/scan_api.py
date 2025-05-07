from flask import Blueprint, request, jsonify
from models.siswa import cari_siswa
from db.database import simpan_absensi
from datetime import datetime

scan_bp = Blueprint('scan_bp', __name__)  # konsisten pakai ini

@scan_bp.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    barcode = data.get("barcode")
    device_id = data.get("device_id")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not barcode or not device_id:
        return jsonify({"status": "error", "message": "Data tidak lengkap"}), 400

    siswa = cari_siswa(barcode)
    if siswa:
        simpan_absensi(barcode, timestamp, device_id, siswa["kelas"])
        return jsonify({"status": "success", "message": "Absensi disimpan", "siswa": siswa}), 200
    else:
        return jsonify({"status": "error", "message": "Siswa tidak ditemukan"}), 404
    
        new_func(barcode, siswa)

def new_func(barcode, siswa):
    print(f"Barcode diterima: {barcode}")
    print(f"Siswa ditemukan: {siswa}")

