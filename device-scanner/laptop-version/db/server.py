from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulasi penyimpanan data (bisa diganti dengan database nyata)
barcode_data = []

@app.route('/api/barcode', methods=['POST'])
def save_barcode():
    data = request.json
    device_id = data.get("device_id")
    barcode = data.get("barcode")
    
    # Simpan data barcode
    barcode_data.append({"device_id": device_id, "barcode": barcode})
    
    print(f"📦 Data barcode diterima: {barcode} dari device {device_id}")
    
    return jsonify({"message": "Data berhasil diterima"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
