def generate_feedback(row):
    fb = []

    if row['study_hours_per_day'] < 2:
        fb.append("Increase daily study time.")
    if row['sleep_hours'] < 6:
        fb.append("Improve sleep hygiene.")
    if row['social_media_hours'] > 3:
        fb.append("Reduce social media usage.")
    if row['netflix_hours'] > 2:
        fb.append("Too much time on Netflix.")
    if row['attendance_percentage'] < 70:
        fb.append("Improve attendance.")
    if row['motivation_level'] < 5:
        fb.append("Work on motivation.")
    if row['exam_anxiety_score'] > 7:
        fb.append("Manage exam anxiety.")

    return " ".join(fb) if fb else "Keep up the good work!"

def apply_feedback(df):
    df['ai_feedback'] = df.apply(generate_feedback, axis=1)
    return df
