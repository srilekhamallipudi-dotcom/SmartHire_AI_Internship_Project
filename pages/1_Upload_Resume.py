import streamlit as st
from PyPDF2 import PdfReader

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Upload Resume",
    page_icon="📄",
    layout="wide"
)

# ================= CUSTOM CSS ================= #

page_style = """
<style>

/* ================= BACKGROUND ================= */

.stApp {
    background: linear-gradient(rgba(0,0,0,0.78),
    rgba(0,0,0,0.78)),
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
    font-size: 58px;
    font-weight: bold;
    color: white;
}

.sub-title {
    font-size: 22px;
    color: #d1d5db;
    margin-bottom: 30px;
}

/* ================= UPLOAD BOX ================= */

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* ================= RESUME BOX ================= */

.resume-box {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 30px;
}

/* ================= TEXT ================= */

h1, h2, h3, p {
    color: white !important;
}

.resume-text {
    color: #f1f5f9;
    line-height: 1.8;
    font-size: 17px;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ================= HEADER ================= #

st.markdown(
    """
    <div class="main-title">
        📄 Resume Upload Portal
    </div>

    <div class="sub-title">
        Upload resumes for intelligent AI-powered analysis
    </div>
    """,
    unsafe_allow_html=True
)

# ================= FILE UPLOAD ================= #

uploaded_file = st.file_uploader(
    "Upload Resume (PDF Only)",
    type=["pdf"]
)

# ================= PDF PARSING ================= #

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully")

    # ================= READ PDF ================= #

    pdf_reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:

        extracted_text = page.extract_text()

        if extracted_text:
            resume_text += extracted_text

    # ================= SAVE IN SESSION ================= #

    # Resume Text
    st.session_state["resume_text"] = resume_text

    # Original Resume File
    st.session_state["resume_file"] = uploaded_file

    # ================= DISPLAY CONTENT ================= #

    st.markdown(
        f"""
        <div class="resume-box">

        <h3>📑 Parsed Resume Content</h3>

        <div class="resume-text">
            {resume_text}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ================= SUCCESS MESSAGE ================= #

    st.success(
        "🚀 Resume stored successfully for ATS Analysis and Recruiter Email System"
    )

else:

    st.warning("⚠ Please upload PDF resume to continue")