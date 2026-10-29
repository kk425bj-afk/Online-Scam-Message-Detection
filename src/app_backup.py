import streamlit as st
import joblib

st.set_page_config(
    page_title="OSMD | Scam Detection",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0B1220;
    color: #F1F5F9;
}

h1, h2, h3 {
    color: #EAF2FF;
}

.stTextArea textarea,
.stTextArea textarea:focus {
    background-color: #172338 !important;
    color: #FFFFFF !important;
    border: 1px solid #38516F !important;
    border-radius: 12px;
    caret-color: #FFFFFF;
}

.stTextArea label {
    color: #FFFFFF !important;
}

.stTextArea textarea::placeholder {
    color: #FFFFFF !important;
    opacity: 1;
}

.stButton button {
    background-color: #147DCE;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #0965AC;
    color: white;
}

.result-card {
    background: #172338;
    border: 1px solid #2C405B;
    border-radius: 12px;
    padding: 12px 16px;
    margin-bottom: 8px;
}

.card-label {
    color: #A9BCD5;
    font-size: 14px;
    margin-bottom: 5px;
}

.card-value {
    font-size: 25px;
    font-weight: 700;
}

.spam-value {
    color: #FF737D;
}

.ham-value {
    color: #43D6A0;
}

.confidence-label {
    color: #DCE8F8;
    font-size: 15px;
    font-weight: 600;
    margin: 8px 0;
}

.result-alert {
    padding: 15px 18px;
    border-radius: 12px;
    margin-top: 14px;
    font-size: 17px;
    font-weight: 600;
}

.spam-alert {
    background: #351B29;
    border: 1px solid #D94C58;
    color: #FF8991;
}

.ham-alert {
    background: #143329;
    border: 1px solid #26966C;
    color: #61E0AC;
}
</style>
""", unsafe_allow_html=True)

calibrated_model = joblib.load("src/osmd_calibrated_model.pkl")

st.title("Online Scam Message Detection")
st.write("Welcome to OSMD!")

message = st.text_area("Enter your message here:")

if st.button("Check Message"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        prediction = calibrated_model.predict([message])[0]
        probabilities = calibrated_model.predict_proba([message])[0]

        spam_index = list(calibrated_model.classes_).index("spam")
        spam_probability = probabilities[spam_index]

        ham_index = list(calibrated_model.classes_).index("ham")
        ham_probability = probabilities[ham_index]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div class="result-card">
                <div class="card-label">Spam Probability</div>
                <div class="card-value spam-value">
                    {spam_probability * 100:.2f}%
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="result-card">
                <div class="card-label">Ham Probability</div>
                <div class="card-value ham-value">
                    {ham_probability * 100:.2f}%
                </div>
            </div>
            """, unsafe_allow_html=True)

        if spam_probability >= 0.70:
            confidence = "High"
            bar_color = "#E05260"
        elif spam_probability >= 0.40:
            confidence = "Medium"
            bar_color = "#E5A33D"
        else:
            confidence = "Low"
            bar_color = "#35B889"

        st.markdown(f"""
        <div class="confidence-label">
            Spam Confidence: {confidence}
        </div>
        <div style="
            background-color: #26364D;
            border-radius: 10px;
            height: 12px;
            overflow: hidden;
            margin-bottom: 14px;
        ">
            <div style="
                width: {spam_probability * 100:.2f}%;
                background-color: {bar_color};
                height: 12px;
                border-radius: 10px;
            "></div>
        </div>
        """, unsafe_allow_html=True)

        if prediction == "spam":
            st.markdown("""
            <div class="result-alert spam-alert">
                🚨 SPAM — This message may be fraudulent.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-alert ham-alert">
                ✅ HAM — This message appears normal.
            </div>
            """, unsafe_allow_html=True)

        st.write("Prediction:", prediction.upper())