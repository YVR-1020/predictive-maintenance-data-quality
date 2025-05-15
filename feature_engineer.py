def engineer_features(df):
    df['temp_avg_3'] = df['temperature'].rolling(3).mean()
    df['vibration_std_3'] = df['vibration'].rolling(3).std()
    return df.dropna()
