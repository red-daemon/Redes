from data_pipeline import DataPipeline
from anomaly_detector import FeatureExtractor, AnomalyDetector
from alert_handler import AlertHandler

TARGET_HOST = '8.8.8.8'
INTERVAL_S = 1.0
THRESHOLD = 0.8
LOG_EVERY = 10  # Mostrar estado cada 10 pasos


def main():
    pipeline = DataPipeline(TARGET_HOST, INTERVAL_S)
    extractor = FeatureExtractor()
    detector = AnomalyDetector()
    alerter = AlertHandler(THRESHOLD)

    step = 0
    for latency in pipeline.stream_latency():
        features = extractor.fit_transform(latency)
        detector.learn(features)
        is_anom, score = detector.is_anomaly(features, THRESHOLD)
        alerter.handle(latency, score)

        # Imprimir información cada LOG_EVERY pasos
        if step % LOG_EVERY == 0:
            mean = extractor.scaler.means.get('latency', None)
            std = extractor.scaler.vars.get('latency', 0) ** 0.5 if 'latency' in extractor.scaler.vars else 0
            scaled = features['latency']
            print(f"\n--- Paso {step} ---")
            print(f"Latencia: {latency:.2f} ms")
            print(f"Latencia escalada: {scaled:.3f}")
            print(f"Media estimada: {mean:.3f}" if mean else "Media: N/A")
            print(f"Desviación estándar estimada: {std:.3f}")
            print(f"Score de anomalía: {score:.3f}")
            print(f"¿Es anomalía?: {'Sí' if is_anom else 'No'}")
            print("----------------------\n")

        step += 1

if __name__ == '__main__':
    main()
