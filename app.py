from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Remote Patient Monitoring</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #e0f7fa, #f5f7fa);
            min-height: 100vh;
        }

        .header {
            background: #167d8d;
            color: white;
            padding: 25px;
            text-align: center;
        }

        .header h1 {
            margin: 0;
            font-size: 32px;
        }

        .header p {
            margin: 8px 0 0;
        }

        .dashboard {
            max-width: 1100px;
            margin: 40px auto;
            padding: 20px;
        }

        .welcome {
            text-align: center;
            margin-bottom: 30px;
        }

        .welcome h2 {
            color: #167d8d;
            font-size: 28px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }

        .card {
            background: purple;
            padding: 25px 15px;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.10);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
        }

        .icon {
            font-size: 40px;
        }

        .card h3 {
            color: #333;
        }

        .value {
            font-size: 25px;
            font-weight: bold;
            color: #167d8d;
        }

        .status {
            color: #28a745;
            font-weight: bold;
        }

        .alert {
            margin-top: 30px;
            background: #fff3cd;
            border-left: 6px solid #ffc107;
            padding: 18px;
            border-radius: 10px;
            color: #664d03;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
        }

        @media (max-width: 800px) {
            .cards {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 500px) {
            .cards {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

    <div class="header">
        <h1>🏥 Remote Patient Monitoring Platform</h1>
        <p>Smart Healthcare Monitoring Dashboard</p>
    </div>

    <div class="dashboard">

        <div class="welcome">
            <h2>Patient Health Dashboard</h2>
            <p>Real-time monitoring of vital health parameters</p>
        </div>

        <div class="cards">

            <div class="card">
                <div class="icon">❤️</div>
                <h3>Heart Rate</h3>
                <div class="value">78 BPM</div>
                <p class="status">● Normal</p>
            </div>

            <div class="card">
                <div class="icon">🩸</div>
                <h3>Blood Pressure</h3>
                <div class="value">120/80</div>
                <p class="status">● Stable</p>
            </div>

            <div class="card">
                <div class="icon">🌡️</div>
                <h3>Temperature</h3>
                <div class="value">98.6 °F</div>
                <p class="status">● Normal</p>
            </div>

            <div class="card">
                <div class="icon">🫁</div>
                <h3>Oxygen Level</h3>
                <div class="value">98%</div>
                <p class="status">● Normal</p>
            </div>

        </div>

        <div class="alert">
            <strong>⚠️ Doctor Alerts:</strong>
            Active — Patient is currently being monitored remotely.
        </div>

    </div>

    <footer>
        Predictive Healthcare Analytics System © 2026
    </footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)