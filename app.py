# app.py
from flask import Flask, render_template, jsonify
from scaler import get_system_metrics

app = Flask(__name__)

@app.route("/")
def home():
    # Serve the main dashboard
    return render_template("index.html")

@app.route("/simulate")
def simulate():
    # Fetch system metrics from scaler.py
    data = get_system_metrics()
    return jsonify(data)

if __name__ == "__main__":
    # Run Flask server on localhost:5000
    app.run(debug=True)