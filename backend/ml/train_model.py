import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "job_title": ["Physiotherapist", "Nurse", "Doctor", "Therapist", "Nurse"],
    "location": ["Berlin", "Munich", "Berlin", "Hamburg", "Cologne"],
    "channel": ["LinkedIn", "Indeed", "LinkedIn", "Facebook", "Indeed"]
}

df = pd.DataFrame(data)

X = df[["job_title", "location"]]
y = df["channel"]

X = pd.get_dummies(X)

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "backend/ml/channel_model.pkl")
joblib.dump(X.columns, "backend/ml/model_columns.pkl")

print("Model trained and saved!")