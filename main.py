from flask import Flask, request, render_template
import pandas as pd
from app.cleaner import clean_data
from app.feature_engineer import engineer_features
from app.evaluator import evaluate_quality

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        file = request.files["file"]
        df = pd.read_csv(file)
        df = clean_data(df)
        df = engineer_features(df)
        results = evaluate_quality(df)
    return render_template("dashboard.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
