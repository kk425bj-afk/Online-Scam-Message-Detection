🛡️ Online Scam Message Detection (OSMD)

📌 Project Overview

Online Scam Message Detection (OSMD) is a machine learning project that classifies text messages as Spam or Ham (Normal). It uses Natural Language Processing (NLP) and a calibrated machine learning model to estimate the probability that a message is spam.

The project includes an interactive web application built with Streamlit.

🎯 Objectives

- Detect potentially fraudulent or unwanted messages.
- Estimate spam and ham probabilities.
- Present predictions through a simple, interactive interface.
- Apply data cleaning, feature extraction, model evaluation, and probability calibration.

✨ Features

- Spam and Ham message classification.
- Spam and Ham probability display.
- Spam confidence indicator.
- Interactive message input.
- Real-time prediction through a Streamlit interface.
- Dark cybersecurity-themed UI.

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Linear Support Vector Classifier (LinearSVC)
- CalibratedClassifierCV
- Joblib
- Streamlit

📂 Project Structure

OSMD/
├── data/
│   ├── raw/
│   └── processed/
│       └── cleaned_messages.csv
├── notebook/
├── src/
│   ├── app_backup.py
│   ├── osmd_tuned_pipeline.pkl
│   └── osmd_calibrated_model.pkl
└── README.md

⚙️ How to Run the Project

1. Install dependencies

pip install streamlit pandas numpy scikit-learn joblib

2. Run the Streamlit application

From the project root directory, run:

python -m streamlit run src/app_backup.py

The application will open in your browser.

📊 Model Evaluation

The calibrated model was evaluated on a stratified train-test split.

- Accuracy: approximately 99.23%
- Spam Precision: approximately 99%
- Spam Recall: approximately 95%
- Spam F1-score: approximately 97%

These results apply to the project's current test split and may differ on new messages.

⚠️ Limitations

- Predictions are estimates, not proof that a message is fraudulent or safe.
- Performance may vary on messages that differ from the training dataset.
- The model should not be used as the sole basis for financial or security decisions.

🚀 Future Improvements

- Expand the dataset with more diverse scam messages.
- Improve the interface and user experience.
- Evaluate performance on new, unseen message sources.
- Deploy the application online.

👨‍💻 Author

Developed as a machine learning and data science project to explore text classification, NLP, and interactive ML applications.