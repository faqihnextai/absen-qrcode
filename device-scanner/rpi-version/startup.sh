#!/bin/bash
# startup.sh

# Menunggu beberapa detik untuk memastikan Raspberry Pi siap
sleep 10

# Jalankan script Python `main.py` di background
nohup python3 /path/to/device-scanner/rpi-version/main.py > /path/to/device-scanner/rpi-version/log.txt 2>&1 &
