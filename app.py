import streamlit as st
import pickle


model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("feature_extraction.pkl", "rb"))


st.markdown("""
    <style>
    /* Set page background to purple */
    body {
        background-color: #4B0082;
    }

    .main {
        background-color: #4B0082;
        color:pink;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Make title and subtext white */
    .title {
        text-align: center;
        color: Black;
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .subtext {
        text-align: center;
        color: black;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Keep textarea white */
    .stTextArea textarea {
        background-color: white;
        color: black;
        border: 1px solid #ccc;
        border-radius: 10px;
        font-size: 16px;
        padding: 12px;
    }

    /* Button style */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
        border-radius: 8px;
        margin-top: 10px;
    }

    .stButton>button:hover {
        background-color: #45a049;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)


# --- PAGE CONTENT ---
st.markdown("<div class='title'>📧 Email Spam Classifier</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Check if your email is spam or ham.</div>", unsafe_allow_html=True)

# Input
email = st.text_area("Enter Email Content:")

# Predict button
if st.button("Analyze"):
    input_data = vectorizer.transform([email])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ This is a Ham Email (Not Spam)")
    else:
        st.error("⚠️ This is likely a Spam Email")
