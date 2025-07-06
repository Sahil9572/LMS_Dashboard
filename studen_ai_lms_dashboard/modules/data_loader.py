import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv("E:\student_ai_dashboard\data\enhanced_student_habits_performance_dataset.csv")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return pd.DataFrame()
