import streamlit as st
import requests

st.title("OpenShift RAG Assistant")
query = st.text_input("Enter your question")

if query:
    res = requests.post("http://backend-service:8000/ask", json={"question": query})
    st.write(res.json().get("answer"))
