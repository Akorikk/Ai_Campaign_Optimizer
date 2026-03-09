import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("AI Channel Recommendation")

job = st.text_input("Job Title")
location = st.text_input("Location")

if st.button("Recommend Channel"):

    payload = {
        "job_title": job,
        "location": location
    }

    r = requests.post(f"{API}/recommend_channel", json=payload)

    st.success("Recommended Channel")
    st.json(r.json())