from sklearn.linear_model import LogisticRegression

def train_model(df):
    df['label'] = (df['vibration'] > 0.05).astype(int)
    X = df[['temperature', 'vibration', 'rpm']]
    y = df['label']
    model = LogisticRegression().fit(X, y)
    return model

def predict(model, df):
    return model.predict(df[['temperature', 'vibration', 'rpm']])
