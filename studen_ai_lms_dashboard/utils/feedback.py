def generate_feedback(df):
    def feedback(row):
        tips = []
        if row['study_hours_per_day'] < 2:
            tips.append("Study more.")
        if row['sleep_hours'] < 6:
            tips.append("Sleep more.")
        if row['social_media_hours'] > 3:
            tips.append("Reduce social media.")
        return " ".join(tips) if tips else "Good performance!"
    
    df['ai_feedback'] = df.apply(feedback, axis=1)
    return df
