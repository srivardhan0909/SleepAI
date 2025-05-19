import numpy as np

class HybridModel:
    def __init__(self, rf_model, ann_model, scaler):
        self.rf_model = rf_model
        self.ann_model = ann_model
        self.scaler = scaler

    def predict(self, X):
        # Generate probabilities from RF
        rf_proba = self.rf_model.predict_proba(X)
        # Combine RF probabilities with original features
        X_hybrid = np.hstack((X, rf_proba))
        # Standardize the hybrid features
        X_hybrid = self.scaler.transform(X_hybrid)
        # Predict with the ANN
        return self.ann_model.predict(X_hybrid)
