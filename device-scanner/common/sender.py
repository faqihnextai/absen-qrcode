import requests
import json
from datetime import datetime

def kirim_data(barcode_data):
    # Baca konfigurasi dari config.json
    with open('config.json') as f:
        config = json.load(f)

    url = config.get("server_url", "")
    token = config.get("token", "")
    device_id = config.get("device_id", "")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "device_id": device_id,
        "barcode": barcode_data,
        "timestamp": datetime.now().isoformat()
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("✅ Sukses kirim data.")
        else:
            print(f"❌ Gagal! Status {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ ERROR kirim data: {str(e)}")

# Contoh pemanggilan
if __name__ == "__main__":
    sample_barcode = "1234567890"
    kirim_data(sample_barcode)
