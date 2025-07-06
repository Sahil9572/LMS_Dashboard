import joblib
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Path to save/load the model
MODEL_PATH = 'E:\student_ai_dashboard\model\model.pkl'

# Features used for training and prediction
FEATURE_COLUMNS = [
    'study_hours_per_day',
    'sleep_hours',
    'social_media_hours',
    'netflix_hours',
    'attendance_percentage',
    'motivation_level',
    'time_management_score',
    'exam_anxiety_score'
]

# ✅ Train the model and save it to model/model.pkl
def train_and_save_model(df):
    X = df[FEATURE_COLUMNS]
    y = df['exam_score']

    model = LinearRegression()
    model.fit(X, y)

    # Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    # Predict on training data for testing
    df['predicted_score'] = model.predict(X).round(2)

    # Print RMSE for info
    rmse = mean_squared_error(y, df['predicted_score'], squared=False)
    print(f"✅ Model trained. RMSE: {rmse:.2f}")

    return df

# ✅ Predict scores using saved model
def predict_scores(df):
    # Check if model exists
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"❌ Model not found at {MODEL_PATH}. Please train it first.")

    model = joblib.load(MODEL_PATH)

    # Predict and round off
    df['predicted_score'] = model.predict(df[FEATURE_COLUMNS]).round(2)
    return df
