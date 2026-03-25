from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

active_servers = 2


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulate")
def simulate():

    global active_servers

    cpu = random.randint(20, 100)
    processing_time = round(random.uniform(0.1, 1.5), 2)

    if cpu > 75:
        suggestion = "Horizontal Scaling Recommended"
        active_servers += 1

    elif cpu < 30 and active_servers > 1:
        suggestion = "Scale Down Servers"
        active_servers -= 1

    else:
        suggestion = "System Stable"

    data = {
        "cpu": cpu,
        "processing_time": processing_time,
        "servers": active_servers,
        "suggestion": suggestion,
        "time": int(time.time())
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)