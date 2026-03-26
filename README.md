# Cloud Auto Scaling Simulator
This project simulates cloud auto-scaling behavior based on CPU load.
It dynamically increases or decreases the number of virtual instances
depending on system load.

The goal is to demonstrate how cloud platforms automatically scale
resources when demand changes.
Architecture

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python (Flask)

Modules:
- app.py → handles web server and API
- scaler.py → scaling logic
- script.js → frontend data updates
- Installation

1. Clone the repository
git clone https://github.com/Kartikchauhan3010/cloud-auto-scaling.git

2. Navigate to project
cd cloud-auto-scaling/backend

3. Install dependencies
pip install flask

4. Run the application
python app.py

Usage

- The system generates simulated CPU load.
- When load exceeds a threshold, the scaler adds instances.
- When load decreases, instances are reduced.
- Graphs display load and scaling behavior.

- Output

- Graph showing CPU load
- Graph showing number of instances
- Dynamic scaling decisions

- Future Improvements
- Integration with real cloud APIs
- Kubernetes-based scaling
- Real load testing tools
- Prometheus metrics

- http://127.0.0.1:5000
