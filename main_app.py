import streamlit as st


if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")
with st.sidebar:

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.switch_page("app.py")

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ================= CUSTOM CSS ================= #

page_style = """
<style>

/* ================= MAIN BACKGROUND ================= */

.stApp {
    background: linear-gradient(rgba(8,8,8,0.88),
    rgba(8,8,8,0.88)),
    url("https://images.unsplash.com/photo-1498050108023-c5249f4df085");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ================= HIDE STREAMLIT MENU & FOOTER ================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ================= MAIN TITLE ================= */

.main-title {
    font-size: 72px;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
    letter-spacing: -2px;
}

/* ================= SUB TITLE ================= */

.sub-title {
    font-size: 24px;
    color: #cbd5e1;
    margin-top: -10px;
    margin-bottom: 30px;
}

/* ================= GLASS CARD ================= */

.glass-card {
    background: rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 24px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    margin-top: 30px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.3);
    transition: 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 12px 40px rgba(0,0,0,0.4);
}

/* ================= SECTION TITLE ================= */

.section-title {
    color: #38bdf8;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 15px;
}

/* ================= PARAGRAPH TEXT ================= */

p {
    color: #e2e8f0;
    font-size: 18px;
    line-height: 1.8;
}

/* ================= LIST ITEMS ================= */

li {
    color: #f8fafc;
    font-size: 18px;
    margin-bottom: 10px;
}

/* ================= METRIC CARDS ================= */

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 20px;
    backdrop-filter: blur(8px);
    box-shadow: 0px 5px 20px rgba(0,0,0,0.25);
    text-align: center;
}

/* ================= SUCCESS BOX ================= */

.stAlert {
    border-radius: 14px;
}

/* ================= FOOTER TEXT ================= */

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    font-size: 15px;
    letter-spacing: 0.5px;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ================= HERO SECTION ================= #

st.markdown(
    """
    <div class="main-title">
        SmartHire AI
    </div>

    <div class="sub-title">
        Intelligent Resume Screening & ATS Optimization Platform
    </div>
    """,
    unsafe_allow_html=True
)

# ================= ABOUT PLATFORM ================= #

st.markdown(
    """
    <div class="glass-card">

    <div class="section-title">
        📌 About the Platform
    </div>

    <p>
    SmartHire AI is an advanced AI-powered resume analysis platform
    developed to streamline candidate screening and improve hiring efficiency
    through intelligent resume parsing and ATS optimization.
    </p>

    <p>
    The platform automatically extracts resume content, identifies
    technical skills, evaluates candidate profiles, generates
    dynamic ATS-based performance scores, and provides recruiter-ready
    ATS PDF reports with automated email integration using Gmail SMTP.
    </p>

    <br>

    <div class="section-title">
        🚀 Core Functionalities
    </div>

    <ul>
        <li>AI-Based Resume Parsing</li>
        <li>Dynamic ATS Score Evaluation</li>
        <li>Technical Skill Intelligence</li>
        <li>Missing Skill Detection</li>
        <li>Resume Role Classification</li>
        <li>Interactive Resume Analytics Dashboard</li>
        <li>Automated ATS PDF Report Generation</li>
        <li>Recruiter Email Integration using Gmail SMTP</li>
        <li>AI-Based Resume Recommendation System</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
)

# ================= HOW IT WORKS ================= #

st.markdown(
    """
    <div class="glass-card">

    <div class="section-title">
        ⚙ How SmartHire AI Works
    </div>

    <ul>
        <li>📄 Upload Resume in PDF format</li>

        <li>🧠 SmartHire AI extracts and analyzes resume content using AI-powered resume parsing</li>

        <li>🔍 Technical skills are automatically identified from the uploaded resume</li>

        <li>📊 ATS score is calculated based on industry-relevant skill matching</li>

        <li>🤖 AI predicts the most suitable technical career role</li>

        <li>📈 Interactive analytics dashboard visualizes resume performance insights</li>

        <li>📥 Generate recruiter-ready ATS PDF reports instantly</li>

        <li>📧 Send ATS reports directly to recruiters using Gmail SMTP integration</li>

    </ul>

    </div>
    """,
    unsafe_allow_html=True
)

# ================= PLATFORM INFO ================= #

st.info(
    "SmartHire AI helps candidates optimize resumes for modern Applicant Tracking Systems (ATS) and improve hiring opportunities."
)

# ================= METRICS ================= #

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Resume Intelligence", "Advanced")

with col2:
    st.metric("NLP Processing", "Enabled")

with col3:
    st.metric("ATS Evaluation", "Smart AI")

# ================= SUCCESS MESSAGE ================= #

st.success("✅ SmartHire AI Platform Initialized Successfully")

# ================= FOOTER ================= #

st.markdown(
    """
    <div class="footer">
        Developed by Srilekha • SmartHire AI
    </div>
    """,
    unsafe_allow_html=True
)