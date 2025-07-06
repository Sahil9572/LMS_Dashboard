import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set style once
sns.set(style="whitegrid")

# ✅ 1. Correlation heatmap
def plot_correlation_heatmap(df):
    try:
        plt.figure(figsize=(10, 8))
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("📊 Correlation Heatmap of Student Attributes")
        os.makedirs("output/plots", exist_ok=True)
        plt.savefig("output/plots/correlation_heatmap.png")
        plt.close()
        print("✅ Saved: correlation_heatmap.png")
    except Exception as e:
        print(f"❌ Error generating heatmap: {e}")

# ✅ 2. Actual vs. Predicted scatter plot
def plot_actual_vs_predicted(df):
    try:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='exam_score', y='predicted_score', data=df, color='blue', s=60)
        plt.plot([df['exam_score'].min(), df['exam_score'].max()],
                 [df['exam_score'].min(), df['exam_score'].max()],
                 color='red', linestyle='--', label='Perfect Prediction')
        plt.xlabel("Actual Exam Score")
        plt.ylabel("Predicted Exam Score")
        plt.title("🎯 Actual vs. Predicted Exam Score")
        plt.legend()
        os.makedirs("output/plots", exist_ok=True)
        plt.savefig("output/plots/actual_vs_predicted.png")
        plt.close()
        print("✅ Saved: actual_vs_predicted.png")
    except Exception as e:
        print(f"❌ Error generating scatter plot: {e}")
