# anomaly_detector.py

from river import anomaly
from river import preprocessing

class FeatureExtractor:
    def __init__(self):
        # Escalador en línea que normaliza características
        self.scaler = preprocessing.StandardScaler()

    def fit_transform(self, x: float) -> dict:
        """
        Ajusta y transforma el valor x bajo el nombre de feature 'latency'.
        Devuelve un dict {'latency': valor_escalado}.
        """
        # 1) Aprende de la nueva muestra
        self.scaler.learn_one({'latency': x})
        # 2) Transforma esa misma muestra
        scaled = self.scaler.transform_one({'latency': x})
        return scaled


class AnomalyDetector:
    def __init__(self, n_trees: int = 10, height: int = 6, seed: int = 42):
        # Modelo online de Half Space Trees
        self.model = anomaly.HalfSpaceTrees(n_trees=n_trees,
                                           height=height,
                                           seed=seed)

    def learn(self, features: dict):
        """
        Ajusta el modelo a la nueva muestra de features.
        """
        self.model.learn_one(features)

    def score(self, features: dict) -> float:
        """
        Obtiene el score de anomalía de la muestra (entre 0 y ∞).
        A mayor score, más probable es que sea anomalía.
        """
        return self.model.score_one(features)

    def is_anomaly(self, features: dict, threshold: float = 0.5) -> tuple:
        """
        Devuelve (True, score) si score > threshold, 
        o (False, score) en caso contrario.
        """
        score = self.score(features)
        return score > threshold, score
