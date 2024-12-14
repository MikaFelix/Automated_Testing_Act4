from flask import Flask, request, jsonify, render_template, session
import requests
import time

app = Flask(__name__)
app.secret_key = "ipeep_secret_key"  # For session management

# Cache for storing query history
CACHE_TIMEOUT = 300  # 5 minutes
cache = {"timestamp": 0, "data": None}

# API endpoint for IP geolocation
IP_API_URL = "https://ipapi.co/json/"  # Replace with your API endpoint if needed

# Helper function to fetch IP and geolocation info
def fetch_ip_info():
    # Use cache to reduce API calls
    if cache["data"] and time.time() - cache["timestamp"] < CACHE_TIMEOUT:
        return cache["data"]

    response = requests.get(IP_API_URL)
    if response.status_code == 200:
        cache["data"] = response.json()
        cache["timestamp"] = time.time()
        return cache["data"]
    else:
        return {"error": "Failed to fetch data from IP API"}

@app.route("/")
def index():
    ip_info = fetch_ip_info()
    device_info = {
        "platform": request.user_agent.platform,
        "browser": request.user_agent.browser,
        "version": request.user_agent.version,
        "language": request.user_agent.language,
    }

    # Initialize query history in session
    if "query_history" not in session:
        session["query_history"] = []

    # Add current query to history
    session["query_history"].append(ip_info)
    session.modified = True

    return render_template(
        "index.html",
        ip_info=ip_info,
        device_info=device_info,
        query_history=session["query_history"],
    )


if __name__ == "__main__":
    app.run(debug=True)
