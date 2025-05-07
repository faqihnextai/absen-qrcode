import cv2
from pyzbar.pyzbar import decode
import time

def capture_barcode():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # 0 untuk kamera default
    cap.set(3, 640)  # Lebar frame
    cap.set(4, 480)  # Tinggi frame

    print("Menunggu barcode...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal mengakses kamera")
            break

        # Deteksi barcode di frame
        decoded_objects = decode(frame)
        if decoded_objects:
            for obj in decoded_objects:
                barcode_data = obj.data.decode('utf-8')
                print(f"Barcode ditemukan: {barcode_data}")
                cap.release()
                return barcode_data

        # Delay sebentar
        time.sleep(0.1)

if __name__ == "__main__":
    barcode = capture_barcode()
