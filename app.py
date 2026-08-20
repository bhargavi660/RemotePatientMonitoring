from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>🏥 Remote Patient Monitoring Platform</h1>

<h2>Patient Dashboard</h2>

<ul>
    <li>❤️ Heart Rate</li>
    <li>🩸 Blood Pressure</li>
    <li>🌡 Temperature</li>
    <li>🫁 Oxygen Level</li>
</ul>

<p>Predictive Healthcare Analytics System</p>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)