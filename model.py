import joblib
from utils import extract_features

# Load trained model
try:
    model = joblib.load("phishing_model.pkl")
except:
    model = None

def predict_url(url):
    features = extract_features(url)

    if model:
        prediction = model.predict([features])[0]
    else:
        # fallback simple rule-based logic
        prediction = 1 if "login" in url or "@" in url else 0

    return prediction