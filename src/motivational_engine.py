import os
import joblib

class MotivationalEngine:
    def __init__(self, models_dir='models'):
        self.models_dir = models_dir
        self.models = self._load_all_models()

    def _load_all_models(self):
        models = {}
        for fname in os.listdir(self.models_dir):
            if fname.endswith('_gmm_v1.pkl'):
                key = fname.replace('_gmm_v1.pkl', '')
                models[key] = joblib.load(os.path.join(self.models_dir, fname))
        return models

    def get_model_key(self, game_mode, difficulty, duration_minutes):
        return f"{game_mode}_{difficulty}_{duration_minutes}min"

    def predict(self, game_mode, difficulty, duration_minutes, player_data):
        key = self.get_model_key(game_mode, difficulty, duration_minutes)
        if key not in self.models:
            raise ValueError(f"No model found for {key}")
        model_data = self.models[key]
        features = model_data['features']
        scaler = model_data['scaler']
        gmm = model_data['gmm_model']

        # Prepare input
        X = [[player_data[feat] for feat in features]]
        X_scaled = scaler.transform(X)
        cluster = int(gmm.predict(X_scaled)[0])
        prob = float(gmm.predict_proba(X_scaled).max())
        percentiles = model_data['percentile_targets'][cluster]
        # Fix: gather all stats for the predicted cluster
        cluster_stats = {stat: values[str(cluster)] for stat, values in model_data['cluster_stats'].items()}

        return {
            'cluster': cluster,
            'confidence': prob,
            'percentiles': percentiles,
            'cluster_stats': cluster_stats
        }

# Example usage (for testing, can be removed in production)
if __name__ == "__main__":
    engine = MotivationalEngine(models_dir='models/models')
    player_data = {
        'score': 150000,
        'age': 25,
        'startSpeed': 5.0,
        'duration_minutes': 10.0
    }
    result = engine.predict('DualFlow', -1, 10.0, player_data)
    print(result) 