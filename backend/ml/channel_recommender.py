import pandas as pd
from sklearn.ensemble import RandomForestClassifier


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


def recommend_channel(job_title, location):

    input_df = pd.DataFrame({
        "job_title": [job_title],
        "location": [location]
    })

    input_df = pd.get_dummies(input_df)

    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(input_df)

    return prediction[0]