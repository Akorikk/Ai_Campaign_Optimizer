import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Create Recruiting Campaign")

name = st.text_input("Campaign Name")
job = st.text_input("Job Title")
location = st.text_input("Location")
budget = st.number_input("Budget")

if st.button("Create Campaign"):

    payload = {
        "name": name,
        "job_title": job,
        "location": location,
        "budget": budget
    }

    r = requests.post(f"{API}/campaign", json=payload)

    st.success("Campaign Created")
    st.json(r.json())