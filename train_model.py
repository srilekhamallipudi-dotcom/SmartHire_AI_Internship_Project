import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

import pickle

# ================= LOAD DATASET ================= #

df = pd.read_csv("Resume.csv")

# ================= CHECK COLUMNS ================= #

print(df.columns)

# ================= INPUT & OUTPUT ================= #

X = df["Resume_str"]

y = df["Category"]

# ================= TF-IDF ================= #

vectorizer = TfidfVectorizer(stop_words="english")

X_vectorized = vectorizer.fit_transform(X)

# ================= TRAIN TEST SPLIT ================= #

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# ================= MODEL ================= #

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ================= PREDICTION ================= #

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# ================= SAVE MODEL ================= #

pickle.dump(model, open("model.pkl", "wb"))

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model Saved Successfully")