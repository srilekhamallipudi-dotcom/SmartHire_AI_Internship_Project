import streamlit as st

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🤖",
    layout="wide"
)

# ================= CUSTOM CSS ================= #

st.markdown("""
<style>

/* Background */

.stApp{
    background: linear-gradient(rgba(0,0,0,0.88),
    rgba(0,0,0,0.88)),
    url("https://images.unsplash.com/photo-1498050108023-c5249f4df085");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Hide Streamlit UI */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Title */

.main-title{
    font-size:70px;
    font-weight:800;
    color:white;
    margin-bottom:0px;
}

.sub-title{
    color:#cbd5e1;
    font-size:24px;
    margin-bottom:30px;
}

/* Glass Card */

.glass{
    background:rgba(255,255,255,0.08);
    padding:30px;
    border-radius:20px;
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.1);
    margin-top:20px;
}

.section{
    color:#38bdf8;
    font-size:28px;
    font-weight:bold;
}

p,li{
    color:white;
    font-size:18px;
    line-height:1.8;
}

</style>
""", unsafe_allow_html=True)

# ================= TOP BAR ================= #

col1, col2 = st.columns([8,2])

with col2:

    st.write("")

    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")

    if st.button("📝 Register", use_container_width=True):
        st.switch_page("pages/1_Register.py")

# ================= HERO SECTION ================= #

st.markdown("""
<div class="main-title">
🤖 SmartHire AI
</div>

<div class="sub-title">
Intelligent Resume Screening & ATS Optimization Platform
</div>
""", unsafe_allow_html=True)

# ================= ABOUT ================= #

st.markdown("""
<div class="glass">

<div class="section">
📌 About SmartHire AI
</div>

<p>
SmartHire AI is an AI-powered resume analysis platform designed
to help candidates optimize their resumes for Applicant Tracking
Systems (ATS). The platform automatically analyzes resumes,
detects technical skills, calculates ATS scores, predicts suitable
job roles, and generates detailed reports.
</p>

</div>
""", unsafe_allow_html=True)

# ================= FEATURES ================= #

st.markdown("""
<div class="glass">

<div class="section">
🚀 Core Features
</div>

<ul>
<li>Resume Upload & Analysis</li>
<li>ATS Score Calculation</li>
<li>Technical Skill Detection</li>
<li>Missing Skill Identification</li>
<li>Role Prediction</li>
<li>Interactive Analytics Dashboard</li>
<li>PDF Report Generation</li>
<li>Email Report Sharing</li>
<li>Report History Tracking</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ================= WORKFLOW ================= #

st.markdown("""
<div class="glass">

<div class="section">
⚙ How It Works
</div>

<ul>
<li>📄 Upload Resume</li>
<li>🔍 Extract Resume Content</li>
<li>🧠 Analyze Skills</li>
<li>📊 Calculate ATS Score</li>
<li>🤖 Predict Suitable Role</li>
<li>📈 Visualize Analytics</li>
<li>📥 Download PDF Report</li>
<li>📧 Send Report via Email</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ================= METRICS ================= #

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ATS Analysis", "Enabled")

with col2:
    st.metric("Role Prediction", "AI Powered")

with col3:
    st.metric("Report Generation", "Available")

# ================= FOOTER ================= #

st.markdown("""
<br><br>
<center style='color:white'>
Developed by Srilekha • SmartHire AI
</center>
""", unsafe_allow_html=True)