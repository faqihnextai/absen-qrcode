from sqlite_storage import create_table, save_barcode

# Buat tabel (kalau belum ada)
create_table()

# Contoh data dummy
device_id = "DEVICE-01"
barcode = "BARCODE123456"

# Simpan ke database
save_barcode(device_id, barcode)
