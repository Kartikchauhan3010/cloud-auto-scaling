
from scaler import get_system_metrics

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    data = get_system_metrics()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
