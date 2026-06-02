import streamlit as st

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")
with st.sidebar:

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.switch_page("app.py")
from fpdf import FPDF

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Download Report",
    page_icon="📥",
    layout="wide"
)

# ================= CUSTOM CSS ================= #

page_style = """
<style>

/* ================= BACKGROUND ================= */

.stApp {
    background: linear-gradient(rgba(0,0,0,0.82),
    rgba(0,0,0,0.82)),
    url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* ================= TITLE ================= */

.main-title {
    font-size: 60px;
    font-weight: bold;
    color: white;
}

.sub-title {
    color: #d1d5db;
    font-size: 22px;
    margin-bottom: 30px;
}

/* ================= CARD ================= */

.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 25px;
}

/* ================= TEXT ================= */

h1, h2, h3, p {
    color: white !important;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ================= HEADER ================= #

st.markdown(
    """
    <div class="main-title">
        📥 ATS Report Generator
    </div>

    <div class="sub-title">
        Download AI-powered resume analysis report
    </div>
    """,
    unsafe_allow_html=True
)

# ================= GET DATA ================= #

resume_text = st.session_state.get("resume_text", "")

# ================= SKILLS ================= #

skills = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "data science",
    "react",
    "django",
    "flask",
    "numpy",
    "pandas",
    "tensorflow",
    "communication",
    "leadership"
]

# ================= CHECK RESUME ================= #

if resume_text:

    text = resume_text.lower()

    detected_skills = []

    for skill in skills:

        if skill in text:
            detected_skills.append(skill)

    missing_skills = []

    for skill in skills:

        if skill not in detected_skills:
            missing_skills.append(skill)

    # ================= ATS SCORE ================= #

    ats_score = int((len(detected_skills) / len(skills)) * 100)

    # ================= RESUME STRENGTH ================= #

    if ats_score >= 75:
        strength = "Strong"

    elif ats_score >= 50:
        strength = "Moderate"

    else:
        strength = "Weak"

    # ================= DISPLAY ================= #

    st.markdown(
        f"""
        <div class="card">

        <h2>📊 ATS Score: {ats_score}%</h2>

        <h3>💪 Resume Strength: {strength}</h3>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">

        <h2>✅ Detected Skills</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(detected_skills)

    st.markdown(
        """
        <div class="card">

        <h2>⚠ Missing Skills</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(missing_skills)

    # ================= PDF FUNCTION ================= #

    def create_pdf():

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", "B", 20)

        pdf.cell(200, 10, "SmartHire AI Report", ln=True, align="C")

        pdf.ln(10)

        pdf.set_font("Arial", "B", 14)

        pdf.cell(200, 10, f"ATS Score: {ats_score}%", ln=True)

        pdf.cell(200, 10, f"Resume Strength: {strength}", ln=True)

        pdf.ln(10)

        # ================= DETECTED ================= #

        pdf.set_font("Arial", "B", 14)

        pdf.cell(200, 10, "Detected Skills:", ln=True)

        pdf.set_font("Arial", "", 12)

        for skill in detected_skills:

            pdf.cell(200, 10, f"- {skill}", ln=True)

        pdf.ln(5)

        # ================= MISSING ================= #

        pdf.set_font("Arial", "B", 14)

        pdf.cell(200, 10, "Missing Skills:", ln=True)

        pdf.set_font("Arial", "", 12)

        for skill in missing_skills:

            pdf.cell(200, 10, f"- {skill}", ln=True)

        pdf.ln(10)

        # ================= FEEDBACK ================= #

        pdf.set_font("Arial", "B", 14)

        pdf.cell(200, 10, "AI Feedback:", ln=True)

        pdf.set_font("Arial", "", 12)

        if ats_score >= 75:

            feedback = (
                "Excellent resume profile with strong ATS compatibility."
            )

        elif ats_score >= 50:

            feedback = (
                "Good resume. Add more advanced skills and projects."
            )

        else:

            feedback = (
                "Resume needs improvement with more relevant skills."
            )

        pdf.multi_cell(0, 10, feedback)

        # ================= SAVE ================= #

        pdf.output("ATS_Report.pdf")

    # ================= BUTTON ================= #

    if st.button("📥 Generate PDF Report"):

        create_pdf()

        with open("ATS_Report.pdf", "rb") as file:

            st.download_button(
                label="⬇ Download Report",
                data=file,
                file_name="ATS_Report.pdf",
                mime="application/pdf"
            )

        st.success("✅ PDF Report Generated Successfully")

else:

    st.warning("⚠ Please upload resume first in Upload Resume page")