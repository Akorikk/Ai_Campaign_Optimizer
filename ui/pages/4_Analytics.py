import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API = "http://127.0.0.1:8000"

st.title("Campaign Analytics")

res = requests.get(f"{API}/campaign_analytics")
data = res.json()

df = pd.DataFrame(
    {
        "Metric": data.keys(),
        "Value": data.values()
    }
)

st.table(df)

fig = px.bar(df, x="Metric", y="Value")

st.plotly_chart(fig)