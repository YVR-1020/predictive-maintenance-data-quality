def evaluate_quality(df):
    total = len(df)
    completeness = df.notnull().sum().sum() / (total * df.shape[1])
    consistency = 1 - df.duplicated().sum() / total
    score = 0.5 * completeness + 0.5 * consistency
    return {
        "completeness": round(completeness, 2),
        "consistency": round(consistency, 2),
        "quality_score": round(score, 2)
    }
