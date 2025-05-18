from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/location', methods=['POST'])
def location():
    try:
        print("Received request headers:", dict(request.headers))
        data = request.get_json()
        print("Received raw data:", data)
        
        location_data = {
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "accuracy": data.get("accuracy"),
            "altitude": data.get("altitude"),
            "altitudeAccuracy": data.get("altitudeAccuracy"),
            "heading": data.get("heading"),
            "speed": data.get("speed"),
            "timestamp": data.get("timestamp"),
            "received_at": datetime.now().isoformat()
        }
        
        print("Processed location data:", location_data)
        
        return jsonify({
            "status": "success",
            "message": "Location received",
            "data": location_data
        }), 200
        
    except Exception as e:
        print("Error processing location:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)