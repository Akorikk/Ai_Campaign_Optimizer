import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("AI Budget Allocation")

job = st.text_input("Job Title")
location = st.text_input("Location")
budget = st.number_input("Budget")

if st.button("Allocate Budget"):

    payload = {
        "job_title": job,
        "location": location,
        "budget": budget
    }

    r = requests.post(f"{API}/allocate_budget", json=payload)
    data = r.json()

    st.success("Budget Allocated")

    allocation = data["budget_allocation"]

    df = pd.DataFrame({
        "Channel": allocation.keys(),
        "Budget": allocation.values()
    })

    fig = px.pie(df, names="Channel", values="Budget")

    st.plotly_chart(fig)