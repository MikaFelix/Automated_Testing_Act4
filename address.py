from flask import Flask, render_template
import requests

app = Flask(__name__)

# API URL to fetch the IP information
IP_API_URL = "https://ipapi.co/json/"

def get_ip_info():
    try:
        response = requests.get(IP_API_URL)
        response.raise_for_status()
        data = response.json()
        
        # Extract necessary fields from the API response
        ip_info = {
            "ipv4": data.get('ip', 'N/A'),
            "ipv6": data.get('ipv6', 'N/A'),
            "isp": data.get('org', 'N/A'),
            "asn": data.get('asn', 'N/A'),
            "city": data.get('city', 'N/A'),
            "region": data.get('region', 'N/A'),
            "country": data.get('country', 'N/A')
        }
        return ip_info
    
    except requests.RequestException as e:
        return {"error": f"Error retrieving IP information: {e}"}


@app.route('/')
def index():
    # Get IP info and pass it to the template
    ip_info = get_ip_info()
    return render_template('index.html', ip_info=ip_info)

if __name__ == '__main__':
    app.run(debug=True)
