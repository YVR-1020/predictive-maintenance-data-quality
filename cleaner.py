import pandas as pd

def clean_data(df):
    df = df.dropna()  # or use fillna(method='ffill')
    df = df[df['temperature'] > 0]  # remove invalid readings
    return df
