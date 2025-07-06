def predict_exam_score(df):
    features = [
        'study_hours_per_day',
        'sleep_hours',
        'social_media_hours',
        'netflix_hours',
        'attendance_percentage',
        'motivation_level',
        'time_management_score',
        'exam_anxiety_score'
    ]
    X = df[features]
    y = df['exam_score']

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)

    df['predicted_score'] = model.predict(X).round(2)
    return df, model
