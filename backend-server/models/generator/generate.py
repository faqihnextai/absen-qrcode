from barcode_generator import generate_barcode_png

# Contoh data barcode siswa (misalnya NISN atau kode unik)
barcode_data = "CODE128"

# Generate barcode
filepath = generate_barcode_png(barcode_data)

print(f"✅ Barcode berhasil dibuat di: {filepath}")
