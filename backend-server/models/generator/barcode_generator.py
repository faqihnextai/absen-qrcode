import os
import barcode
from barcode.writer import ImageWriter
import json
import re  # Untuk membersihkan nama file

def generate_barcode_png(barcode_data_json, nama_siswa, kelas_siswa, output_dir="static"):
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_dir)
    os.makedirs(output_dir, exist_ok=True)

    print(f"📂 Output path barcode: {output_dir}")  # <-- Tambahkan ini

    try:
        data = json.loads(barcode_data_json)
        nis = data.get("nis", "unknown")
    except json.JSONDecodeError:
        print("❌ Format barcode_data bukan JSON valid.")
        nis = "unknown"

    gabungan = f"{nama_siswa}_{kelas_siswa}_{nis}"
    nama_file_bersih = re.sub(r'[^\w\-]', '', gabungan)[:50]

    CODE128 = barcode.get_barcode_class("code128")
    barcode_obj = CODE128(barcode_data_json, writer=ImageWriter())

    filename = os.path.join(output_dir, nama_file_bersih)

    try:
        full_path = barcode_obj.save(filename)
        return full_path
    except FileNotFoundError as e:
        print(f"❌ Gagal simpan barcode: {e}")
        return None
