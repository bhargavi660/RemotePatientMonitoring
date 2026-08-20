from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Remote Patient Monitoring Platform</h1>
    <h3>Welcome to the Healthcare Dashboard</h3>
    <p>Monitor patient health records and analytics.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)