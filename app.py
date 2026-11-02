from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker & Kubernetes Assignment</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #0d1b2a, #1b263b, #415a77);
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                text-align: center;
                max-width: 500px;
                width: 100%;
            }
            h1 {
                color: #00b4d8;
                font-size: 26px;
                margin-bottom: 10px;
            }
            h2 {
                color: #90e0ef;
                font-size: 18px;
                margin-bottom: 20px;
                font-weight: 500;
            }
            p {
                color: #e0e1dd;
                font-size: 20px;
                margin: 8px 0;
            }
            .badge {
                display: inline-block;
                background: #0077b6;
                color: white;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 14px;
                margin-top: 15px;
                font-weight: bold;
                letter-spacing: 0.5px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Docker and Kubernetes Assignment</h1>
            <h2>Application is Running Successfully!</h2>
            <p>Welcome to our Python Flask Application.</p>
            <p>Deployment using Docker and Kubernetes.</p>
            <div class="badge">Name: Om Sinkar | PRN: 202301040197</div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Docker-Kubernetes-Demo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)