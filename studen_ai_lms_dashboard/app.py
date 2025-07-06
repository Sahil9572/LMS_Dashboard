from flask import Flask, render_template, request
import pandas as pd
import os

# Reuse your core modules from utils/
from utils.loader import load_data
from utils.feedback import generate_feedback  # renamed apply_feedback
from utils.predictor import predict_scores, train_and_save_model
from utils.visualizer import plot_correlation_heatmap, plot_actual_vs_predicted

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_csv(file)

            # Optional: Train + save model (only for testing phase)
            # df = train_and_save_model(df)

            # Predict + Feedback
            df = predict_scores(df)
            df = generate_feedback(df)

            # Visuals (optional for Flask)
            plot_correlation_heatmap(df)
            plot_actual_vs_predicted(df)

            # Save
            os.makedirs("output", exist_ok=True)
            df.to_csv("output/final_results.csv", index=False)

            # Display
            results = df[['student_id', 'exam_score', 'predicted_score', 'ai_feedback']].to_dict(orient='records')

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
