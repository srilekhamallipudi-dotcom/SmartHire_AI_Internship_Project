import streamlit as st
from mongodb import reports_collection

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")
with st.sidebar:

    if st.button("🚪 Logout"):

        st.session_state.clear()

        st.switch_page("app.py")
import pickle
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ================= DOWNLOAD NLTK ================= #

nltk.download("stopwords")
nltk.download("wordnet")

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Role Prediction",
    page_icon="🤖",
    layout="wide"
)

# ================= LOAD MODEL ================= #

model = pickle.load(open("model.pkl", "rb"))

tfidf = pickle.load(open("vectorizer.pkl", "rb"))

# ================= CUSTOM CSS ================= #

page_style = """
<style>

.stApp {
    background: linear-gradient(rgba(0,0,0,0.82),
    rgba(0,0,0,0.82)),
    url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

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

.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 25px;
}

.role-box {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    padding: 25px;
    border-radius: 18px;
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

h1, h2, h3, p {
    color: white !important;
}

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
        🤖 AI Role Prediction
    </div>

    <div class="sub-title">
        Machine Learning Based Resume Role Prediction System
    </div>
    """,
    unsafe_allow_html=True
)

# ================= GET RESUME ================= #

resume_text = st.session_state.get("resume_text", "")

# ================= CLEAN FUNCTION ================= #

def clean_resume(text):

    text = re.sub(r"http\\S+", " ", text)

    text = re.sub(r"[^a-zA-Z]", " ", text)

    text = text.lower()

    words = text.split()

    stop_words = stopwords.words("english")

    words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()

    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

# ================= CHECK RESUME ================= #

if resume_text:

    st.success("✅ Resume Loaded Successfully")

    # ================= CLEAN ================= #

    cleaned_resume = clean_resume(resume_text)

    # ================= TFIDF ================= #

    transformed_resume = tfidf.transform([cleaned_resume])

    # ================= PREDICT ================= #

    prediction = model.predict(transformed_resume)[0]

    # ================= ROLE MAPPING ================= #

    if prediction == "Engineering":
        prediction = "Software Engineer"

    elif prediction == "Data Science":
        prediction = "Data Analyst / Data Scientist"

    elif prediction == "Java Developer":
        prediction = "Backend Java Developer"

    elif prediction == "Testing":
        prediction = "QA Engineer"

    elif prediction == "HR":
        prediction = "HR Specialist"

    elif prediction == "Web Designing":
        prediction = "Frontend Web Developer"

    # ================= CONFIDENCE ================= #

    confidence = round(
        max(model.predict_proba(transformed_resume)[0]) * 100,
        2
    )
    # ================= SAVE REPORT IN MONGODB ================= #
    st.write(st.session_state)
    user_email = st.session_state.get("user_email", "Unknown")
    resume_filename = st.session_state.get(
    "resume_filename",
    "Unknown Resume"
    )

    reports_collection.update_one(
        {
            "user_email": user_email},
        {

            "$set": {
                "user_email": user_email,
                "resume_name": resume_filename,
                "predicted_role": prediction,
                "confidence": confidence
        }
    },
    upsert=True
)
    # ================= RESULT ================= #

    st.markdown(
        f"""
        <div class="role-box">

        🎯 Predicted Role: {prediction}

        </div>
        """,
        unsafe_allow_html=True
    )

    # ================= CONFIDENCE UI ================= #

    st.markdown(
        """
        <div class="card">

        <h2>📊 Prediction Confidence</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(confidence / 100)

    st.success(f"ML Confidence Score: {confidence}%")

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
        "power bi",
        "excel",
        "tableau"
    ]

    detected_skills = []

    lower_text = resume_text.lower()

    for skill in skills:

        if skill in lower_text:
            detected_skills.append(skill)

    # ================= DETECTED SKILLS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>✅ Detected Skills</h2>

        </div>
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

        st.warning("No technical skills detected.")

    # ================= CAREER INSIGHTS ================= #

    st.markdown(
        """
        <div class="card">

        <h2>📈 Career Insights</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        f"""
        SmartHire AI analyzed the uploaded resume using
        NLP preprocessing, TF-IDF vectorization,
        and Logistic Regression Machine Learning model.

        Predicted Career Role:
        {prediction}
        """
    )

    # ================= MODEL INFO ================= #

    st.markdown(
        """
        <div class="card">

        <h2>🧠 AI/ML Technologies Used</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write([
        "Natural Language Processing (NLP)",
        "TF-IDF Vectorization",
        "Logistic Regression",
        "Resume Dataset Training",
        "Machine Learning Classification"
    ])

else:

    st.warning("⚠ Please upload resume first in Upload Resume page")