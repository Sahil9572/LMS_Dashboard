import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def plot_actual_vs_predicted(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['student_id'], df['exam_score'], label='Actual', marker='o')
    plt.plot(df['student_id'], df['predicted_score'], label='Predicted', linestyle='--', marker='x')
    plt.xlabel("Student ID")
    plt.ylabel("Exam Score")
    plt.title("Actual vs Predicted Exam Scores")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
