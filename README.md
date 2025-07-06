# 🎓 AI-Powered LMS Dashboard

This project is an AI-powered Learning Management System (LMS) Dashboard built using **Flask**, **Pandas**, **Scikit-learn**, and **Joblib**.  
It allows users to upload student habit datasets (CSV), predicts their exam scores using a trained ML model, and provides intelligent feedback.

---

## 🚀 Key Features

- 📊 Upload student data (CSV format)
- 🤖 Predict exam scores based on learning behavior
- 🧠 Generate AI-powered performance feedback
- 📉 Visualize correlation and prediction accuracy (offline/CLI)
- 🌐 Flask-based interactive dashboard

---

## 🧠 AI Model Details

- **Model Used:** Linear Regression (Scikit-learn)
- **Training Features:**
  - Study hours per day
  - Sleep hours
  - Social media hours
  - Netflix hours
  - Attendance %
  - Motivation level
  - Time management score
  - Exam anxiety score
- **Target:** Exam score

---

## 🗂️ Project Structure

├── app.py # Flask application
├── run_pipeline.py # Offline CLI runner
├── model/
│ └── model.pkl # Trained ML model
├── data/
│ └── student_habits.csv # Input dataset (CSV)
├── utils/
│ ├── predictor.py # ML training & prediction
│ ├── feedback.py # AI feedback logic
│ ├── loader.py # CSV loading helper
│ └── visualizer.py # Heatmap & scatter plot
├── templates/
│ └── index.html # Dashboard UI
├── static/
│ └── style.css # Optional styling
└── requirements.txt # Required Python packages

yaml
Copy
Edit
