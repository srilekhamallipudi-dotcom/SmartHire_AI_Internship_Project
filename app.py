import streamlit as st

st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🔐",
    layout="centered"
)

st.title("🤖 SmartHire AI")

st.write("Please Login or Register to continue.")

if st.button("📝 Register"):
    st.switch_page("pages/1_Register.py")

if st.button("🔐 Login"):
    st.switch_page("pages/2_Login.py")