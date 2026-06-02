import streamlit as st
from mongodb import reports_collection

if not st.session_state.get("logged_in", False):

    st.switch_page("app.py")
with st.sidebar:

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.switch_page("app.py")
from mongodb import resume_collection

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="ATS Analysis",
    page_icon="🤖",
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
    padding: 30px;
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
    margin: 6px;
    font-size: 16px;
}

/* ================= RESUME TEXT ================= */

.resume-text {
    color: #f1f5f9;
    line-height: 1.8;
    font-size: 16px;
}

/* ================= PROGRESS BAR ================= */

.stProgress > div > div > div > div {
    background-color: #22c55e;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ================= HEADER ================= #

st.markdown(
    """
    <div class="main-title">
        🤖 ATS Resume Analysis
    </div>

    <div class="sub-title">
        Intelligent AI-powered resume evaluation platform
    </div>
    """,
    unsafe_allow_html=True
)

# ================= GET RESUME FROM SESSION ================= #

resume_text = st.session_state.get("resume_text", "")

# ================= SKILL DATABASE ================= #

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

# ================= ANALYSIS ================= #

if resume_text:

    st.success("✅ Resume Loaded Successfully")

    # ================= SHOW RESUME TEXT ================= #

    st.markdown(
        f"""
        <div class="card">

        <h2>📄 Extracted Resume Content</h2>

        <div class="resume-text">
        {resume_text}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ================= LOWERCASE ================= #

    resume_text_lower = resume_text.lower()

    # ================= DETECT SKILLS ================= #

    detected_skills = []

    for skill in skills:

        if skill.lower() in resume_text_lower:
            detected_skills.append(skill)

    # ================= ATS SCORE ================= #

    total_skills = len(skills)

    found_skills = len(detected_skills)

    ats_score = int((found_skills / total_skills) * 100)
    user_email = st.session_state.get("user_email", "")
    missing_skills = [skill for skill in skills if skill not in detected_skills]
    import datetime
       # ================= ROLE + CONFIDENCE (SIMPLE LOGIC) ================= #
    if "python" in detected_skills and "machine learning" in detected_skills:
        predicted_role = "Data / ML Engineer"
        confidence = 85
    elif "javascript" in detected_skills:
        predicted_role = "Frontend Developer"
        confidence = 75
    else:
        predicted_role = "General Developer"
        confidence = 60

    if not st.session_state.get("report_saved"):
        reports_collection.insert_one({
            "user_email": user_email,
            "resume_name": st.session_state.get("resume_filename", "Unknown"),
            "ats_score": ats_score,
            "detected_skills": detected_skills,
            "missing_skills": missing_skills,
            "predicted_role": predicted_role,
            "confidence": confidence,
            "created_at": datetime.datetime.now()
        })
        st.session_state["report_saved"] = True
    # ================= MISSING SKILLS ================= #

    
    result = resume_collection.update_one(
    {"resume_text": resume_text},
    {
        "$set": {
            "ats_score": ats_score,
            "detected_skills": detected_skills,
            "missing_skills": missing_skills
        }
    }
)

    st.write("Matched:", result.matched_count)
    st.write("Modified:", result.modified_count)

    # ================= ATS SCORE DISPLAY ================= #

    st.markdown(
        f"""
        <div class="card">

        <h2>📊 ATS Score: {ats_score}%</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(ats_score / 100)

    # ================= DETECTED SKILLS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>✅ Detected Skills</h2>

        """,
        unsafe_allow_html=True
    )

    if detected_skills:

        for skill in detected_skills:

            st.markdown(
                f"<span class='skill'>{skill}</span>",
                unsafe_allow_html=True
            )

    else:
        st.warning("No matching skills detected.")

    st.markdown("</div>", unsafe_allow_html=True)

    # ================= MISSING SKILLS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>⚠ Missing Skills</h2>

        """,
        unsafe_allow_html=True
    )

    for skill in missing_skills:

        st.markdown(
            f"<span class='skill'>{skill}</span>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ================= AI FEEDBACK ================= #

    st.markdown(
        """
        <div class="card">

        <h2>💡 AI Feedback</h2>

        """,
        unsafe_allow_html=True
    )

    if ats_score >= 75:
        st.success(
            "Excellent Resume! Your profile matches most ATS requirements."
        )

    elif ats_score >= 50:
        st.warning(
            "Good Resume. Add more relevant technical skills to improve ATS performance."
        )

    else:
        st.error(
            "Resume needs improvement. Add more industry-relevant skills and projects."
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= NO RESUME ================= #

else:

    st.warning("⚠ Please upload resume first in Upload Resume page")