import streamlit as st
from mongodb import reports_collection

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

st.title("📜 Report History")

user_email = st.session_state.get("user_email")

reports = reports_collection.find(
    {"user_email": user_email}
)

for report in reports:

    st.subheader(report.get("resume_name", "Unknown Resume"))

    st.write(
        "🎯 Predicted Role:",
        report.get("predicted_role", "N/A")
    )

    st.write(
        "📊 ATS Score:",
        report.get("ats_score", "N/A")
    )

    st.write(
        "🤖 Confidence:",
        report.get("confidence", "N/A")
    )

    st.divider()