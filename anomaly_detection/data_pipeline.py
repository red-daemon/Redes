import time
import subprocess
from statistics import mean

class DataPipeline:
    def __init__(self, target: str, interval: float = 1.0):
        self.target = target
        self.interval = interval

    def stream_latency(self):
        while True:
            try:
                # Ejecuta 'ping -c 1' y parsea la salida
                result = subprocess.run(
                    ["ping", "-c", "1", self.target],
                    capture_output=True,
                    text=True,
                    check=True
                )
                # Busca "time=X ms" en la línea del reply
                for line in result.stdout.split("\n"):
                    if "time=" in line:
                        time_str = line.split("time=")[1].split(" ")[0]
                        latency = float(time_str)
                        yield latency
                        break
                else:
                    yield float('nan')
            except Exception as e:
                print(f"Error midiendo latencia con subprocess: {e}")
            time.sleep(self.interval)
