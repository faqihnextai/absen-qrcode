import cv2
from pyzbar import pyzbar

def baca_barcode():
    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    if not cap.isOpened():
        print("Gagal membuka kamera.")
        return None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            # Deteksi barcode
            barcodes = pyzbar.decode(frame)

            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                cap.release()
                cv2.destroyAllWindows()
                return barcode_data  # Barcode ditemukan

            # Tampilkan preview (opsional)
            cv2.imshow('Scan Barcode (Tekan Q untuk keluar)', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

    return None  # Jika tidak ada barcode

# Contoh pemanggilan
if __name__ == "__main__":
    hasil = baca_barcode()
    if hasil:
        print(f"Barcode terbaca: {hasil}")
    else:
        print("Tidak ada barcode yang terbaca.")
