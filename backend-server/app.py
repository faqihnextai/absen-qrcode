from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.scan_api import scan_bp  # pastikan ini ada dan benar
from routes.Absensi_scan import absensi_bp  # pastikan ini ada dan benar
import os
# Import file lain
from routes.scan_api import scan_bp

# Load variabel dari file .env
load_dotenv()

# Konfigurasi dasar
PORT = int(os.getenv("PORT", 5000))

# Inisialisasi Flask
app = Flask(__name__)
CORS(app)

# Daftarkan route API
app.register_blueprint(scan_bp, url_prefix="/api") 
app.register_blueprint(absensi_bp) # Daftarkan blueprint dengan prefix URL

# Jalankan server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
