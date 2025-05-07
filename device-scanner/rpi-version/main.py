import time
import json
from camera_rpi import capture_barcode  # Fungsi untuk membaca barcode dari kamera Pi
from sender import kirim_data  # Fungsi untuk mengirim data ke server

# Load konfigurasi
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Inisialisasi kamera
print("Initializing camera...")
# Kamera Raspberry Pi sudah dipersiapkan di camera_rpi.py

def main():
    while True:
        # Baca barcode dari kamera
        barcode = capture_barcode()

        if barcode:
            print(f"Barcode terdeteksi: {barcode}")
            try:
                # Kirim data ke server menggunakan sender.py
                response = kirim_data(barcode, config['server_url'], config['device_id'])
                if response.status_code == 200:
                    print("Data terkirim dengan sukses!")
                else:
                    print(f"Terjadi kesalahan saat mengirim data: {response.status_code}")
            except Exception as e:
                print(f"Error saat mengirim data: {e}")

        # Delay sejenak sebelum mencoba membaca barcode lagi
        time.sleep(1)

if __name__ == "__main__":
    main()
