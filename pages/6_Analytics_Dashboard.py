import streamlit as st

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")
with st.sidebar:

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.switch_page("app.py")
import matplotlib.pyplot as plt

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
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

/* ================= TITLES ================= */

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
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 25px;
}

/* ================= TEXT ================= */

h1, h2, h3, p {
    color: white !important;
}

/* ================= SKILL TAG ================= */

.skill {
    background-color: #2563eb;
    color: white;
    padding: 8px 14px;
    border-radius: 10px;
    display: inline-block;
    margin: 5px;
    font-size: 15px;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ================= HEADER ================= #

st.markdown(
    """
    <div class="main-title">
        📊 Resume Analytics Dashboard
    </div>

    <div class="sub-title">
        Visual insights generated from resume analysis
    </div>
    """,
    unsafe_allow_html=True
)

# ================= GET RESUME ================= #

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

    resume_text_lower = resume_text.lower()

    detected_skills = []

    for skill in skills:

        if skill.lower() in resume_text_lower:
            detected_skills.append(skill)

    missing_skills = []

    for skill in skills:

        if skill not in detected_skills:
            missing_skills.append(skill)

    # ================= ATS SCORE ================= #

    ats_score = int((len(detected_skills) / len(skills)) * 100)

    # ================= STRENGTH ================= #

    if ats_score >= 75:
        strength = "Strong"

    elif ats_score >= 50:
        strength = "Moderate"

    else:
        strength = "Weak"

    # ================= METRICS ================= #

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Score", f"{ats_score}%")

    with col2:
        st.metric("Detected Skills", len(detected_skills))

    with col3:
        st.metric("Resume Strength", strength)

    # ================= PIE CHART ================= #

    st.markdown("## 📈 Skill Distribution")

    pie_labels = ["Detected", "Missing"]

    pie_values = [len(detected_skills), len(missing_skills)]

    fig1, ax1 = plt.subplots(figsize=(4,4))

    ax1.pie(
        pie_values,
        labels=pie_labels,
        autopct="%1.1f%%"
    )

    st.pyplot(fig1)

    # ================= BAR CHART ================= #

    st.markdown("## 📊 Resume Overview")

    chart_labels = ["Detected", "Missing"]

    chart_values = [len(detected_skills), len(missing_skills)]

    fig2, ax2 = plt.subplots(figsize=(5,3))

    ax2.bar(chart_labels, chart_values)

    st.pyplot(fig2)

    # ================= DETECTED SKILLS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>✅ Detected Skills</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    for skill in detected_skills:

        st.markdown(
            f"<span class='skill'>{skill}</span>",
            unsafe_allow_html=True
        )

    # ================= MISSING SKILLS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>⚠ Missing Skills</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    for skill in missing_skills:

        st.markdown(
            f"<span class='skill'>{skill}</span>",
            unsafe_allow_html=True
        )

    # ================= RESUME SUMMARY ================= #

    st.markdown(
        """
        <div class="card">

        <h2>📄 Resume Summary</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        f"""
        Resume contains {len(detected_skills)} detected technical skills
        and achieved an ATS score of {ats_score}%.
        """
    )

    # ================= AI RECOMMENDATIONS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>💡 AI Recommendations</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    if ats_score >= 75:

        st.success(
            "Excellent profile! Your resume matches most ATS requirements."
        )

    elif ats_score >= 50:

        st.warning(
            "Good profile. Add more advanced technical skills and projects."
        )

    else:

        st.error(
            "Resume needs improvement. Add industry-relevant skills and strong project experience."
        )

    # ================= SKILL MATCH ================= #

    st.markdown(
        """
        <div class="card">

        <h2>🎯 Skill Match Percentage</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(ats_score / 100)

    st.write(f"Skill Match: {ats_score}%")

else:

    st.warning("⚠ Please upload resume first in Upload Resume page")