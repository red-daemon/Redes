#!/usr/bin/env python3
# wifi_speed_test.py

import speedtest
import datetime
import argparse
import json
import os

def test_speed():
    st = speedtest.Speedtest()
    # Selecciona el mejor servidor basado en ping
    st.get_best_server()
    download_bps = st.download()
    upload_bps = st.upload()
    ping_ms = st.results.ping

    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "download_mbps": round(download_bps / 1e6, 2),
        "upload_mbps": round(upload_bps / 1e6, 2),
        "ping_ms": round(ping_ms, 2),
        "server": st.results.server
    }

def save_results(data, output_file):
    # Si no existe el archivo, crea lista; si existe, lee y append
    if os.path.isfile(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(data)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(
        description="Mide la velocidad de tu conexión Wi-Fi y guarda los resultados."
    )
    parser.add_argument(
        '-o', '--output',
        default='wifi_speed_log.json',
        help='Archivo JSON donde se guardarán los resultados'
    )
    args = parser.parse_args()

    print("Iniciando test de velocidad...")
    result = test_speed()
    print(f"Ping: {result['ping_ms']} ms")
    print(f"Download: {result['download_mbps']} Mbps")
    print(f"Upload: {result['upload_mbps']} Mbps")

    save_results(result, args.output)
    print(f"Resultados guardados en {args.output}")

if __name__ == "__main__":
    main()
