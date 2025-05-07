import cv2
from pyzbar.pyzbar import decode
from sender import send_barcode
import threading

scanned_cache = set()

def async_send(barcode_data):
    # Fungsi pengiriman dijalankan di thread terpisah agar tidak menghambat kamera
    send_barcode(barcode_data)

def capture_barcode():
    cap = cv2.VideoCapture(0)
    print("🎥 Kamera aktif... Tekan ESC untuk keluar")

    font = cv2.FONT_HERSHEY_SIMPLEX
    feedback = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kamera tidak terbaca.")
            break

        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")

            if barcode_data not in scanned_cache:
                scanned_cache.add(barcode_data)

                # ✅ Tampilkan langsung di kamera
                feedback = f"✅ {barcode_data} berhasil absen!"

                # Kirim data tanpa blocking
                threading.Thread(target=async_send, args=(barcode_data,), daemon=True).start()

        # Tampilkan feedback di frame kamera
        cv2.putText(frame, feedback, (10, 50), font, 1, (0, 255, 0), 2)

        cv2.imshow("Scan Barcode", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_barcode()
