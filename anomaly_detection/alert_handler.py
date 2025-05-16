import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO
)

class AlertHandler:
    def __init__(self, threshold: float):
        self.threshold = threshold

    def handle(self, value: float, score: float):
        """Logea o envía notificaciones si se detecta anomalía."""
        if score > self.threshold:
            logging.warning(f"Anomalía detectada: valor={value:.2f} ms, score={score:.3f}")