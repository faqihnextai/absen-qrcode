import cv2
from pyzbar.pyzbar import decode

def scan_barcode():
    cap = cv2.VideoCapture(0)  # Kamera default

    print("🎥 Kamera aktif... Tekan ESC untuk keluar")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Kamera tidak terbaca.")
            break

        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            print(f"✅ Terbaca: [{barcode_type}] {barcode_data}")

            # Gambar kotak di sekitar barcode
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Tampilkan isi barcode di layar
            cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) == 27:  # ESC untuk keluar
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_barcode()
