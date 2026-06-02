import streamlit as st
from mongodb import db

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

users_collection = db["users"]

st.title("🔐 User Login")

email = st.text_input("Enter Email")
password = st.text_input("Enter Password", type="password")

if st.button("Login"):

    user = users_collection.find_one(
        {
            "email": email,
            "password": password
        }
    )

    if user:

        st.session_state["logged_in"] = True
        st.session_state["user_email"] = email
        st.session_state["user_name"] = user["name"]

        st.switch_page("pages/3_Upload_Resume.py")

    else:

        st.error("❌ Invalid Email or Password")