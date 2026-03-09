import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Recruiting Platform",
    layout="wide"
)

st.title("🤖 AI Recruiting Campaign Optimizer")

st.markdown("### Overview")

res = requests.get(f"{API}/campaign_analytics")
data = res.json()

col1, col2, col3 = st.columns(3)

col1.metric("Total Campaigns", data["total_campaigns"])
col2.metric("Total Budget", data["total_budget"])
col3.metric("Average Budget", data["average_budget"])

st.markdown("---")

st.info("Use the sidebar to navigate through AI tools.")