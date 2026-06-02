import streamlit as st
from mongodb import db

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

users_collection = db["users"]

st.title("📝 User Registration")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")
password = st.text_input("Enter Password", type="password")

if st.button("Register"):

    if name and email and password:

        existing_user = users_collection.find_one(
            {"email": email}
        )

        if existing_user:
            st.error("❌ Email already registered")

        else:

            users_collection.insert_one(
                {
                    "name": name,
                    "email": email,
                    "password": password
                }
            )

            st.success("✅ Registration Successful")

    else:
        st.warning("⚠ Fill all fields")